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
  st.title("ChatGPT-like clone")

  client = OpenAI(api_key=st.secrets["sk-proj-Eq8r0p04kHoAbLjStep8T3BlbkFJr8JyNTd4kEmIyJDsJqwR"])
  
  if "openai_model" not in st.session_state:
      st.session_state["openai_model"] = "gpt-3.5-turbo"
  
  if "messages" not in st.session_state:
      st.session_state.messages = []
  
  for message in st.session_state.messages:
      with st.chat_message(message["role"]):
          st.markdown(message["content"])
  
  if prompt := st.chat_input("What is up?"):
      st.session_state.messages.append({"role": "user", "content": prompt})
      with st.chat_message("user"):
          st.markdown(prompt)
  
      with st.chat_message("assistant"):
          stream = client.chat.completions.create(
              model=st.session_state["openai_model"],
              messages=[
                  {"role": m["role"], "content": m["content"]}
                  for m in st.session_state.messages
              ],
              stream=True,
          )
          response = st.write_stream(stream)
      st.session_state.messages.append({"role": "assistant", "content": response})
    
with expander2:
  st.write("Data analysis and visualizations here.")
