from pypdf import PdfReader
import os

PDF_FOLDER = "data/pdf"

def read_pdfs():
    all_text = []

    for file_name in os.listdir(PDF_FOLDER):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(PDF_FOLDER, file_name)
            reader = PdfReader(file_path)

            print(f"\n--- Reading {file_name} ---")

            for page in reader.pages:
                text = page.extract_text()
                if text:
                    all_text.append(text)
                    print(text)

    return all_text


if __name__ == "__main__":
    read_pdfs()
