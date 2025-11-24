import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import time

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Job Market Analyzer", layout="wide")

# --- 1. THE SCRAPING ENGINE (Cached so it doesn't re-run on every click) ---
@st.cache_data
def scrape_data():
    """Scrapes the fake-jobs site and returns a DataFrame."""
    base_url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    results = soup.find(id="ResultsContainer")
    job_elements = results.find_all("div", class_="card-content")
    
    data = []
    
    # Progress bar for the UI
    progress_bar = st.progress(0)
    total_jobs = 20 # Limit for speed demo
    
    for idx, job in enumerate(job_elements[:total_jobs]):
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        date = job.find("p", class_="is-small").text.strip()
        
        # Get Detail Link
        links = job.find_all("a")
        detail_url = links[1]['href']
        
        # Visit Detail Page to get description
        try:
            detail_resp = requests.get(detail_url)
            detail_soup = BeautifulSoup(detail_resp.content, "html.parser")
            desc = detail_soup.find("div", class_="content").get_text().strip()
        except:
            desc = ""

        # Simple Skill Extraction Logic
        skills_found = []
        target_skills = ['python', 'sql', 'aws', 'rest', 'linux', 'git', 'flask', 'django', 'react']
        for skill in target_skills:
            if skill in desc.lower():
                skills_found.append(skill)
        
        data.append({
            "Title": title,
            "Company": company,
            "Location": location,
            "Date": date,
            "Skills": ", ".join(skills_found) if skills_found else "Not Specified"
        })
        
        # Update progress
        progress_bar.progress((idx + 1) / total_jobs)
        time.sleep(0.1) # Be polite to the server
        
    progress_bar.empty()
    return pd.DataFrame(data)

# --- 2. THE DASHBOARD UI ---
st.title("📊 Live Job Market Analysis Pipeline")
st.markdown("""
This dashboard scrapes **Real Python Fake Jobs** in real-time, extracts key skills, 
and visualizes the demand trends.
""")

# Button to trigger refresh
if st.button("🔄 Scrape Live Data Now"):
    st.cache_data.clear()  # Clear cache to force fresh scrape

# Load Data
with st.spinner('Scraping data from the web...'):
    df = scrape_data()

# --- 3. METRICS ROW ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Jobs Scanned", len(df))
col2.metric("Unique Companies", df['Company'].nunique())
col3.metric("Top Skill", df['Skills'].mode()[0] if not df.empty else "N/A")

# --- 4. VISUALIZATION (SEABORN) ---
st.subheader("🔥 Top Skills in Demand")

# Process data for plotting
if not df.empty:
    # Split "python, sql" into individual rows
    skills_series = df['Skills'].str.split(', ', expand=True).stack()
    skills_df = pd.DataFrame(skills_series, columns=['Skill'])
    # Remove "Not Specified"
    skills_df = skills_df[skills_df['Skill'] != "Not Specified"]

    # Create Seaborn Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(y="Skill", data=skills_df, 
                  order=skills_df['Skill'].value_counts().index, 
                  palette="viridis", ax=ax)
    ax.set_xlabel("Number of Mentions")
    ax.set_ylabel("Skill")
    sns.despine()
    
    # Display in Streamlit
    st.pyplot(fig)
else:
    st.warning("No skills found in the current dataset.")

# --- 5. DATA PREVIEW & EXPORT ---
st.subheader("📋 Raw Data Explorer")
st.dataframe(df)

# Export Buttons
col_dl1, col_dl2 = st.columns(2)

# CSV Download
csv = df.to_csv(index=False).encode('utf-8')
col_dl1.download_button(
    "📥 Download as CSV",
    csv,
    "job_market_data.csv",
    "text/csv",
    key='download-csv'
)

# Excel Download (Requires openpyxl)
# We use a buffer to save the excel file in memory
import io
buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Jobs')
    
col_dl2.download_button(
    label="📥 Download as Excel",
    data=buffer,
    file_name="job_market_data.xlsx",
    mime="application/vnd.ms-excel"
)