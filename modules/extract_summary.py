import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Folder containing your PDFs
folder_path = "data/raw_docs"

# Loop through all PDF files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".pdf"):
        file_path = os.path.join(folder_path, filename)
        print(f"\n--- Extracting from: {filename} ---")
        print(extract_text_from_pdf(file_path))
