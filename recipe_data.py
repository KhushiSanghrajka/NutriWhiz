from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_core.tools import tool
import json
import os

OPENAI_API_KEY = os.getenv("OPENAI_KEY")
# Initialize OpenAI embeddings
embeddings = OpenAIEmbeddings(
    base_url="https://models.inference.ai.azure.com",
    model="text-embedding-3-small",
    api_key=OPENAI_API_KEY  # Replace with your actual API key
)

# Step 1: Load documents (CSV file)
loader = CSVLoader("recipes/IndianHealthyRecipe.csv")
documents = loader.load()[:20]  # Load only 20 documents for now
print("Loaded CSV")

# Step 2: Split text into chunks
def make_chunks(documents, max_chunk_size=500):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=max_chunk_size, chunk_overlap=200)
    
    all_chunks = []
    for doc in documents:
        text = doc.page_content
        chunks = text_splitter.split_text(text)
        all_chunks.extend(chunks)
    return all_chunks

# Step 3: Create and save FAISS vector store
def chunk_store(text_chunks):
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_db")
    return vector_store

# Step 4: Load FAISS vector store
def load_vector_store():
    return FAISS.load_local("faiss_db", embeddings=embeddings, allow_dangerous_deserialization=True)

#steP 5: Query FAISS vector store
def query_vector_store(query, k=2):
    vector_store = load_vector_store()
    results = vector_store.similarity_search(query, k=k)
    return results

# Recipe Agent Tool
@tool
def recipe_agent(query: str, k: int = 1) -> dict:
    """
    Searches the FAISS vector store for the most relevant recipes based on the user's query.
    """
    text_chunks = make_chunks(documents, max_chunk_size=500)
    
    # Create and save FAISS vector store
    vector_store = chunk_store(text_chunks)
    print("FAISS vector store created and saved!")

    results = query_vector_store(query)
    for i, result in enumerate(results):
        print(f"Result {i + 1}: {result.page_content}")
    recipe_vector_store = load_vector_store()

    # Perform similarity search
    results = recipe_vector_store.similarity_search(query, k=k)

    # If no results are found, return a relevant message
    if not results:
        return {"error": "No relevant recipes found for your query."}

    # Return the search results
    recipe = result.page_content
    response = {"recipes": recipe}
    response = json.dumps(response)
    print("Response:::",response)
    # recipe[]
    return response
