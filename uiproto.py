import streamlit as st

st.header('resi-bot')
st.subheader('a multilingual receipt scanner')
st.text('a protype made by Team Sentient')
        
st.file_uploader(
  'Upload Button',
  help='Upload here your receipts.'
)
