# Legal Buddy AI

Legal Buddy AI is an AI-powered legal assistant designed to provide instant answers to legal queries related to **Residential and Commercial Tenancy** in India. It utilizes NLP-based search and retrieval mechanisms to fetch relevant legal information from Indian tenancy laws and regulations. The AI also leverages large language models to generate concise and relevant responses.

> *Note: Future updates will expand support to additional legal domains.*

## Features
- 🏠 **Tenancy Law Assistance**: Provides legal information on rent agreements, eviction rules, security deposits, and more.
- 📜 **Legal Document Processing**: Parses and indexes tenancy-related legal documents (PDFs) using NLP-based embeddings.
- 🔍 **Smart Query Handling**: Retrieves relevant sections from tenancy laws based on user questions.
- 🤖 **AI-Powered Responses**: Uses Llama3.2 (via Ollama) to generate concise legal responses.
- ⚡ **FastAPI Backend**: Provides an easy-to-use REST API.
- 📖 **API Documentation**: Swagger UI and ReDoc are available for easy API exploration.
- 🏗️ **Scalable & Modular**: Designed for future expansions beyond tenancy laws.

---

## Installation & Setup

### 1. Clone the Repository
```sh
$ git clone https://github.com/shenoy-dsouza/legal-buddy-ai.git
$ cd legal-buddy-ai
```

### 2. Create and Activate a Virtual Environment
```sh
$ python3 -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4. Install and Set Up Ollama
Legal Buddy AI relies on **Ollama** for running large language models locally. Ensure you have **Ollama installed**.

#### Install Ollama

##### **For macOS**
```sh
brew install ollama
```
Or download the macOS installer from: [https://ollama.com/download](https://ollama.com/download)

##### **For Windows**
1. Download the Windows installer from: [https://ollama.com/download](https://ollama.com/download)
2. Run the installer and follow the setup instructions.

##### **For Linux**
```sh
curl -fsSL https://ollama.com/install.sh | sh
```

#### Pull Required Models
```sh
$ ollama pull llama3.2
```

### 5. Run the Application
```sh
$ uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000/`.

---

## API Documentation
- **Swagger UI**: Available at `http://127.0.0.1:8000/docs`
- **ReDoc**: Available at `http://127.0.0.1:8000/redoc`

---

## API Usage

### 1. Check API Status
**Endpoint:** `GET /`

**Response:**
```json
{
    "message": "Legal Buddy AI is running!"
}
```

### 2. Ask a Tenancy-Related Legal Question

**Endpoint:** `POST /ask`

#### Example 1: Rent Increase Query  
**Request:**  
```json
{
    "question": "Is my landlord allowed to increase my rent without prior notice?"
}
```

**Response:**  
```json
{
    "query": "Is my landlord allowed to increase my rent without prior notice?",
    "answer": "No, your landlord is not allowed to increase your rent without prior agreement. According to the context, any increase in rent must be agreed upon by both parties prior to the commencement of work. If your landlord attempts to increase the rent without your consent, you may be entitled to a reduction in rent or other remedies, depending on the specific circumstances and applicable laws."
}
```

#### Example 2: Security Deposit Limits  
**Request:**  
```json
{
    "question": "Is my landlord allowed to ask for more than two months’ rent as a security deposit?"
}
```

**Response:**  
```json
{
    "query": "Is my landlord allowed to ask for more than two months’ rent as a security deposit?",
    "answer": "No, your landlord is not allowed to ask for more than three times the monthly rent as a security deposit, unless there is an agreement to the contrary. According to Chapter IV, Section 11 of the provided context, charging a security deposit in excess of three times the monthly rent is unlawful."
}
```

---

## Future Enhancements

- 📂 **Case Study Files (PDF) Support**: Users can upload legal case study PDFs, and the AI will extract relevant legal advice. The bot will be trained on these files so that it can provide legal advice when requested.
- 💬 **Multi-Language Support**: Answer queries in regional Indian languages.
- 🔗 **Legal Expert Consultation**: Connect users with verified legal experts.
- 📚 **Expanded Legal Database**: Future updates will include more legal domains beyond tenancy laws.

---

