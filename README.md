# Chat with Your Data: An Advanced AI Agent 🧠

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This project is a sophisticated, production-ready AI application that allows users to have intelligent conversations with their own data. It features an autonomous AI agent capable of reasoning and using multiple tools to answer complex queries.

The agent's primary tool is a custom-built Retrieval-Augmented Generation (RAG) pipeline that intelligently sources information from user-provided documents. If the answer isn't in the documents, the agent can independently use a live web search to find the most current information.

---

## ✨ Core Features

*   **Multi-Source Data Ingestion**: Process and understand various data formats, including PDFs, websites, and raw text.
*   **Intelligent RAG Pipeline**: Employs a state-of-the-art RAG system using semantic search to find the most relevant information.
*   **Autonomous Agent with ReAct Framework**: Built with the powerful ReAct (Reason + Act) methodology, allowing the agent to reason, choose tools, and synthesize answers.
*   **Dynamic Tool Usage**: Accesses a dynamic toolkit including a custom document search and a live web search.

---

## ⚙️ How It Works

The application follows a modular, service-oriented architecture. A user interacts with a Flask API, which passes the query to a LangChain agent. The agent then orchestrates the entire workflow:

1.  **🧠 Agent Reasoning**: The ReAct agent analyzes the query to decide which tool is best suited to answer it.
2.  **🛠️ Tool Execution**: The chosen tool is executed (either searching the local vector store or calling a web search API).
3.  **📝 LLM Synthesis**: The tool's output is passed back to the Gemini LLM.
4.  **💬 Final Answer**: The LLM synthesizes the information into a human-readable answer for the user.

---

## 🛠️ Technology Stack

*   **Backend**: Python, Flask, Gunicorn
*   **AI/ML**:
    *   **LLM**: Google Gemini Pro
    *   **Agent Framework**: LangChain
    *   **Embeddings**: Sentence-Transformers (`all-MiniLM-L6-v2`)
    *   **Vector Store**: FAISS
    *   **Data Parsing**: PyMuPDF, BeautifulSoup
*   **DevOps**:
    *   **Containerization**: Docker
    *   **CI/CD**: GitHub Actions
    *   **Cloud Deployment**: AWS EC2

---

## 🚀 Getting Started

### Prerequisites

*   Python 3.9+
*   An API key for Google Gemini and Tavily Search.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt 
    ```
    *(Note: You will need to create a `requirements.txt` file.)*

### Configuration

Create a `.env` file in the root directory and add your API keys:
```
GEMINI_API_KEY="your_gemini_api_key"
TAVILY_API_KEY="your_tavily_api_key"
```

---

## ▶️ Usage

### Running the Application

To start the Flask development server:
```bash
flask run
```

For a production environment, use a WSGI server like Gunicorn:
```bash
gunicorn --bind 0.0.0.0:8000 app:app
```

### API Example

Query the agent using `curl`:

```bash
curl -X POST http://127.0.0.1:5000/query \
-H "Content-Type: application/json" \
-d '{"query": "What is the capital of France?"}'
```

---

## 📁 Project Structure
```
.
├── RAG/            # Core RAG pipeline implementation
├── indexer/        # Logic for creating and managing the vector index
├── loaders/        # Data loaders for different file formats
├── test.py         # Test file
├── app.log         # Application log file
├── input.txt       # Example input for data loaders
├── README.md       # This file
└── .gitignore      # Git ignore file
```

---

## 🌟 Key Engineering Highlights

*   **Production-Ready API**: Scalable backend built with Flask and Gunicorn.
*   **Modular RAG System**: The RAG pipeline is encapsulated, making it reusable and testable.
*   **Advanced Agentic Workflow**: Demonstrates modern LLM capabilities beyond simple prompt-and-response.
*   **Full CI/CD Automation**: Complete pipeline using GitHub Actions for testing, building, and deploying.
*   **Infrastructure as Code**: Containerized with Docker for consistent environments.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.