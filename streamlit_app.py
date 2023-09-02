import streamlit as st
import pandas as pd

st.set_page_config(layout = 'wide')

st.title('ChatCSV with LLM')

input_csv = st.file_uploader('Upload your CSV file', type = ['csv'])

if input_csv is not None:
  pass
