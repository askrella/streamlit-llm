import os
import sys
import inspect

# Streamlit
import streamlit as st

# Llama Index
from llama_index import (
    SimpleDirectoryReader,  Document,
    load_index_from_storage
)

# FFMPEG
import ffmpeg

# Import from app
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from app import (
    TEMP_PATH,
    VECTOR_STORE_PATH,
    get_service_context,
    get_storage_context,
    transcribe_audio
)

# File upload container
file_upload_container = st.container()

with file_upload_container:
    st.title("📁 Upload your file")
    uploaded_file = st.file_uploader("File")
    
    if not uploaded_file:
        st.stop()
    
    uploaded_file_name: str = uploaded_file.name
    uploaded_file_buffer = uploaded_file.getbuffer()
    
    document_text: str = None
    
    # If temp folder doesnt exist, create it
    if not os.path.exists(TEMP_PATH):
        os.mkdir(TEMP_PATH)

    # Video support
    if uploaded_file_name.endswith('.mp4'):
        # Write Video file to temp file
        video_temp_file = os.path.join(TEMP_PATH, uploaded_file_name)
        with open(video_temp_file, "wb") as f:
            f.write(uploaded_file_buffer)

        # Transcribe
        document_text = transcribe_audio(video_temp_file)
        
        # Delete temp files
        os.unlink(video_temp_file)

    # Audio support
    elif uploaded_file_name.endswith(('.mp3', '.ogg', '.wav')):
        # Write audio file to temp file
        audio_temp_file = os.path.join(TEMP_PATH, uploaded_file_name)
        with open(audio_temp_file, "wb") as f:
            f.write(uploaded_file_buffer)

        # Transcribe
        transcription_text = transcribe_audio(audio_temp_file)
        document_text = transcription_text
        
        # Delete temp file
        os.unlink(audio_temp_file)

    # Text Support
    else:
        # Write text file to temp file
        text_temp_file = os.path.join(TEMP_PATH, uploaded_file_name)
        with open(text_temp_file, "wb") as f:
            f.write(uploaded_file_buffer)
        
        # Read file with simple directory reader
        documents = SimpleDirectoryReader(input_files=[text_temp_file]).load_data()
        
        document_text = documents[0].text
        print(document_text)
        pass
            
    # Load index and insert document
    if document_text:
        index = load_index_from_storage(
            storage_context=get_storage_context(),
            service_context=get_service_context(),
        )
        
        index.insert(Document(text=document_text, extra_info={"file_name": uploaded_file_name}))
        
        # Persist index
        index.storage_context.persist(VECTOR_STORE_PATH)
        
        # Success
        st.write(f"File was inserted, ready to query!")
