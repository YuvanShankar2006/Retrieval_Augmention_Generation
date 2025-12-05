# 📚 RAG : A Comprehensive Study & Implementation

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-green)
![Status](https://img.shields.io/badge/Status-Active%20Research-orange)

## 🚀 About The Project

Welcome to **RAG-Zero-to-Hero**. This repository is not just another RAG wrapper; it is a documentation of my journey building Retrieval-Augmented Generation systems from scratch. 

The goal of this project is to deconstruct every component of the RAG pipeline—from data ingestion to vector retrieval—to understand how different choices affect performance, cost, and accuracy.



### 🎯 Key Objectives
* **Universal Ingestion:** Handling real-world dirty data (PDFs, CSVs, JSON, Text).
* **Chunking Strategy Analysis:** Studying how `Fixed-size`, `Recursive`, and `Semantic` chunking impact context retrieval.
* **Vector Database Showdown:** Benchmarking **FAISS**, **ChromaDB**, and **Pinecone**.
* **Embedding Evaluation:** Comparing open-source (HuggingFace) vs. proprietary (OpenAI/Cohere) embedding models.

---

## 🏗️ Architecture & Features

### 1. Data Ingestion Pipeline
I have built modular loaders to handle various file formats:
* **Unstructured Data:** PDFs (using `pypdf`, `unstructured`), `.txt` files.
* **Structured Data:** CSVs (row-based vs. column-based ingestion), JSON.

### 2. The Chunking Laboratory
One of the hardest parts of RAG is deciding how to split text. This repo contains notebooks comparing:
* **Character Splitting:** Simple, fast, but often breaks context.
* **Recursive Character Splitting:** Tries to keep paragraphs together.
* **Semantic Chunking:** Uses embeddings to split text based on meaning, not just syntax.

### 3. Vector Database Implementations
I have implemented adapters for different vector stores to compare their DX (Developer Experience) and latency:

| Database | Type | Use Case in this Repo |
| :--- | :--- | :--- |
| **FAISS** | In-memory/Local | Rapid prototyping & speed benchmarking |
| **ChromaDB** | Local/Server | Persistent local storage & metadata filtering |
| **Pinecone** | Cloud | Scalable, production-grade cloud retrieval |

---

## 🧪 Experiments & Analysis

*This section documents my findings (The "How I Learned" part).*

### 📊 Embedding Model Comparison
| Model | Dimensions | MTEB Score (Approx) | Notes |
| :--- | :---: | :---: | :--- |
| `text-embedding-3-small` | 1536 | High | Best all-rounder for cost/performance. |
| `all-MiniLM-L6-v2` | 384 | Medium | Incredible for local-only speed. |
| `e5-large-v2` | 1024 | High | Great open-source alternative. |

### ✂️ Chunking Findings
> **Observation:** Through testing, I found that for distinct Q&A on PDF documents, a `RecursiveCharacterTextSplitter` with a chunk size of 1000 and overlap of 200 performed best. However, for the CSV data, row-level chunking was strictly required to maintain data integrity.

---

## 🛠️ Getting Started

### Prerequisites
* Python 3.10+
* API Keys (OpenAI, Pinecone) in a `.env` file.

### Installation

1. **Clone the repo**
   ```bash
   git clone [https://github.com/YuvanShankar2006/Retrieval_Augmention_Generation.git](https://github.com/YuvanShankar2006/Retrieval_Augmention_Generation.git)
   cd Retrieval_Augmention_Generation
