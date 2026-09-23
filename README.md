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
- [x] Document-ingestion pipeline
  - [x] Added three sample technical-support documents
  - [x] Loaded and cleaned text documents
  - [x] Divided documents into 100-word chunks
  - [x] Attached source metadata and unique IDs to every chunk
  - [x] Generate embeddings for each chunk
  - [x] Store embeddings in a local vector database
  - [x] Prevent duplicate document ingestion
  - [x] Documented how to add new source documents
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

## Document Ingestion

Run the document-ingestion pipeline:

```powershell
python -m app.ingest
```

The pipeline loads `.txt` files from the `data/` directory, cleans their text, divides them into 100-word chunks, generates embeddings, and stores the results in the local Chroma vector database.

Expected summary output:

```text
Chunks stored in Chroma: 11
First embedding dimensions: 384
Documents processed: 3
Total chunks created: 11
```

## Adding New Source Documents

1. Create a plain-text file with the `.txt` extension.
2. Use a descriptive filename, such as `printer_troubleshooting.txt`.
3. Put the document’s readable title on the first line.
4. Add the technical-support content below the title.
5. Save the file inside the `data/` directory.
6. Run the ingestion pipeline again:

```powershell
python -m app.ingest
```

Example source document:

```text
Printer Connection Troubleshooting

Purpose
Use this procedure when a user cannot connect to a network printer.

Troubleshooting Steps
Confirm that the computer is connected to the organization’s network.
Verify the printer name and network address.
Remove and reconnect the printer if necessary.
```

The filename without `.txt` becomes the document ID. For example:

```text
printer_troubleshooting.txt → printer_troubleshooting
```

Each generated chunk receives a stable ID such as:

```text
printer_troubleshooting_chunk_1
```

The pipeline uses those stable chunk IDs with Chroma’s `upsert()` operation. Running ingestion again updates matching records instead of creating uncontrolled duplicates.

## Development Roadmap

- **Week 1:** Core RAG pipeline
- **Week 2:** Tracing and regression evaluation
- **Week 3:** Permission-controlled automation and portfolio polish
