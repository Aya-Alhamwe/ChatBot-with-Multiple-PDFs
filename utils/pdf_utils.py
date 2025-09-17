from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def get_text_chunks(text, model_name):

    if model_name == "Google AI":
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,      
            chunk_overlap=100     
        )
    chunks = text_splitter.split_text(text)
    return chunks
