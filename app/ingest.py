from pathlib import Path
import chromadb

CURRENT_FILE = Path(__file__).resolve()
APP_DIRECTORY = CURRENT_FILE.parent
PROJECT_ROOT = APP_DIRECTORY.parent
DATA_DIRECTORY = PROJECT_ROOT / "data"
CHROMA_DIRECTORY = PROJECT_ROOT / "chroma_db"

chroma_client = chromadb.PersistentClient(path=str(CHROMA_DIRECTORY))

chunk_collection = chroma_client.get_or_create_collection("document_chunks")

def clean_text(text):
    lines = text.splitlines()
    cleaned_lines = []

    # Check each line from the original doucment
    for line in lines:
        cleaned_line = line.strip() # Remove leading and trailing spaces
       # Keep the line only if it is not empty after cleaning 
        if cleaned_line:
           cleaned_lines.append(cleaned_line)

    return "\n".join(cleaned_lines)


def chunk_text(text, chunk_size=100):
    words = text.split()
    chunks = []

    for start_index in range(0, len(words), chunk_size):
        end_index = min(start_index + chunk_size, len(words))
        chunk = " ".join(words[start_index:end_index])
        chunks.append(chunk)

    return chunks

def load_documents():
    documents = []  # Create the documents list 

    for file_path in DATA_DIRECTORY.glob("*.txt"):
        raw_text = file_path.read_text(encoding="utf-8")
        document_text = clean_text(raw_text)
        document_chunks = chunk_text(document_text)
        document_id = file_path.stem 
        document_title = document_text.splitlines()[0]

        chunk_records = []

        for chunk_number, chunk_content in enumerate(document_chunks, start=1):
            chunk_id = f"{document_id}_chunk_{chunk_number}"

            chunk_record = {
                "document_id": document_id,
                "document_title": document_title,
                "source_filename": file_path.name,
                "chunk_id": chunk_id,
                'chunk_text': chunk_content
            }

            chunk_records.append(chunk_record)

        document =  {
                "document_id": document_id,
                "document_title": document_title,
                "source_filename": file_path.name,
                "text": document_text, 
                "chunks": chunk_records
        }

        documents.append(document)

        print(file_path.name)
        print(f"Chunks created: {len(chunk_records)}")

    return documents

def store_chunks_in_chroma(documents):
    chunk_ids = []
    chunk_texts = []
    chunk_metadatas = []

    for document in documents:
        for chunk in document['chunks']:

            chunk_ids.append(chunk['chunk_id'])
            chunk_texts.append(chunk['chunk_text'])

            chunk_metadata = {
            'source_filename': chunk['source_filename'],
            'document_id': chunk['document_id'],
            'document_title': chunk['document_title'],
            'chunk_id': chunk['chunk_id'],
            }


            chunk_metadatas.append(chunk_metadata)

    if chunk_ids:
        chunk_collection.upsert(
            ids=chunk_ids,
            documents=chunk_texts,
            metadatas=chunk_metadatas,
        )
        print(f"Chunks stored in Chroma: {chunk_collection.count()}")

        stored_chunks = chunk_collection.get(
            ids=[chunk_ids[0]],
            include=['embeddings'],
        )

        first_embedding = stored_chunks['embeddings'][0]
        print(f"First embedding dimensions: {len(first_embedding)}")

loaded_documents = load_documents()
store_chunks_in_chroma(loaded_documents)

total_chunks = 0

for document in loaded_documents:
    total_chunks += len(document['chunks'])

print(f"Documents processed: {len(loaded_documents)}")
print(f"Total chunks created: {total_chunks}")