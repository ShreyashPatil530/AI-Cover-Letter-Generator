import streamlit as st
from resume_parser import extract_resume
from cover_letter_generator import generate_cover_letter
from ats_analyzer import ats_keyword_analysis
from pathlib import Path

# Streamlit page setup
st.set_page_config(page_title="AI Cover Letter Generator", layout="centered")
st.title("AI Cover Letter Generator")

# Resume Upload with unique key
uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF or DOCX)", 
    type=["pdf", "docx"], 
    key="resume_uploader"  # ✅ unique key to fix DuplicateElementId
)

# Job Description Input
job_desc = st.text_area("Paste Job Description Here", key="job_desc_input")

# Tone selection
tone = st.selectbox(
    "Select Cover Letter Tone", 
    ["Professional", "Friendly", "Formal"],
    key="tone_selection"
)

# Generate Button
if st.button("Generate Cover Letter", key="generate_btn"):
    if uploaded_file is None or job_desc.strip() == "":
        st.warning("Please upload resume and paste job description.")
    else:
        with st.spinner("Extracting resume and generating cover letter..."):
            # Extract resume text
            resume_text = extract_resume(uploaded_file)
            
            # Generate cover letter via Groq
            cover_letter = generate_cover_letter(resume_text, job_desc, tone)
            
            # Display cover letter
            st.subheader("Generated Cover Letter")
            st.write(cover_letter)
            
            # ATS keyword analysis (optional)
            score, matched = ats_keyword_analysis(cover_letter, job_desc)
            st.write(f"**ATS Keyword Match Score:** {score:.2f}%")
            st.write(f"**Matched Keywords:** {', '.join(matched)}")
            
            # Download option
            output_dir = Path("downloads/generated_letters")
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / f"{uploaded_file.name.split('.')[0]}_cover_letter.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(cover_letter)
            st.download_button(
                "Download Cover Letter", 
                data=cover_letter, 
                file_name="cover_letter.txt"
            )
