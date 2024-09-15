import chromadb
from config import CHROMADB_COLLECTION

# Initialize ChromaDB client and create a collection
client = chromadb.Client()
collection = client.create_collection(CHROMADB_COLLECTION)

# Function to store embeddings into ChromaDB
def store_embeddings_in_chromadb(chunks, embeddings):
    ids = [f"chunk-{i}" for i in range(len(chunks))]  # Generate unique IDs for each chunk
    collection.add(
        ids=ids,  # Unique IDs for each document
        documents=chunks,  # The text chunks
        embeddings=embeddings,  # The corresponding embeddings
        metadatas=[{"source": f"Chunk {i} from PDF"} for i in range(len(chunks))]  # Optional metadata
    )

# To count stored embeddings in ChromaDB
def count_embeddings():
    return collection.count()
