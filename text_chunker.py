from pypdf import PdfReader
import os

PDF_FOLDER = "data/pdf"

def extract_text_from_pdfs():
    documents = []

    for file_name in os.listdir(PDF_FOLDER):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(PDF_FOLDER, file_name)
            reader = PdfReader(file_path)

            full_text = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"

            documents.append({
                "source": file_name,
                "text": full_text
            })

    return documents


def chunk_text(text, chunk_size=300, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap

    return chunks


if __name__ == "__main__":
    docs = extract_text_from_pdfs()

    for doc in docs:
        print(f"\n=== Chunks from {doc['source']} ===")
        chunks = chunk_text(doc["text"])

        for i, c in enumerate(chunks):
            print(f"\nChunk {i+1}:\n{c}")
