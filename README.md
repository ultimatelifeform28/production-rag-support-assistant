# Production RAG Support Assistant

A production-focused Retrieval-Augmented Generation application that searches technical-support documentation and generates grounded answers with source citations.

## Project Goal

This project demonstrates how to build a reliable RAG application with:

- Document ingestion and text chunking
- Semantic document retrieval
- Grounded answer generation
- Source citations
- Evaluation and regression testing
- Observability and tracing
- Permission-controlled automation tools

## Current Status

### Week 1: Core RAG Pipeline

- [x] Repository initialized
- [x] Python 3.12 development environment created
- [x] Initial project structure created
- [x] Starter application tested
- [ ] Document-ingestion pipeline
  - [x] Added three sample technical-support documents
  - [x] Loaded and cleaned text documents
  - [x] Divided documents into 100-word chunks
  - [x] Attached source metadata and unique IDs to every chunk
  - [ ] Generate embeddings for each chunk
  - [ ] Store embeddings in a local vector database
  - [ ] Prevent duplicate document ingestion
- [ ] Semantic retrieval
- [ ] Grounded answer generation
- [ ] Source citations
- [ ] Week 1 demonstration

## Project Structure

```text
production-rag-support-assistant/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── ingest.py
│   ├── retrieve.py
│   └── generate.py
├── data/
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.12
- Git
- Visual Studio Code

## Setup

Clone the repository:

```powershell
git clone https://github.com/ultimatelifeform28/production-rag-support-assistant.git
cd production-rag-support-assistant
```

Create the Python 3.12 virtual environment:

```powershell
py -3.12 -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run the starter application:

```powershell
python -m app.main
```

## Expected Starter Output

```text
Production RAG Support Assistant is running...
Environment setup successful. Ready to assist with RAG support tasks.
```

## Development Roadmap

- **Week 1:** Core RAG pipeline
- **Week 2:** Tracing and regression evaluation
- **Week 3:** Permission-controlled automation and portfolio polish
