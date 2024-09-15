import openai
from config import AZURE_API_KEY, AZURE_ENDPOINT

# Set up the AzureOpenAI client (Ensure you have the correct client initialization)
client = openai.AzureOpenAI(
    api_key=AZURE_API_KEY,
    azure_endpoint=AZURE_ENDPOINT,
    api_version="2024-02-01"  # Update based on your API version
)

# Function to generate a response using Azure OpenAI GPT
def generate_gpt_response(user_query, context):
    # Improved prompt to guide GPT more effectively
    prompt = f"Answer the following query using the context provided below.\n\nQuery: {user_query}\n\nContext: {context}\n\nAnswer:"
    
    # Generate GPT-based response using the user query and context
    response = client.completions.create(
        model="gpt-35-turbo",  # Update to your model's deployment name
        prompt=prompt,
        max_tokens=150
    )
    
    return response.choices[0].text.strip()
