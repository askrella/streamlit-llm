import streamlit as st 
import os
import openai
import shutil

from llama_index import ServiceContext, VectorStoreIndex, SimpleDirectoryReader, LangchainEmbedding
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

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

# Constants
DATA_PATH = './data'

# Function to save uploaded file
def save_uploadedfile(uploadedfile):
    # Create data/ folder if it doesn't exist
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)

    # Save file to data/ folder
    with open(os.path.join(DATA_PATH, uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())

# Query function
def semantic_search(query):
    documents = SimpleDirectoryReader(DATA_PATH).load_data()
    index = VectorStoreIndex.from_documents(documents, service_context=get_service_context())
    engine = index.as_query_engine(service_context=get_service_context())
    response = engine.query(query)
    return response

# Streamlit app
st.set_page_config(layout='centered')
st.title('Streamlit LLM')

# Password protection
password = st.text_input("Password:", type="password")
if password != os.environ.get("PASSWORD"):
    st.stop()

# Streamlit components
uploaded_file = st.file_uploader("Upload your file")
question = st.text_area("Enter your question")

# Upload
if uploaded_file is not None:
    save_uploadedfile(uploaded_file)
    print(f"Uploaded {uploaded_file.name} to {DATA_PATH} folder!")

# Buttons
if os.path.exists(DATA_PATH):
    send_button = st.button("Send", type="primary")
    delete_button = st.button("Delete", type="primary")

    # Delete button
    if delete_button:
        print(f"Deleting {DATA_PATH} folder...")
        shutil.rmtree(DATA_PATH)

        # Create data/ folder
        os.mkdir(DATA_PATH)

        st.write("Deleted data folder!")

    # Send button
    if send_button:
        # Print question
        st.title("Question:")
        st.write(question)

        # Spinner
        st.spinner("Querying...")

        # Query
        print(f"Question: {question}")
        result = semantic_search(question)

        # Answer
        response_text = result.response
        st.title("Answer")
        st.write(response_text)
        print(f"Answer: {response_text}")

        # Sources
        formatted_sources = result.get_formatted_sources()
        st.title("Sources")
        st.write(formatted_sources)
        print(f"Sources: {formatted_sources}")

        # Extra Info
        st.title("Extra Info")
        st.write(result.extra_info)
        print(f"Extra Info: {result.extra_info}")
