import subprocess
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai.llm.openai import OpenAI
from pandasai import PandasAI
import shelve

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

def chat_with_csv(df, prompt):
    try:
        llm = OpenAI(api_token=openai_api_key)
        pandas_ai = PandasAI(llm)
        result = pandas_ai.run(df, prompt=prompt)
        return result
    except Exception as e:
        return str(e)

# ... rest of your code ...

# Specify a different database backend (e.g., 'dbm.gnu' or 'dbm.dumb')
db_backend = 'dbm.gnu'  # You can try other backends as well

# Open the shelve database with the specified backend
with shelve.open('mydata.db', 'c', protocol=4, writeback=True, flag='n', backend=db_backend) as db:
    # Perform operations on the database
