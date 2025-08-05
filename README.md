Chat with Your Data: An Advanced AI Agent 🧠
This project is a sophisticated, production-ready AI application that allows users to have intelligent conversations with their own data. It's more than just a script; it's a well-engineered system featuring an autonomous AI agent capable of reasoning and using multiple tools to answer complex queries.

The agent's primary tool is a custom-built Retrieval-Augmented Generation (RAG) pipeline that intelligently sources information from user-provided documents (PDFs, websites, text). If the answer isn't in the documents, the agent can independently decide to use a live web search tool to find the most current information.

Core Features ✨
Multi-Source Data Ingestion: Process and understand various data formats, including:

PDF documents (.pdf)

Live website content (via URL)

Raw text snippets

Intelligent RAG Pipeline: Employs a state-of-the-art RAG system that uses semantic search to find the most relevant pieces of information from the ingested documents to answer user questions.

Autonomous Agent with ReAct Framework: At its core is an agent built with the powerful ReAct (Reason + Act) methodology. This allows the agent to reason about a user's query, choose the appropriate tool, and synthesize the information into a coherent answer.

Dynamic Tool Usage: The agent has access to a dynamic toolkit:

Custom Document Search: For questions related to the user's private knowledge base.

Live Web Search: For general knowledge questions or topics not covered in the documents.

System Architecture ⚙️
The application follows a modular, service-oriented architecture designed for scalability and maintainability. The user interacts with a Flask API, which passes the query to the LangChain agent. The agent then orchestrates the entire workflow.

The logical flow is as follows:

User Query: The user sends a query through the API.

Agent Reasoning: The ReAct agent analyzes the query and decides which tool is best suited to answer it. For example, "What did the Q3 report say about revenue?" will trigger the Document Search, while "What's the weather like in London today?" will trigger the Web Search.

Tool Execution: The chosen tool is executed (either searching the FAISS vector index or calling the Tavily Search API).

LLM Synthesis: The output from the tool is passed back to the Gemini LLM.

Final Answer: The LLM synthesizes the tool's output into a final, human-readable answer and sends it back to the user.

Technology Stack 🛠️
This project utilizes a modern, robust tech stack, emphasizing best practices in AI engineering and DevOps.

Backend: Python, Flask, Gunicorn

AI/ML:

LLM: Google Gemini Pro

Agent Framework: LangChain (for ReAct agent implementation)

Embeddings: Sentence-Transformers (all-MiniLM-L6-v2)

Vector Store: FAISS (Facebook AI Similarity Search)

Data Parsing: PyMuPDF, BeautifulSoup

DevOps:

Containerization: Docker

CI/CD: GitHub Actions

Cloud Deployment: AWS EC2

Key Engineering Highlights 🚀
This project was built not just to work, but to work well. It showcases several key engineering principles that are critical for building real-world AI systems.

Production-Ready API: A scalable backend built with Flask, ready to be served by a production-grade WSGI server like Gunicorn.

Modular RAG System: The entire RAG pipeline is encapsulated within its own class, making it a reusable and independently testable component.

Advanced Agentic Workflow: The implementation of the ReAct framework demonstrates a deeper understanding of modern LLM capabilities beyond simple prompt-and-response.

Full CI/CD Automation: A complete pipeline using GitHub Actions automates code linting, unit testing, Docker image building, and secure deployment to the AWS cloud on every push to main.

Infrastructure as Code Principles: The entire application is containerized with Docker, ensuring that the development environment is identical to the production environment, eliminating "it works on my machine" issues.
