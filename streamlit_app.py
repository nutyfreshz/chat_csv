import subprocess
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai.llm.openai import OpenAI
from pandasai import PandasAI
import shelve  # Add the shelve import

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
