from embeddings.generate import generate_embeddings
from chromadb_operations.setup import collection

# Function to perform search on ChromaDB based on user query
def search_query(query, top_k=5):
    query_embedding = generate_embeddings(query)
    
    # Search the collection using the query embedding
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    
    return results
