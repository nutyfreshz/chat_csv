import streamlit as st
import pandas as pd
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

st.title('ChatCSV with LLM')

input_csv = st.file_uploader('Upload your CSV file', type = ['csv'])

if input_csv is not None:
  pass
