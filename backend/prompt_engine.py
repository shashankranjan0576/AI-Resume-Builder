from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
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