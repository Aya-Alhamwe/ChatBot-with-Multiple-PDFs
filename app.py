import streamlit as st
import pandas as pd
import base64
from datetime import datetime
import asyncio
from dotenv import load_dotenv
import os

from utils.pdf_utils import get_pdf_text, get_text_chunks
from utils.vector_utils import get_vector_store, load_vector_store
from utils.qa_utils import get_conversational_chain

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

def user_input(user_question, model_name, api_key, pdf_docs, conversation_history):
    if api_key is None or pdf_docs is None:
        st.warning("Please upload PDF files and make sure API key is set.")
        return

    # Extract text chunks from uploaded PDFs
    text_chunks = get_text_chunks(get_pdf_text(pdf_docs), model_name)
    get_vector_store(text_chunks, model_name)
    vector_store = load_vector_store(model_name)
    
    # Run similarity search and QA chain
    docs = vector_store.similarity_search(user_question, k=3)
 
    chain = get_conversational_chain(model_name, api_key=api_key)
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    
    user_question_output = user_question
    response_output = response['output_text']
    
    pdf_names = [pdf.name for pdf in pdf_docs] if pdf_docs else []
    conversation_history.append(
        (user_question_output, response_output, model_name,
         datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
         ", ".join(pdf_names))
    )

    # Display conversation
    for question, answer, model_name, timestamp, pdf_name in reversed(conversation_history):
        st.markdown(
            f"""
            **User:** {question}  
            **Bot:** {answer}  
            """,
            unsafe_allow_html=True
        )

    # Download conversation history
    if conversation_history:
        df = pd.DataFrame(conversation_history, columns=["Question", "Answer", "Model", "Timestamp", "PDF Name"])
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="conversation_history.csv"><button>Download conversation history as CSV file</button></a>'
        st.markdown(href, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
    st.header("ChatBot with Multiple PDFs")
    st.markdown("<h3 style='text-align: center; color: gray;'>Aya Alhamwi</h3>", unsafe_allow_html=True)


    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

    model_name = st.sidebar.radio("The Model:", ("Google AI",))
    api_key = API_KEY

    if not api_key:
        st.error(" Google API Key not found! Please add it to your .env file.")
        return

    pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)
    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question, model_name, api_key, pdf_docs, st.session_state.conversation_history)
        st.session_state.user_question = ""

if __name__ == "__main__":
    main()

