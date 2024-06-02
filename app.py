import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os 
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()

# Configure Google Generative AI with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to read text from uploaded PDF files
def read_pdf(pdf):
    text = ""
    for file in pdf:
        pdf_read = PdfReader(file)
        for page in pdf_read.pages:
            text += page.extract_text()
    return text

# Function to split the text into smaller chunks for processing
def get_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=20000, chunk_overlap=500)
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create a vector store from text chunks
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss-index")

# Function to create a question-answering chain using Google Generative AI
def get_conversation_chain_pdf():
    prompt_template = """ 
    Your role is to be a meticulous researcher. Answer the question using only the information found within the context. Be detailed, but avoid unnecessary rambling. If you cannot find the answer, simply state 'answer is not available'.
    Context: \n{context}\n
    Question: \n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.5)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

# Function to handle user queries and display the response
def user_input(user_query):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    load_vector_db = FAISS.load_local("faiss-index", embeddings, allow_dangerous_deserialization=True)
    docs = load_vector_db.similarity_search(user_query)
    chain = get_conversation_chain_pdf()
    response = chain(
        {
            "input_documents": docs, "question": user_query
        },
        return_only_outputs=True
    )
    st.write(f"**Question:** {user_query}")
    st.write(f"**Answer:** {response['output_text']}")

# Main function to run the Streamlit app
def main():
    st.set_page_config(page_title="PDF Chat App", page_icon=":page_with_curl:")
    st.title("📄 Chat with your PDF files using Google Gemini Pro 🚀")
    user_query = st.text_input("❓ Ask a question about the PDF File:")
    if user_query:
        user_input(user_query)

    with st.sidebar:
        st.title("Menu 📚")
        pdf_docs = st.file_uploader("📂 Upload your PDF File(s)", accept_multiple_files=True)
        if st.button("Submit"):
            with st.spinner('Processing... ⏳'):
                raw_text = read_pdf(pdf_docs)
                text_chunks = get_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Processing Done! ✅")

    # Footer
    st.markdown("""
    ---
    Powered by [Google Gemini](https://gemini.google.com/app) :rocket:
    """)

if __name__ == "__main__":
    main()
