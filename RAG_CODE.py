import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain_community.llms import Ollama
from langchain.document_loaders import PyPDFLoader
import tempfile  # For temporary file handling



load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
groq_api_key=os.environ['GROQ_API_KEY']



# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: #ffffff;
    }
    
   .title {
        color: #4CAF50;
        font-size: 36px;
        font-weight: bold;
        border: 3px solid #4CAF50;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-top: 0;
        margin-bottom: 20px; /* Adds space below the subtitle */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main container with custom styling
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    
    # Premium-looking title with royal blue color and border
    st.markdown(
        """
        <h1 class="title">
        📚🔍RAG-based Chatbot
        </h1>
        """,
        unsafe_allow_html=True
    )

    # File uploader for document upload
    uploaded_file = st.file_uploader("Upload a document (PDF or Text):", type=["pdf", "txt"])

    if uploaded_file:
        st.success("Document uploaded successfully!")
        
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name
        
        # Process PDF or Text file
        try:
            if uploaded_file.type == "application/pdf":
                loader = PyPDFLoader(temp_file_path)
                docs = loader.load()
                st.write("Processing PDF...")
            elif uploaded_file.type == "text/plain":
                file_content = uploaded_file.read().decode("utf-8")
                docs = [{"text": file_content}]  # Mock document format for text
                st.text_area("Document Content", file_content, height=300)
            
            # Proceed with embedding and vector store setup
            embeddings = OllamaEmbeddings()
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            final_documents = text_splitter.split_documents(docs[:50])
            vectors = Chroma.from_documents(final_documents, embeddings)
            
            # Set up retrieval and prompt chain
            llm=ChatGroq(groq_api_key=groq_api_key,
             model_name="mixtral-8x7b-32768")
            prompt = ChatPromptTemplate.from_template(
                """
                Answer the questions based on the provided context only.
                Please provide the most accurate response based on the question.
                <context>
                {context}
                <context>
                Question: {input}
                """
            )
            
            document_chain = create_stuff_documents_chain(llm, prompt)
            retriever = vectors.as_retriever()
            retrieval_chain = create_retrieval_chain(retriever, document_chain)

            # Placeholder for chatbot interaction
            user_input = st.text_input("Chat with the RAG-based chatbot:", placeholder="Ask me anything...")

            if user_input:
                response = retrieval_chain.invoke({"input": user_input})
                st.write("Response: ", response['answer'])  # Display the chatbot response

        finally:
            # Clean up the temporary file
            os.remove(temp_file_path)

    st.markdown('</div>', unsafe_allow_html=True)

