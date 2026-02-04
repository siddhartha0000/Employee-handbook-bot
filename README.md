# Employee Handbook RAG Assistant

## 📚 Table of Contents
- Problem Statement
- Overview
- High-Level Architecture
- Tech Stack Used
- Key Features
- Installation & Setup
- Usage
- Project Structure
- Challenges Faced
- Contact

---

## Problem Statement

In many organizations, employees depend on HR teams or internal portals to find information related to company policies such as leave rules, working hours, code of conduct, and benefits.  
These documents are usually long, unstructured, and difficult to search using normal keyword-based systems.

Because of this, employees often waste time searching for answers or repeatedly asking HR the same questions.

To solve this problem, I built an **Employee Handbook Assistant** using a **Retrieval Augmented Generation (RAG)** approach.  
The system allows employees to ask questions in natural language and retrieves accurate, context-aware answers from company policy documents using **Endee as the vector database**.

---

## Overview
Employees often struggle to quickly find answers from long employee handbook PDFs.
This project solves that problem by enabling **natural language questions** over employee policy documents using **semantic search and RAG (Retrieval-Augmented Generation)**.

---
## High-Level Architecture of Employee Handbook Bot

### 1️⃣ Data Source (Employee Documents)

**Input:**
- Employee handbook
- HR policies (leave, working hours, code of conduct)

**Format:**
- PDF files (text extracted from PDFs)

These documents act as the **knowledge base** of the system.

---

### 2️⃣ Embedding Generation

- Each document is split into small overlapping text chunks
- Each chunk is passed to an embedding model
- Output is a vector (list of numbers) representing the meaning of the text

This step converts **text meaning into numerical form**.

---

### 3️⃣ Vector Storage (Endee)

- All generated vectors are stored in **Endee**
- Along with:
  - original text chunk
  - metadata (document name)

Endee acts as the **memory layer** of the system.

---

### 4️⃣ User Query Input

- The user types a question like:
  *“What is the leave policy?”*
- The question is also converted into an embedding vector

The same embedding process is used for documents and queries.

---

### 5️⃣ Vector Search (Core Step)

- The query vector is sent to Endee
- Endee performs **similarity search**
- Top relevant policy chunks are returned

This is the **core vector database step**.

---

### 6️⃣ Context Augmentation

- Retrieved text chunks are combined with the user question
- This combined context is passed to the LLM

This step helps prevent hallucination.

---

### 7️⃣ Answer Generation (LLM)

- The LLM receives:
  - user question
  - retrieved policy text
- Generates an answer grounded strictly in company policies

---

### 8️⃣ Final Response to User

- User receives a clear and accurate policy-based answer
- Answer is based only on the retrieved documents
- Optional: source document can be shown

---

## One-Line Architecture Summary 

**Documents → Embeddings → Endee (vector storage) → Similarity search → Context → Answer generation**

---

## 🧰 Tech Stack
- **Vector Database:** Endee
- **Programming Language:** Python
- **Embeddings:** Sentence Transformers (all-MiniLM-L6-v2)
- **LLM:** Gemini 2.5 Flash (free tier)
- **PDF Processing:** pypdf
- **Environment:** Python Virtual Environment (venv)
- **Containerization:** Docker

---

## ✨ Key Features
- Semantic search over employee handbook PDFs
- Uses **Endee** as the primary vector database
- Retrieval-Augmented Generation (RAG) pipeline
- Supports large PDFs (100+ pages)
- Answers are grounded strictly in document content
- Modular and beginner-friendly code structure

---

## ⚙️ Installation & Setup

### 1️⃣ Clone or Download the Project
(If Git is not used, simply download the folder)

---
Employee-handbook-bot/
### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv

#windows:
venv\Scripts\activate

#3️⃣ Install Dependencies
pip install -r requirements.txt 

#4️⃣ Start Endee Vector Database (Docker)
#Make sure use are running this in command prompt and ensure Docker Desktop is running.
docker run -d ^
  -p 8080:8080 ^
  -v endee-data:/data ^
  --name endee-server ^
  endeeio/endee-server:latest

#Check:
http://localhost:8080

#5️⃣ Create Vector Index
python create_index.py

#6️⃣ Ingest PDFs into Endee
python endee_upsert.py

#This step:Reads PDFs,Chunks text,Generates embeddings,Stores vectors in Endee
#▶️ Usage : Ask Questions (RAG Pipeline)
python rag_with_llm.py

#Example questions:How many sick leaves are allowed?,what is the dress code? what are the working hours?
#Expected outputs:Employees are entitled to 20 PTO per year according to the leave policy.,Our company’s official dress code is [ Business/ Business Casual/ Smart Casual/ Casual. ],The standard working hours are from 9:30 AM to 6:30 PM, Monday to Friday. Employees are expected to work for 8 hours per day excluding breaks.
```

### 📁 Project Structure
Employee-handbook-bot/
│
├── data/
│   └── pdf/
│       ├── leave_policy.pdf
│       ├── working_hours.pdf
│       └── code_of_conduct.pdf
│
├── text_chunker.py
├── create_index.py
├── endee_upsert.py
├── rag_with_llm.py
├── venv/
└── README.md


## Challenges Faced

- Handling large PDF files  
  → Solved using text chunking with overlap

- Incorrect or vague answers initially  
  → Fixed by passing retrieved text (not filenames) to the LLM

- Vector storage issues  
  → Solved by properly storing metadata and text inside Endee

## Contact

**Name:** Siddhartha Pamarthi  
**LinkedIn profile link:**  (https://www.linkedin.com/in/siddhartha-pamarthi-39021825a/)

