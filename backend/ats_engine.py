import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")


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


if __name__ == "__main__":

    from resume_parser import extract_text_from_pdf, clean_text

    resume_text = extract_text_from_pdf("uploads/sample_resume.pdf")

    sample_text = clean_text(resume_text)

    skills = extract_skills(sample_text)

    print("Extracted Skills:")
    print(skills)