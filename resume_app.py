import io
import streamlit as st
import pandas as pd
import pdfplumber
from docx import Document
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- UI CONFIG ---
st.set_page_config(page_title="AI Resume Ranking Tool", layout="wide", page_icon="📄")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .stProgress > div > div > div > div {
        background-color: #28a745;
    }
    .skill-tag {
        background-color: #e1f5fe;
        color: #01579b;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8em;
        margin-right: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 AI-Powered Resume Ranking Tool")
st.markdown("---")
st.write("Upload candidate resumes and paste the job description to find the best match with keyword extraction.")

def clean_text(text):
    """Normalize text by removing special characters and extra whitespace."""
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # remove extra whitespace
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text) # remove special characters
    return text.strip()

def extract_skills(text, skill_list):
    """Check for presence of specific skills in the text."""
    found_skills = []
    for skill in skill_list:
        skill = skill.strip()
        if not skill: continue
        # Use regex to find whole word matches only
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text.lower()):
            found_skills.append(skill)
    return found_skills

def extract_text(uploaded_file):
    """Extract text from PDF, DOCX, or TXT formats."""
    try:
        if uploaded_file.type == "application/pdf":
            with pdfplumber.open(uploaded_file) as pdf:
                text = "\n".join(page.extract_text() or "" for page in pdf.pages)
            return text
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(uploaded_file)
            return "\n".join([para.text for para in doc.paragraphs])
        elif uploaded_file.type == "text/plain":
            return str(uploaded_file.read(), "utf-8")
        else:
            return ""
    except Exception as e:
        st.error(f"Error parsing {uploaded_file.name}: {e}")
        return ""

def main():
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("📁 Input Data")
        job_description = st.text_area("Job Description", height=200, placeholder="Paste the job requirements here...")
        
        st.markdown("---")
        st.write("**Specific Skills / Keywords to extract:**")
        skills_input = st.text_input("Enter skills separated by commas", placeholder="e.g. Python, SQL, React, Machine Learning")
        skill_list = [s.strip() for s in skills_input.split(",")] if skills_input else []
        
        uploaded_files = st.file_uploader("Candidate Resumes", type=["pdf","docx","txt"], accept_multiple_files=True)

    with col2:
        st.subheader("📊 Ranking Results")
        if uploaded_files and job_description:
            resumes_text = []
            filenames = []
            extracted_skills_per_resume = []
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i, uploaded_file in enumerate(uploaded_files):
                status_text.text(f"Processing {uploaded_file.name}...")
                text = extract_text(uploaded_file)
                if text.strip(): # Only include non-empty resumes
                    cleaned = clean_text(text)
                    resumes_text.append(cleaned)
                    filenames.append(uploaded_file.name)
                    
                    if skill_list:
                        found = extract_skills(text, skill_list)
                        extracted_skills_per_resume.append(", ".join(found))
                    else:
                        extracted_skills_per_resume.append("N/A")
                        
                progress_bar.progress((i + 1) / len(uploaded_files))
            
            status_text.text("Calculating scores...")
            
            if resumes_text:
                # Preprocess job description
                clean_job_desc = clean_text(job_description)
                
                # Vectorize and Similarity Calculation
                vectorizer = TfidfVectorizer(stop_words="english")
                all_docs = [clean_job_desc] + resumes_text
                vectors = vectorizer.fit_transform(all_docs)
                
                # Job description vector is at index 0, resumes are from 1 onwards
                job_vector = vectors[0]
                resume_vectors = vectors[1:]
                
                similarity_scores = cosine_similarity(job_vector, resume_vectors).flatten() * 100
                
                # Prepare and display results
                df = pd.DataFrame({
                    "Rank": range(1, len(filenames) + 1),
                    "Candidate Name": filenames,
                    "Match Score (%)": similarity_scores.round(2),
                    "Skills Detected": extracted_skills_per_resume
                })
                df = df.sort_values(by="Match Score (%)", ascending=False)
                df["Rank"] = range(1, len(df) + 1) # Revise rank after sorting

                # Highlight the best match
                st.success(f"Best Overall Match: **{df.iloc[0]['Candidate Name']}** with a score of **{df.iloc[0]['Match Score (%)']}%**")
                
                st.dataframe(df.style.background_gradient(subset=["Match Score (%)"], cmap="Greens"), use_container_width=True)

                # Download section
                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button("📥 Download Rankings CSV", data=csv, file_name="resume_rankings.csv", mime="text/csv")
            else:
                st.warning("No valid text could be extracted from the uploaded resumes.")
            
            progress_bar.empty()
            status_text.empty()
        else:
            st.info("Plese upload resumes and provide a job description to see rankings.")

if __name__ == "__main__":
    main()
