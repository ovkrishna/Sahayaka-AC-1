from extraction.pdf_extractor import extract_text_from_pdf
from embeddings.generate import generate_embeddings
from chromadb_operations.setup import store_embeddings_in_chromadb, count_embeddings
from chromadb_operations.search import search_query
from models.gpt_response import generate_gpt_response
from utils.chunking import split_text_to_fit_token_limit,truncate_context
from config import PDF_PATH

import tiktoken  # For token counting

def main():
    # Step 1: Extract text from the PDF
    pdf_text = extract_text_from_pdf(PDF_PATH)
    
    # Step 2: Split text into chunks based on token limit
    chunks = split_text_to_fit_token_limit(pdf_text, max_tokens=4096)
    print(f"Extracted {len(chunks)} chunks from the PDF")
    
    # Step 3: Generate embeddings for each chunk with progress monitoring
    embeddings = []
    for i, chunk in enumerate(chunks):
        print(f"Generating embedding for chunk {i+1} of {len(chunks)}...")
        embedding = generate_embeddings(chunk)
        embeddings.append(embedding)
    
    # Step 4: Store embeddings in ChromaDB
    store_embeddings_in_chromadb(chunks, embeddings)
    print(f"Stored {count_embeddings()} embeddings in ChromaDB")
    
    # Step 5: Handle user query
    user_query = input("Enter your query: ")
    search_results = search_query(user_query)
    
    # Step 6: Flatten the list of documents before joining them
    flat_documents = [doc for sublist in search_results['documents'] for doc in sublist]
    context = "\n".join(flat_documents)  # Join the flattened list of documents
    
    # Step 7: Truncate the context to fit within the token limit, with a buffer
    truncated_context = truncate_context(context, user_query)
    
    # Step 8: Generate GPT-based response using truncated context
    response = generate_gpt_response(user_query, truncated_context)
    
    # Step 9: Print the final response
    print(f"Chatbot Response: {response}")

if __name__ == "__main__":
    main()
