import os
import sys
import inspect

import streamlit as st

# Llama Index
from llama_index import (
    load_index_from_storage
)

# Import from app.py
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from app import (
    get_service_context,
    get_storage_context,
)

# Text area and send button
st.title("❓ Ask your question ")
question = st.text_area("Enter your question")
send_button = st.button("Send")
    
if send_button and question:
    # Spinner
    st.write("Querying...")

    # Query
    index = load_index_from_storage(
        storage_context=get_storage_context(),
        service_context=get_service_context(),
    )

    query_engine = index.as_query_engine(
        service_context=get_service_context()
    )

    result = query_engine.query(question)
    response_text = result.response

    # Response
    st.write(response_text)
    st.empty()

    # Sources
    formatted_sources = result.get_formatted_sources()
    st.write(formatted_sources)
    st.empty()

    # Extra Info
    st.write(result.extra_info)
