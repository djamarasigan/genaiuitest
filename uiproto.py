import streamlit as st
import numpy as np
from openai import OpenAI

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
  st.write("Chat with AI for assistance.")
  prompt = st.chat_input("Say something")
    if prompt:
      st.write(f{prompt}")
    
with expander2:
  st.write("You can see here your AI chat history.")
