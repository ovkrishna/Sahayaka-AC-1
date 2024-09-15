**Generative AI RAG Chatbot with ChromaDB and Azure OpenAI**

Here's the info that reflects the current setup and provides clear instructions for anyone who wants to run your chatbot using main.py. It includes information on installation, execution, and what each part of the project does.

This project implements a Retrieval-Augmented Generation (RAG) chatbot using ChromaDB for embedding storage and Azure OpenAI GPT for generating responses. The chatbot extracts information from PDFs, generates embeddings, stores them in ChromaDB, and retrieves relevant information to answer user queries.

**Project Structure**

- main.py: The entry point for running the chatbot. It extracts text from a PDF, generates embeddings, stores them in ChromaDB, and provides answers to user queries using Azure OpenAI GPT.
- chunking.py: Contains utilities for splitting text into chunks that fit within token limits and truncating context to ensure it's within the token limit for GPT.
- config.py: Stores configuration details such as the path to the PDF and any necessary API keys or environment variables.
- extraction/pdf_extractor.py: Extracts text from the input PDF file.
- embeddings/generate.py: Generates embeddings for each text chunk using Azure OpenAI embeddings.
- chromadb_operations/setup.py: Handles storing embeddings in ChromaDB and counting the stored embeddings.
- chromadb_operations/search.py: Handles searching for the most relevant embeddings in ChromaDB based on the user query.
- models/gpt_response.py: Generates a response using Azure OpenAI GPT based on the user query and the retrieved context.

**Setup Instructions**

1. Clone the Repository
Clone the GitHub repository to your local machine:
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

2. Install Dependencies
Make sure you have Python installed. You can install all the required Python dependencies using the following command:
pip install -r requirements.txt
If you don’t have a requirements.txt, here are the core dependencies you’ll need:
pip install chromadb openai tiktoken

3. Configure API Keys
Make sure to configure your Azure OpenAI API key and ChromaDB setup in the config.py file.

- Azure OpenAI API Key: You can set your API key in the config.py file, like so:
AZURE_API_KEY = "your-azure-openai-api-key"
AZURE_ENDPOINT = "your-azure-openai-endpoint"

- PDF Path: Update the path to the PDF you want to extract text from in the config.py file:
PDF_PATH = "path/to/your/pdf-file.pdf"

4. Run the Chatbot

To run the chatbot, simply execute the main.py file:
python main.py

You’ll be prompted to enter a query. The chatbot will search the ChromaDB for relevant information and generate a response using Azure OpenAI GPT based on the context.

**Project Workflow**

1. PDF Extraction: The text from the provided PDF is extracted using the pdf_extractor.py module.
2. Text Chunking: The extracted text is split into manageable chunks using the split_text_to_fit_token_limit function in chunking.py.
3. Embedding Generation: For each text chunk, an embedding is generated using Azure OpenAI’s embedding API.
4. Embedding Storage: The embeddings are stored in ChromaDB using the store_embeddings_in_chromadb function.
5. Query Handling: When a user enters a query, the chatbot searches for relevant chunks of text in ChromaDB using the search_query function.
6. GPT Response: The retrieved context is passed to the Azure OpenAI GPT model, which generates a response to the user’s query.

**File Breakdown**

- main.py: 
  - Extracts text from the PDF.
  - Splits the text into chunks.
  - Generates embeddings for each chunk.
  - Stores embeddings in ChromaDB.
  - Takes a user query and generates a GPT-based response using the most relevant chunks.

- chunking.py: 
  - Provides utility functions for chunking text and truncating context to ensure it fits within token limits for GPT.

- pdf_extractor.py: 
  - Handles the PDF text extraction process.

- generate.py: 
  - Contains functions for generating embeddings using Azure OpenAI’s embedding API.

- setup.py and search.py: 
  - Handle ChromaDB operations for storing and searching embeddings.

- gpt_response.py: 
  - Sends the user query and retrieved context to Azure OpenAI GPT and generates a response.

**Example Usage**

python main.py
You’ll be prompted with:
Enter your query:
Type your question, such as: "What are decision trees?"
The chatbot will return a response based on the extracted content from the PDF and additional information from GPT.

<img width="724" alt="Screenshot 2024-09-14 184535" src="https://github.com/user-attachments/assets/fa490ec3-1fb8-4349-8feb-eb1e2dd908f3">

<img width="721" alt="Screenshot 2024-09-14 184632" src="https://github.com/user-attachments/assets/b38a2447-d41b-4266-b6e3-55b84b3ff78e">



**Future Enhancements**

- Flask Frontend: You can later extend this project with a Flask-based web interface to allow users to interact with the chatbot through a web browser.
- Add More PDF Files: You can easily extend this setup to handle multiple PDFs and expand the knowledge base by modifying config.py and ChromaDB setup.

**Contributing**

Feel free to fork this repository, create issues, or submit pull requests if you find any bugs or want to contribute to the project!
