import streamlit as st
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Importaciones ajustadas a tu configuración
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# Configuración de la interfaz
st.set_page_config(page_title="NexusDocs")
st.title("🤖 NexusDocs: Agente Corporativo")

# Cargar configuración desde .env
api_key = os.getenv("GROQ_API_KEY")
model_name = os.getenv("GROQ_MODEL_NAME")

if not api_key:
    st.error("Error: GROQ_API_KEY no encontrada en el archivo .env")
else:
    # Procesamiento de documentos
    loader = DirectoryLoader('./docs', glob="./*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma.from_documents(texts, embeddings)

    # Inicialización del modelo
    llm = ChatGroq(groq_api_key=api_key, model_name=model_name)

    # Configuración de la cadena RAG
    prompt = ChatPromptTemplate.from_template("""
    Responde la pregunta basándote únicamente en el contexto proporcionado:
    {context}
    Pregunta: {input}
    """)

    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(db.as_retriever(), combine_docs_chain)

    # Chat
    query = st.text_input("¿Qué deseas saber sobre los documentos?")
    if query:
        response = retrieval_chain.invoke({"input": query})
        st.write(response["answer"])