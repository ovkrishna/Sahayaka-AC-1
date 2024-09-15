import tiktoken  # Importing tiktoken for token handling

# Function to split text into chunks based on token limit
def split_text_to_fit_token_limit(text, max_tokens=512):
    """Split text into chunks that fit within the token limit."""
    tokenizer = tiktoken.encoding_for_model("text-embedding-ada-002")
    tokens = tokenizer.encode(text)
    
    # Split tokens into smaller chunks
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        token_chunk = tokens[i:i + max_tokens]
        chunk_text = tokenizer.decode(token_chunk)
        chunks.append(chunk_text)
    
    return chunks

def truncate_context(context, user_query, max_tokens=8192, max_completion_tokens=150, buffer=50):
    """Truncate the context to fit within the model's token limit, with a larger buffer."""
    tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")  # Update if you're using a different model
    query_tokens = len(tokenizer.encode(user_query))
    context_tokens = tokenizer.encode(context)
    
    # Calculate how many tokens we can allocate for the context, leaving a larger buffer
    available_context_tokens = max_tokens - query_tokens - max_completion_tokens - buffer
    
    # If the context is too long, truncate it
    if len(context_tokens) > available_context_tokens:
        truncated_context = tokenizer.decode(context_tokens[:available_context_tokens])
    else:
        truncated_context = context
    
    return truncated_context