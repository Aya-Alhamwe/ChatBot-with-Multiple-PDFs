# Chatbot with Multiple PDFs 📚🤖

A powerful **PDF-based chatbot** that allows you to ask questions from one or more PDF files using AI.  
Built with **Streamlit**, **LangChain**, and **FAISS** for semantic search and contextual question answering.

---

## Features ✨

- Upload **multiple PDFs** and extract their text automatically.  
- Split PDFs into chunks and create **vector embeddings** for fast similarity search.  
- Ask questions and get **detailed AI answers** based on your PDFs.  
- **Download conversation history** as a CSV file.  
- Works with **Google Generative AI** using your own API Key.  
- Modern and clean chat interface with user-friendly design.

---

## Demo Screenshot

![Chatbot Screenshot](https://i.ibb.co/wNmYHsx/langchain-logo.webp)  
*Example of how the chat interface looks.*

---

## Installation 💻

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/ChatBot-with-Multiple-PDFs.git
cd ChatBot-with-Multiple-PDFs
```
## Create a virtual environment and activate it:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

```

## Install dependencies:
```bash
pip install -r requirements.txt

```
Add your Google API Key:

Create a .env file in the root directory:

```bash
# .env
GOOGLE_API_KEY= # Add your Google API Key here
```

Run the app:
```bash
streamlit run app.py
```
## Project Structure 🗂️
```bash
pdf-chatbot/
│
├─ app.py                # Main Streamlit app
├─ requirements.txt      # Required Python packages
├─ runtime.txt           # Python version for Streamlit Cloud
├─ README.md             # Project documentation
├─ .gitignore            # Files to ignore (venv, .env, etc.)
├─ utils/                # Helper modules
│   ├─ __init__.py
│   ├─ pdf_utils.py
│   ├─ vector_utils.py
│   └─ qa_utils.py
└─ .env                  # Your private Google API Key (do not push!)
```

## Usage 📝
-Open the app in your browser.
-Upload one or more PDFs.
-Ask a question in the input field (e.g., "What is the summary of chapter 1?").
-Get AI-generated answers based on your PDF content.
-Download the conversation history if needed.

## Notes ⚠️

-Keep your .env private, do not push the actual key to GitHub.
-The FAISS index (faiss_index/) is generated automatically and does not need to be pushed.
-The app uses Python 3.12.2, specified in runtime.txt.

