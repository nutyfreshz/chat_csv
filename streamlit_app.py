import subprocess
# Use subprocess to run the pip install command
subprocess.call(["pip", "install", "-r", "requirements.txt"])

import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai.llm.openai import OpenAI
from pandasai import PandasAI

load_dotenv()
# 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
openai_api_key = os.getenv('OPENAI_API_KEY')

# Function for pandasAI
def chat_with_csv(df, prompt):
    llm = OpenAI(api_key=openai_api_key)  # Pass your API key here
    pandas_ai = PandasAI(llm)
    result = pandas_ai.run(df, prompt=prompt)
    return result

st.set_page_config(layout='wide')

st.title('ChatCSV with LLM')

input_csv = st.file_uploader('Upload your CSV file', type=['csv'])

if input_csv is not None:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.info('CSV Uploaded successfully')
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
