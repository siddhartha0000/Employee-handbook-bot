from endee import Endee
from sentence_transformers import SentenceTransformer
import uuid
from text_chunker import extract_text_from_pdfs, chunk_text

client = Endee()
index = client.get_index(name="employee_policies")

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = extract_text_from_pdfs()
vectors = []

for doc in documents:
    chunks = chunk_text(doc["text"])

    for chunk in chunks:
        embedding = model.encode(chunk).tolist()

        vectors.append({
            "id": str(uuid.uuid4()),
            "vector": embedding,
            "meta": {
                "source": doc["source"],   # ✅ PDF name
                "text": chunk              # ✅ ACTUAL CONTENT
            }
        })

index.upsert(vectors)
print(f"Upserted {len(vectors)} vectors into Endee")
