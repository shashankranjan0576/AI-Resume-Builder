# AI Resume Optimizer

An AI-powered ATS Resume Optimization Web App built using Python, Streamlit, NLP, and Large Language Models.

## Features

- ATS Match Score Analysis
- Resume Skill Extraction
- Missing Skill Detection
- AI Professional Summary Generation
- Full ATS-Optimized Resume Generation
- AI Cover Letter Generation
- Resume Bullet Point Optimization
- DOCX Resume & Cover Letter Downloads

## Tech Stack

- Python
- Streamlit
- Sentence Transformers
- Groq API (LLaMA 3.3 70B)
- NLP
- python-docx

## Project Structure

```text
backend/
    ats_engine.py
    prompt_engine.py
    resume_parser.py
    utils.py

frontend/
    app.py
```

## Installation

```bash
git clone <your-repo-link>

cd AI_Resume_Builder

pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run frontend/app.py
```

## Future Improvements

- PDF Export
- Multiple Resume Templates
- Better ATS Semantic Matching
- Multi-language Support
- Recruiter Analytics Dashboard
- Cloud Deployment

## Author

Shashank Ranjan