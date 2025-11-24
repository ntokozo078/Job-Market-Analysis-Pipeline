import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd
import time
import re

# --- CONFIGURATION ---
BASE_URL = "https://realpython.github.io/fake-jobs/"
DB_NAME = "advanced_job_market.db"
# Skills we want to hunt for (must be lowercase for matching)
TARGET_SKILLS = ['python', 'sql', 'aws', 'rest', 'linux', 'git', 'flask', 'django']

def get_job_description(detail_url):
    """Visits a specific job page and returns the full text description."""
    try:
        response = requests.get(detail_url)
        soup = BeautifulSoup(response.content, "html.parser")
        # On this specific site, details are in a div with class 'content'
        # We use .get_text() to strip HTML tags and get pure text
        content_div = soup.find("div", class_="content")
        return content_div.get_text() if content_div else ""
    except Exception as e:
        return ""

def extract_skills(description):
    """Checks which target skills appear in the text."""
    found_skills = []
    # simple normalization: lowercase everything
    desc_lower = description.lower()
    
    for skill in TARGET_SKILLS:
        # We use regex to ensure we match "sql" but not "mysql" if we want strictness,
        # but for now, simple inclusion is fine.
        if skill in desc_lower:
            found_skills.append(skill)
            
    return ", ".join(found_skills) # Returns string like "python, sql"

def run_advanced_pipeline():
    print("🚀 Starting Advanced Crawler...")
    
    # 1. GET MAIN LIST
    print(f"   - Fetching main list from {BASE_URL}...")
    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    job_elements = results.find_all("div", class_="card-content")
    
    extracted_data = []
    
    # LIMIT to first 20 for speed during testing
    print("   - Processing first 20 jobs (fetching details for each)...")
    
    for job in job_elements[:20]: 
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        
        # Find the "Apply" link
        # The structure usually has links in the footer
        links = job.find_all("a")
        detail_url = links[1]['href'] # The second link is usually 'Apply'
        
        # 2. CRAWL DETAIL PAGE
        description = get_job_description(detail_url)
        
        # 3. ANALYZE SKILLS
        skills_found = extract_skills(description)
        
        extracted_data.append((title, company, skills_found))
        
        # Be polite to the server
        time.sleep(0.5) 
        print(f"     -> Scraped: {title} [{skills_found}]")

    # 4. SAVE TO DB
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS job_skills 
                      (title TEXT, company TEXT, skills TEXT)''')
    cursor.execute('DELETE FROM job_skills') # Clean slate
    cursor.executemany('INSERT INTO job_skills VALUES (?,?,?)', extracted_data)
    conn.commit()
    
    # 5. ANALYSIS
    print("\n📊 SKILL DEMAND ANALYSIS (Top Skills Found)")
    df = pd.read_sql("SELECT * FROM job_skills", conn)
    
    # Split the 'skills' string into individual rows to count them
    # e.g. "python, sql" becomes two rows
    skills_series = df['skills'].str.split(', ', expand=True).stack()
    
    # Count and print
    print(skills_series.value_counts())
    
    conn.close()

if __name__ == "__main__":
    run_advanced_pipeline()