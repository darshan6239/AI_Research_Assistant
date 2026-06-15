from pypdf import PdfReader
import io

def extract_text_from_pdf(pdf_bytes):
    try:
        pdf_reader = PdfReader(io.BytesIO(pdf_bytes))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n\n"
        return text.strip()
    except Exception as e:
        raise ValueError(f"Error reading PDF: {str(e)}")