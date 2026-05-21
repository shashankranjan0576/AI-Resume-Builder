from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

import streamlit as st
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:

    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

client = Groq(
    api_key=GROQ_API_KEY
)


def rewrite_resume_bullet(bullet_point):

    prompt = f"""
    Rewrite the following resume bullet point
    into a concise, ATS-optimized,
    achievement-oriented bullet point.

    Requirements:
    - Output ONLY the rewritten bullet point
    - No explanations
    - No extra text
    - Use strong action verbs
    - Keep it professional
    - Improve clarity and impact
    - Do not invent fake metrics
    - Keep it 1–2 lines maximum

    Resume Bullet:
    {bullet_point}
    """

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": "You are an expert ATS resume optimizer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7
    )

    return response.choices[0].message.content


def generate_professional_summary(candidate_info, target_role):

    prompt = f"""
    Create a professional ATS-optimized resume summary.

    Requirements:
    - Output ONLY the summary
    - Keep it professional and concise
    - Maximum 4 lines
    - Focus on recruiter readability
    - Highlight strongest technical skills
    - Align with the target role
    - Do not invent fake experience

    Candidate Information:
    {candidate_info}

    Target Role:
    {target_role}
    """

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": "You are an expert ATS resume writer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.5
    )

    return response.choices[0].message.content


def generate_full_resume(resume_text, job_description, target_role):

    prompt = f"""
    Generate an ATS-optimized resume.

    Requirements:
    - Keep it professional
    - ATS-friendly formatting
    - Use concise bullet points
    - Improve recruiter readability
    - Optimize for the target role
    - Use strong action verbs
    - Do NOT invent fake experience
    - Do NOT invent fake companies
    - Do NOT invent fake metrics
    - Naturally integrate relevant keywords
    - Keep formatting clean

    Resume Information:
    {resume_text}

    Job Description:
    {job_description}

    Target Role:
    {target_role}

    Output Format:

    PROFESSIONAL SUMMARY

    SKILLS

    EXPERIENCE

    PROJECTS

    EDUCATION
    """

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": "You are an expert ATS resume writer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.5
    )

    return response.choices[0].message.content

def generate_cover_letter(
    resume_text,
    job_description,
    target_role
):

    prompt = f"""
    Generate a professional cover letter.

    Requirements:
    - Keep it professional
    - ATS-friendly language
    - Concise and recruiter-focused
    - Highlight relevant skills
    - Align with the target role
    - Do NOT invent fake experience
    - Keep it under 300 words

    Resume Information:
    {resume_text}

    Job Description:
    {job_description}

    Target Role:
    {target_role}
    """

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": "You are an expert resume and cover letter writer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.5
    )

    return response.choices[0].message.content


def generate_ats_suggestions(
    resume_text,
    job_description,
    missing_skills
):

    prompt = f"""
    Analyze the resume against the job description
    and provide ATS improvement suggestions.

    Requirements:
    - Keep suggestions concise
    - Use bullet points
    - Focus on ATS optimization
    - Focus on recruiter readability
    - Suggest missing keywords naturally
    - Do NOT invent fake experience
    - Maximum 6 suggestions

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Missing Skills:
    {missing_skills}
    """

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": "You are an ATS optimization expert."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.4
    )

    return response.choices[0].message.content




if __name__ == "__main__":

    candidate_info = """
    Computer Engineering student with experience
    in Python, FastAPI, AI systems, LangChain,
    Machine Learning, React, and backend development.
    Built AI-powered resume optimization systems
    and multi-agent applications.
    """

    target_role = "AI Engineer"

    summary = generate_professional_summary(
        candidate_info,
        target_role
    )

    print("\nProfessional Summary:\n")

    print(summary)