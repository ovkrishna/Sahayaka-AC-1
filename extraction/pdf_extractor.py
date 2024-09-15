import fitz  # PyMuPDF

# Function to extract text from a given PDF file
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()  # Extract text from each page
    return text
