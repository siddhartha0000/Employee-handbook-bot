from endee import Endee
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set")

genai.configure(api_key=GEMINI_API_KEY)
MODEL_NAME = "models/gemini-2.5-flash"


client = Endee()
index = client.get_index(name="employee_policies")

embedder = SentenceTransformer("all-MiniLM-L6-v2")


llm = genai.GenerativeModel(MODEL_NAME)

def ask_question(question: str):
   
    query_vector = embedder.encode(question).tolist()

    results = index.query(
        vector=query_vector,
        top_k=3
    )

    context = "\n\n".join(
        [f"Source: {r['meta']['source']}\n{r['meta']['text']}" for r in results]
    )

    prompt = f"""
You are an HR assistant.
Answer ONLY using the policy text below.

Policy Text:
{context}

Question:
{question}
"""

    response = llm.generate_content(prompt)

    print("\n--- Final Answer ---")
    print(response.text)

if __name__ == "__main__":
    q = input("Ask a question: ")
    ask_question(q)
