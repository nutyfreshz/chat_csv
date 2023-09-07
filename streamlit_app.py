import subprocess
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai.llm.openai import OpenAI
from pandasai import PandasAI
import shelve

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# Function to initialize the cache safely
def initialize_cache():
    try:
        cache = shelve.open('/mount/src/chat_csv/cache/cache', writeback=True)
        return cache
    except Exception as e:
        st.error(f"Error initializing the cache: {e}")
        return None

# Function for pandasAI
def chat_with_csv(df, prompt, cache):
    llm = OpenAI(api_key=openai_api_key)
    pandas_ai = PandasAI(llm)
    
    try:
        if cache is None:
            st.warning("Cache initialization failed. Caching disabled.")
            result = pandas_ai.run(df, prompt=prompt)
        else:
            # Check if the prompt is already in the cache
            if prompt in cache:
                st.info("Result retrieved from cache.")
                result = cache[prompt]
            else:
                st.info("Running AI model.")
                result = pandas_ai.run(df, prompt=prompt)
                # Store the result in the cache
                cache[prompt] = result
                cache.sync()  # Ensure data is written to the cache file

        return result
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

st.set_page_config(layout='wide')

st.title('ChatCSV with LLM')

# Initialize the cache
cache = initialize_cache()

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
                result = chat_with_csv(data, input_text, cache)
                if result:
                    st.success(result)
