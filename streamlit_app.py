import streamlit as st
import pandas as pd

st.title('ChatcSV with LLM')

input_csv = st.file_uploader('Upload your CSV file', type = ['csv'])

if input_csv is not None:
  pass
