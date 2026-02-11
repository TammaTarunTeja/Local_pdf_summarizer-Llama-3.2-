# Local PDF Summarizer (Llama 3.2)

A lightweight tool that allows you to summarize PDF documents locally using the Llama 3.2 model. 
---

## Features

- **Local Processing**: Your data never leaves your machine. Summarization is performed locally using Llama 3.2.
- **Streamlit Interface**: A clean, user-friendly web interface for uploading PDFs and viewing summaries.

---

## Classification Framework

The system follows a tiered approach to ensure speed and accuracy:
1.  **LLM (Llama 3.2)**: Acts as the primary summarizer and a fallback classifier for unknown or low-sample data patterns.

![Architecture](./arch.png)

---

## Project Structure

```text
├── app.py               # Streamlit frontend
├── pipeline.py          # Core logic for summarization
└── requirements.txt     # Project dependencies
