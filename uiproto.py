import streamlit as st

def set_bg_image(img_path):
  """
  Function to set a background image for the app

  Args:
      img_path (str): Path to the background image file
  """
  st.markdown(
      f"""
      <style>
      .stApp {{
        background-image: url("data:image/png;base64,{base64.b64encode(open({https://foto.wuestenigel.com/wp-content/uploads/api/receipt-on-a-white-background.jpeg}, "rb").read()).decode()});
        background-size: cover;
      }}
      </style>
      """,
      unsafe_allow_html=True,
  )
  
# Set the path to your background image
img_path = "background.jpg"  # Replace with your image path
set_bg_image(https://foto.wuestenigel.com/wp-content/uploads/api/receipt-on-a-white-background.jpeg)
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
  help='Supported file types: JPG, PNG'
)

#tabs
expander1 = st.expander("New AI Chat")
expander2 = st.expander("AI Chat History")

# Add content specific to each expander
with expander1:
  language = st.selectbox("Language", ["English", "Filipino"])
  with st.chat_message("assistant"):
    if language:
      freeform_text = st.text_area(label="What is your question?",max_chars=100)
    if freeform_text:
      response = my_chatbot(language,freeform_text)
      st.write(response['text'] )

    
with expander2:
  st.write("You can see here your AI chat history.")
