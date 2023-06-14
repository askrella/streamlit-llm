import os
import sys
import inspect

# Streamlit
import streamlit as st

# Util
import shutil

# Import from app
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from app import (
    VECTOR_STORE_PATH,
)

# Settings
st.title("Settings")

# Delete button
delete_button = st.button("Delete Vector Store")

if delete_button:
    shutil.rmtree(VECTOR_STORE_PATH)
    st.success("Deleted Vector Store")
    