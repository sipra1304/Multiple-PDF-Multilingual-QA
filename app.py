import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("Google_API_Key"))

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectore_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vectore_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template=""" 
    Answer the question as directed by the user in details and if the answer is not in the context simply say "answer is not there in the context", dont provide the wrong answer.
    Context:\n{context}? \n
    Question: {question} \n
    
    Answer: {answer} :
    """
    model=ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.4)
    
    prompt=PromptTemplate(template=prompt_template, input_variables=["context","question"])
    chain=load_qa_chain(model,chain_type="stuff",prompt=prompt)
    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    
    chain = get_conversational_chain()
    
    # Prepare input for chain function
    input_data = {
        "input_documents": docs,
        "question": user_question,
        "answer": "answer"  # Provide an empty string or appropriate default value for 'answer'
    }
    
    response = chain(input_data, return_only_outputs=True)
    
    print(response)
    st.write("Reply: ", response["output_text"])

# Streamlit frontend
def main():
    st.header("PDF Question Answering System")
    
    user_question = st.text_input("ask a question based on pdf")
    
    if user_question:
        user_input(user_question)
    
    
    with st.sidebar:
        st.title("Uploads")
        
        pdf_docs = st.file_uploader("Choose PDF files", type=["pdf"], accept_multiple_files=True)
    
        if st.button("Submit"):
            with st.spinner("Processing..."):
                pdf_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(pdf_text)
                get_vector_store(text_chunks)
                st.success("PDFs uploaded!")


if __name__ == "__main__":
    main()          
