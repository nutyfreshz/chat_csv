import subprocess
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai.llm.openai import OpenAI
from pandasai import PandasAI
import shelve
import time

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

def initialize_cache():
    try:
        cache = shelve.open('/mount/src/chat_csv/cache/cache', writeback=True)
        return cache
    except Exception as e:
        st.error(f"Error initializing the cache: {e}")
        return None

def chat_with_csv(df, prompt, cache):
    llm = OpenAI(api_key=openai_api_key)
    pandas_ai = PandasAI(llm)
    
    def cache_operation():
        if cache is None:
            st.warning("Cache initialization failed. Caching disabled.")
            return pandas_ai.run(df, prompt=prompt)
        elif prompt in cache:
            st.info("Result retrieved from cache.")
            return cache[prompt]
        else:
            st.info("Running AI model.")
            result = pandas_ai.run(df, prompt=prompt)
            cache[prompt] = result
            cache.sync()
            return result

    return retry(cache_operation)

def retry(func, max_retries=3):
    for i in range(max_retries):
        try:
            result = func()
            return result
        except Exception as e:
            st.warning(f"Retry attempt {i + 1}: {e}")
            time.sleep(1)  # Wait for 1 second before retrying
    return None

st.set_page_config(layout='wide')

st.title('ChatCSV with LLM')

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
