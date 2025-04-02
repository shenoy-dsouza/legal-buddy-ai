import faiss
from sentence_transformers import SentenceTransformer
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import numpy as np
import ollama


# Load legal documents (PDFs)
document_paths = ["app/legal_docs/tenant_laws.pdf"]
documents = []
for path in document_paths:
    loader = PyPDFLoader(path)
    documents.extend(loader.load())

# Use SentenceTransformer for embeddings
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Split and embed documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

texts = [chunk.page_content for chunk in chunks]
embeddings = np.array(embedding_model.encode(texts)).astype(np.float32)

# Ensure embeddings is a 2D array
if len(embeddings.shape) == 1:
    embeddings = embeddings.reshape(1, -1)


# Create FAISS vector store
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)


def process_legal_query(question: str) -> str:    
    # Generate query embedding
    query_embedding = np.array(embedding_model.encode(question)).astype(np.float32).reshape(1, -1)

    # Retrieve the most relevant document chunk
    _, indices = index.search(query_embedding, k=3)
    retrieved_text = chunks[indices[0][0]].page_content

    # Construct a prompt for Ollama
    prompt = f"Answer the question using the legal context below:\n\nContext: {retrieved_text}\n\nQuestion: {question}\nAnswer:"
    
    # Call Ollama's Llama3 model
    response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])

    # Extract response from Ollama
    short_answer = response["message"]["content"].strip()

    # Format as JSON
    return {
        "query": question,
        "answer": short_answer
    }
