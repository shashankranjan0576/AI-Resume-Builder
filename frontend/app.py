import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import streamlit as st

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

from backend.resume_parser import (
    extract_text_from_pdf,
    clean_text
)

from backend.ats_engine import (
    extract_skills,
    calculate_ats_score,
    find_missing_skills
)

from backend.prompt_engine import (
    generate_professional_summary,
    rewrite_resume_bullet,
    generate_full_resume,
    generate_cover_letter
)

from backend.utils import create_resume_docx

# Page config
st.set_page_config(
    page_title="AI Resume Optimizer",
    layout="wide"
)

st.title("AI-Powered ATS Resume Optimizer")

st.sidebar.title("AI Resume Optimizer")

st.sidebar.info(
    """
    Upload your resume and compare it
    against a job description using AI.

    Features:
    - ATS Score
    - Missing Skills
    - Resume Optimization
    - Cover Letter Generation
    """
)

st.write(
    "Upload your resume and compare it with a job description."
)

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

# Job Description Input
job_description = st.text_area(
    "Paste Job Description",
    height=200
)

target_role = st.text_input(
    "Target Role",
    placeholder="Example: AI Engineer"
)

# Analyze Button
if st.button("Analyze Resume"):

    st.session_state.analysis_done = True


if st.session_state.analysis_done:

    if uploaded_file and job_description:

        # Save uploaded PDF
        save_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Extract Resume Text
        resume_text = extract_text_from_pdf(save_path)

        resume_text = clean_text(resume_text)

        # Extract Skills
        resume_skills = extract_skills(resume_text)

        jd_skills = extract_skills(job_description)

        # ATS Score
        ats_score = calculate_ats_score(
            resume_text,
            job_description
        )

        # Missing Skills
        missing_skills = find_missing_skills(
            resume_skills,
            jd_skills
        )

        # Generate Professional Summary
        summary = generate_professional_summary(
            resume_text,
            target_role
        )

        # Display Results
        col1, col2 = st.columns(2)

        with col1:

            st.subheader("ATS Match Score")

            st.metric(
                label="ATS Score",
                value=f"{ats_score:.2f}%"
            )

            st.subheader("Missing Skills")

            st.write(missing_skills)

        with col2:

            st.subheader("Extracted Resume Skills")

            st.write(resume_skills)

        st.divider()

        st.subheader("AI Professional Summary")

        st.write(summary)

        # Generate Full Resume
        optimized_resume = generate_full_resume(
            resume_text,
            job_description,
            target_role
        )

        st.divider()

        st.subheader("Full ATS-Optimized Resume")

        st.write(optimized_resume)

        # Create DOCX Resume
        resume_docx_path = "outputs/optimized_resume.docx"

        create_resume_docx(
            optimized_resume,
            resume_docx_path
        )

        with open(resume_docx_path, "rb") as file:

            st.download_button(
                label="Download Optimized Resume (DOCX)",
                data=file,
                file_name="optimized_resume.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

        # Generate Cover Letter
        cover_letter = generate_cover_letter(
            resume_text,
            job_description,
            target_role
        )

        st.divider()

        st.subheader("AI Generated Cover Letter")

        st.write(cover_letter)


        # Create DOCX Cover Letter
        cover_docx_path = "outputs/cover_letter.docx"

        create_resume_docx(
            cover_letter,
            cover_docx_path
        )

        with open(cover_docx_path, "rb") as file:

            st.download_button(
                label="Download Cover Letter (DOCX)",
                data=file,
                file_name="cover_letter.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

        st.divider()

        # Resume Bullet Optimizer
        st.subheader("AI Resume Bullet Optimizer")

        user_bullet = st.text_area(
            "Paste Resume Bullet Point",
            height=100
        )

        if st.button("Optimize Bullet Point"):

            if user_bullet:

                optimized_bullet = rewrite_resume_bullet(
                    user_bullet
                )

                st.success("Optimized Bullet Point")

                st.write(optimized_bullet)

    else:

        st.warning(
            "Please upload resume and paste job description."
        )