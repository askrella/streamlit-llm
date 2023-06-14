import streamlit as st 
import os
import openai

# Llama Index
from llama_index import (
    ServiceContext,
    StorageContext,
    VectorStoreIndex,
    LangchainEmbedding
)

# Langchain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings

# OpenAI Whisper
import whisper

# Util
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Constants
VECTOR_STORE_PATH = './vector_store'
TEMP_PATH = './temp'
AUDIO_EXTENSIONS = ('.mp3', '.ogg', '.wav')

# Streamlit app
st.set_page_config(
    page_title="Streamlit LLM",
    page_icon="👋",
)

st.write("# Welcome to Streamlit LLM! 👋")
st.sidebar.success("Select an option above.")

# Build & cache service context
@st.cache_resource
def get_service_context():
    llm = ChatOpenAI(
        temperature=0.9,
    )

    embed_model = LangchainEmbedding(
        HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2"
        )
    )

    service_context = ServiceContext.from_defaults(
        llm=llm,
        embed_model=embed_model,
    )

    return service_context

def get_storage_context():
    # If vector store doesnt exist, create it
    if not os.path.exists(VECTOR_STORE_PATH):
        index = VectorStoreIndex.from_documents(
            [],
            service_context=get_service_context()
        )
        index.storage_context.persist(VECTOR_STORE_PATH)
    
    return StorageContext.from_defaults(
        persist_dir=VECTOR_STORE_PATH,
    )

@st.cache_resource
def get_whisper_model():
    return whisper.load_model("base")

# Transcribe audio
def transcribe_audio(audio_file_path):
    model = get_whisper_model()

    st.write(f"Transcribing audio file...")
    transcription = model.transcribe(audio_file_path)
    transcription_text = transcription["text"]

    # Strip transcription text
    transcription_text = transcription_text.strip()
    
    return transcription_text

