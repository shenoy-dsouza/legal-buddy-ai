import faiss
import numpy as np
import ollama
from sentence_transformers import SentenceTransformer
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.core.config import MODEL_NAME, PDF_PATH
from app.models.schemas import QueryResponse


def initialize_search():
    """Loads legal documents, creates embeddings, and initializes FAISS index."""
    global embedding_model, index, chunks

    # Load legal documents
    documents = []
    loader = PyPDFLoader(PDF_PATH)
    documents.extend(loader.load())

    # Load embedding model
    embedding_model = SentenceTransformer(MODEL_NAME)

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50
    )
    chunks = text_splitter.split_documents(documents)

    texts = [chunk.page_content for chunk in chunks]
    embeddings = np.array(embedding_model.encode(texts)).astype(np.float32)

    # Create FAISS vector store
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    print("✅ FAISS index initialized successfully!")


def fetch_answer(question: str) -> QueryResponse:
    """Processes a legal query using FAISS for retrieval
    and Ollama for AI-generated responses."""

    # Generate query embedding
    query_embedding = (
        np.array(embedding_model.encode(question))
        .astype(np.float32)
        .reshape(1, -1)
    )

    # Retrieve most relevant document chunk
    _, indices = index.search(query_embedding, k=3)
    retrieved_text = chunks[indices[0][0]].page_content

    # Construct a prompt for Ollama
    prompt = (
        "Answer the question using the legal context below:\n\n"
        f"Context: {retrieved_text}\n\n"
        f"Question: {question}\nAnswer:"
    )

    # Call Ollama's Llama3 model
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
    )

    # Extract response
    short_answer = response["message"]["content"].strip()

    return QueryResponse(query=question, answer=short_answer)
