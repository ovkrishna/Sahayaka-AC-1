import os
import tiktoken  # For counting tokens
from openai import AzureOpenAI
from config import AZURE_API_KEY, AZURE_ENDPOINT

# Set up the AzureOpenAI client
client = AzureOpenAI(
    api_key=AZURE_API_KEY,  # Fetch from config.py
    api_version="2024-02-01",  # API version
    azure_endpoint=AZURE_ENDPOINT  # Azure OpenAI endpoint
)

# Define the tokenizer for the model
tokenizer = tiktoken.encoding_for_model("text-embedding-ada-002")

# Function to generate embeddings for text using Azure OpenAI
def generate_embeddings(text):
    # Check token length
    tokens = tokenizer.encode(text)
    
    # Ensure the text is under the token limit (say 4096 for safety)
    max_tokens = 4096
    if len(tokens) > max_tokens:
        raise ValueError(f"Text too long: {len(tokens)} tokens. Please reduce the size of the text.")
    
    # Generate embeddings
    response = client.embeddings.create(
        input=text,  # The text to embed
        model="text-embedding-ada-002"  # Azure OpenAI embedding model
    )
    
    # Return the embedding data
    return response.data[0].embedding
