from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Load transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')


# Predefined technical skills database
SKILLS_DB = [

    # Programming Languages
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",
    "sql",

    # Web Development
    "html",
    "css",
    "react",
    "node.js",
    "fastapi",
    "flask",
    "django",
    "rest api",
    "api",

    # AI / ML
    "machine learning",
    "deep learning",
    "nlp",
    "rag",
    "langchain",
    "langgraph",
    "prompt engineering",
    "sentence transformers",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "pandas",
    "numpy",

    # Databases
    "mysql",
    "mongodb",
    "sqlite",
    "chromadb",

    # Tools
    "git",
    "github",
    "docker",
    "streamlit",
    "postman",
    "linux",
    "bash",
    "vscode",

    # Concepts
    "oop",
    "oops",
    "dbms",
    "operating systems",
    "computer networks",
    "data structures",
    "algorithms"
]


def extract_skills(text):

    text = text.lower()

    found_skills = set()

    for skill in SKILLS_DB:

        if skill.lower() in text:
            found_skills.add(skill)

    return sorted(found_skills)


def calculate_ats_score(resume_text, job_description):
    """
    Calculate semantic ATS match score
    """

    # Convert text into embeddings
    resume_embedding = model.encode([resume_text])

    jd_embedding = model.encode([job_description])

    # Calculate cosine similarity
    similarity = cosine_similarity(
        resume_embedding,
        jd_embedding
    )[0][0]

    # Convert to percentage
    ats_score = round(similarity * 100, 2)

    return ats_score


def find_missing_skills(resume_skills, jd_skills):
    """
    Find skills missing from resume
    """

    missing = []

    for skill in jd_skills:

        if skill not in resume_skills:
            missing.append(skill)

    return missing


if __name__ == "__main__":

    from resume_parser import extract_text_from_pdf, clean_text

    # Extract resume text
    resume_text = extract_text_from_pdf(
        "uploads/sample_resume.pdf"
    )

    resume_text = clean_text(resume_text)

    # Extract skills
    skills = extract_skills(resume_text)

    print("\nExtracted Skills:")
    print(skills)

    # Sample Job Description
    job_description = """
    We are looking for a Python Developer
    with experience in FastAPI, SQL,
    Machine Learning, APIs, and React.
    Experience with NLP and AI systems
    is a plus.
    """

    # Extract JD skills
    jd_skills = extract_skills(job_description)

    print("\nJob Description Skills:")
    print(jd_skills)

    # Calculate ATS score
    ats_score = calculate_ats_score(
        resume_text,
        job_description
    )

    print("\nATS Match Score:")
    print(f"{ats_score:.2f}%")

    # Find missing skills
    missing_skills = find_missing_skills(
       skills,
        jd_skills
    )

    print("\nMissing Skills:")
    print(missing_skills)