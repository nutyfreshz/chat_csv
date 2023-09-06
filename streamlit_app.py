!pip install dotenv

import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai.llm.openai import OpenAI
from pandasai import PandasAI

load_dotenv()

openai_api = os.getenv('OOENAI_API_KEY')

#Function for pandasAI
def chat_with_csv(df, prompt):
  llm = OpenAI()
  pandas_ai = PandasAI(llm)
  result = pandas_ai.run(df, prompt = prompt)
  print(result)
  return result

st.set_page_config(layout = 'wide')

st.title('ChatCSV with LLM')

input_csv = st.file_uploader('Upload your CSV file', type = ['csv'])

if input_csv is not None:
  col1, col2 = st.columns([1,1])

  with col1:
    st.info('CSV Uploaded success fully')
    data = pd.read_csv(input_csv)
    st.dataframe(data)

  with col2:
    st.info('Chat with your CSV')

    input_text = st.text_area('Enter your query')
    if input_text is not None:
      if st.button('Chat with CSV'):
          st.info('Your Query: ' + input_text)
          result = chat_with_csv(data, input_text)
          st.success(result)
