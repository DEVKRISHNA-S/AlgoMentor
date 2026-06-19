# AlgoMentor

A local AI-powered DSA mentor built with Streamlit, Ollama, and VibeThinker-3B.

AlgoMentor helps users learn Data Structures and Algorithms through guided problem solving, code reviews, and personalized knowledge retrieval.

## Features

### Chat Mode

Ask DSA questions and receive guided explanations.

Examples:

* Explain Binary Search
* What is Kadane's Algorithm?
* How does DFS work?

### Problem Solver Mode

Paste a LeetCode or Codeforces problem and get:

* Pattern Identification
* Difficulty Analysis
* Brute Force Approach
* Guided Hints
* Optimized Approach

### Code Review Mode

Paste your code and receive:

* Logic Feedback
* Complexity Discussion
* Improvement Suggestions
* DSA-focused Review

### Conversation Memory

AlgoMentor remembers previous messages during the current session and maintains conversational context.

### Local LLM

Powered entirely by a locally running VibeThinker-3B model through Ollama.

No API keys required.

### RAG Foundation

Includes a Retrieval-Augmented Generation pipeline using:

* Sentence Transformers
* FAISS Vector Search
* Local Knowledge Base

Current knowledge sources:

* Markdown Notes
* DSA Documentation

Future versions will support:

* PDF Uploads
* DOCX Uploads
* Personal DSA Notes

---

## Tech Stack

### Frontend

* Streamlit

### LLM

* Ollama
* VibeThinker-3B

### RAG

* Sentence Transformers
* FAISS

### Language

* Python 3.12.10

### Environment Management

* uv

---

## Project Structure

```text
app/

├── llm/
│   └── ollama_client.py
│
├── prompts/
│   ├── mentor.txt
│   ├── problem_solver.txt
│   └── code_review.txt
│
├── rag/
│   ├── embedder.py
│   ├── build_index.py
│   ├── retriever.py
│   └── vector_store.py
│
├── services/
├── ui/
└── main.py

data/
vectorstore/
```

---

## Installation

Clone the repository:

```bash
git clone <repo-url>
cd algomentor
```

Create environment:

```bash
uv venv --python 3.12.10
```

Activate environment:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
uv sync
```

---

## Run Ollama Model

Start Ollama:

```bash
ollama run vibethinker3b
```

---

## Build Knowledge Base

After adding notes inside the `data/` folder:

```bash
python -m app.rag.build_index
```

This generates:

```text
vectorstore/
├── faiss_index
└── documents.txt
```

---

## Run Application

```bash
streamlit run app/main.py
```

---

## Roadmap

### Version 0.3

* Structured Problem Solver
* Structured Code Review

### Version 0.4

* PDF Upload Support
* DOCX Upload Support
* Automatic Knowledge Base Indexing

### Version 0.5

* Full RAG Integration with VibeThinker

### Version 1.0

* Personal DSA Mentor
* User Knowledge Base
* Learning Progress Tracking

```
```
