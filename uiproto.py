import streamlit as st

st.image("https://i.imgur.com/SqyF5E3.png")


#headers
st.header('resi-bot')
st.subheader('a multilingual receipt scanner')
st.text('a protype made by Team Sentient')

#space
st.write("")

#upload button
st.file_uploader(
  'Upload Button',
  help='Supported file types: JPG, PNG'
)

#tabs
expander1 = st.expander("New AI Chat")
expander2 = st.expander("AI Chat History")

# Add content specific to each expander
with expander1:
  language = st.selectbox("Select Language", ["English", "Filipino"])
  with st.chat_message("assistant"):
    if language:
      freeform_text = st.text_area(label="What is your question?",max_chars=100)
    if freeform_text:
      response = my_chatbot(language,freeform_text)
      st.write(response['text'] )

    
with expander2:
  st.write("You can see here your AI chat history.")
