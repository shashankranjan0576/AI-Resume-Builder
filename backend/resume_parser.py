import pdfplumber
import re


def extract_text_from_pdf(pdf_path):
    """
    Extract text from PDF resume
    """

    text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:
                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

        return text

    except Exception as e:
        return f"Error extracting PDF: {str(e)}"


def clean_text(text):
    """
    Clean extracted resume text
    """

    # Remove extra spaces/newlines
    text = re.sub(r'\s+', ' ', text)

    # Fix merged words around punctuation
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

    return text.strip()


if __name__ == "__main__":

    sample_pdf = "uploads/sample_resume.pdf"

    extracted_text = extract_text_from_pdf(sample_pdf)

    cleaned_text = clean_text(extracted_text)

    print(cleaned_text)