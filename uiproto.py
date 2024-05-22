import streamlit as st
import numpy as np

#space
st.write("")

#headers
st.header('resi-bot')
st.subheader('a multilingual receipt scanner')
st.text('a protype made by Team Sentient')

#space
st.write("")

#upload button
st.file_uploader(
  'Upload Button',
  help='Upload here your receipts.'
)

# Create expanders with titles like tabs
expander1 = st.expander("New AI Chat")
expander2 = st.expander("AI Chat History")

# Add content specific to each expander
with expander1:
  with st.chat_message("user"):
    st.write("How may I assist you?")

# Display a chat input widget at the bottom of the app.
    st.chat_input("Say something")

with expander2:
  st.write("Data analysis and visualizations here.")
