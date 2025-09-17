from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

def get_conversational_chain(model_name, api_key=None):
    if model_name == "Google AI":
        prompt_template = """
Answer the question as detailed as possible from the provided context.
If the answer is not in the context, just say "answer is not available in the context".
Do not provide incorrect answers.

Context:
{context}

Question:
{question}

Answer:
"""
        model = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0.3,
            google_api_key=api_key
        )
        prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

        chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
        return chain
