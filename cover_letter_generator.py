import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def generate_cover_letter(resume_text, job_description, tone="Professional"):
    prompt = f"""
You are an expert HR assistant.
Generate a {tone} cover letter using the following resume and job description.

Resume:
{resume_text}

Job Description:
{job_description}

Cover Letter:
"""
    response = client.chat.completions.create(
        messages=[{"role":"user","content": prompt}],
        model="llama-3.3-70b-versatile",
        max_tokens=500  # ✅ use max_tokens, not max_output_tokens
    )
    return response.choices[0].message.content
