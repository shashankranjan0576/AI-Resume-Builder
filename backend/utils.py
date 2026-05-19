from docx import Document


def create_resume_docx(content, filename):

    doc = Document()

    doc.add_heading(
        "ATS Optimized Resume",
        level=1
    )

    doc.add_paragraph(content)

    doc.save(filename)


from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_resume_pdf(content, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "ATS Optimized Resume",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 12))

    paragraphs = content.split("\n")

    for para in paragraphs:

        if para.strip():

            p = Paragraph(
                para,
                styles['BodyText']
            )

            elements.append(p)

            elements.append(Spacer(1, 8))

    doc.build(elements)

def clean_ai_output(text):

    unwanted_phrases = [

        "Here is an ATS-optimized resume",
        "Here is a professional cover letter",
        "Here’s a professional cover letter",
        "Here is a rewritten version",
        "Note:",
        "I've kept the formatting",
        "I have kept the formatting",
        "Let me know if you need any further assistance",
        "tailored to the",
        "ATS Optimized Resume"
    ]

    cleaned_lines = []

    lines = text.split("\n")

    for line in lines:

        should_skip = False

        for phrase in unwanted_phrases:

            if phrase.lower() in line.lower():

                should_skip = True
                break

        if not should_skip:

            cleaned_lines.append(line)

    cleaned_text = "\n".join(cleaned_lines)

    return cleaned_text.strip()