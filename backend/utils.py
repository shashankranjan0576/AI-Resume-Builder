from docx import Document


def create_resume_docx(content, filename):

    doc = Document()

    doc.add_heading(
        "ATS Optimized Resume",
        level=1
    )

    doc.add_paragraph(content)

    doc.save(filename)