# 🧠 AI Debugging Assistant (Vector Search System)

## 🚀 Overview
This project is an AI-powered debugging assistant that helps developers identify and resolve programming errors using semantic search.

Unlike traditional keyword-based search, this system uses vector embeddings to understand the meaning of error messages and return the most relevant solutions.

---

## 💡 Problem Statement
Developers often struggle to find solutions for errors due to differences in wording. This system solves that problem using semantic similarity instead of exact matching.

---

## 🧠 Features
- Semantic search using embeddings
- Fast similarity search using FAISS (vector database)
- Interactive UI using Streamlit
- Duplicate result filtering
- Fallback handling for unmatched queries

---

## 🏗️ Architecture
User Input
↓
Embedding Model (Sentence Transformers)
↓
Vector Database (FAISS)
↓
Similarity Search
↓
Top Matching Errors + Solutions

---

## ⚙️ Tech Stack
- Python
- Sentence Transformers
- FAISS (Vector Database)
- Streamlit

---

## 🔗 Endee Integration Note
This project demonstrates vector-based retrieval and can be extended to use Endee Vector Database for scalable production deployment.

---

## 📂 Project Structure
ai-debugging-assistant/
│
├── data/errors.json
├── embedder.py
├── database.py
├── main.py
├── ui.py
├── requirements.txt

---

## ▶️ Setup Instructions

```bash
git clone https://github.com/MuditBh/ai-debugging-assistant
cd ai-debugging-assistant
pip install -r requirements.txt
streamlit run ui.py
