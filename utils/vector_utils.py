from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def get_vector_store(text_chunks, model_name):
    if model_name == "Google AI":
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")
    return vector_store

def load_vector_store(model_name):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    return vector_store
