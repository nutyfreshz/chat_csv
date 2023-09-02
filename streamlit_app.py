import streamlit as st
import pandas as pd

st.set_page_config(layout = 'wide')

st.title('ChatCSV with LLM')

input_csv = st.file_uploader('Upload your CSV file', type = ['csv'])

if input_csv is not None:
  col1, col2 = st.columns([1,1])

  with col1:
    st.info('CSV Uploaded success fully')
    data = pd.read_csv(input_csv)
    st.DataFrame(data)
