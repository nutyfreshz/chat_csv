import streamlit as st
import pandas as pd
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

st.title('ChatCSV with LLM')

# Authenticate with Google Drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Authenticates using a local webserver

drive = GoogleDrive(gauth)

# Create a function to upload the CSV from Google Drive
def upload_csv_from_google_drive():
    st.subheader('Upload CSV from Google Drive')
    drive_url = st.text_input('Enter the Google Drive shareable link for the CSV file:')
    if drive_url:
        try:
            # Extract the file ID from the shareable link
            file_id = drive_url.split("/")[-2]
            
            # Get the file
            file = drive.CreateFile({'id': file_id})
            file.GetContentFile('uploaded_csv.csv')

            st.success('CSV file downloaded successfully!')

            # Read the CSV and display it
            df = pd.read_csv('uploaded_csv.csv')
            st.dataframe(df)

        except Exception as e:
            st.error(f'Error: {str(e)}')

# Display the CSV upload widget
upload_csv_from_google_drive()
# input_csv = st.file_uploader('Upload your CSV file', type = ['csv'])

# if input_csv is not None:
#   pass
