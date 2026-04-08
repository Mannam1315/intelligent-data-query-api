# Intelligent Data Query API

This project demonstrates a practical AI-enabled backend system that allows users to query structured datasets using natural language. It combines FastAPI, data preprocessing, embeddings, FAISS, and MLflow to build a lightweight RAG-based data query service.

## 🚀 Project Overview

The application is designed to help users explore structured data without writing SQL manually. Instead of querying datasets directly, users can ask plain-English questions and retrieve contextually relevant results.

## 🔧 Core Capabilities

* preprocesses structured CSV data
* converts rows into searchable vector documents
* stores embeddings in FAISS
* exposes REST APIs using FastAPI
* supports experiment tracking through MLflow
* packaged for deployment using Docker

## 📂 Project Structure

* `api/` → FastAPI endpoints
* `pipeline/` → preprocessing and embedding logic
* `rag/` → retrieval flow
* `ml/` → MLflow utilities
* `data/` → sample structured dataset

## ⚙️ Tech Stack

* Python
* FastAPI
* Pandas
* LangChain
* FAISS
* MLflow
* Docker

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
```

Then open:

```bash
http://127.0.0.1:8000/query?q=Which product had highest sales in February?
```

## 📌 Future Enhancements

* integrate LLM summarization on top of retrieval
* connect to real SQL or NoSQL sources
* add CI/CD pipeline
* deploy on AWS
* add authentication and usage logging

## 💡 Why I Built This

I wanted to build a project that combines backend engineering, data processing, and practical generative AI patterns in a way that feels close to a real production use case rather than a generic chatbot demo.
