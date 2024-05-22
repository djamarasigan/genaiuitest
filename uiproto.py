import streamlit as st

>>> tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
>>> tab1.write("this is tab 1")
>>> tab2.write("this is tab 2")

st.write("")

st.header('resi-bot')
st.subheader('a multilingual receipt scanner')
st.text('a protype made by Team Sentient')

st.write("")

st.file_uploader(
  'Upload Button',
  help='Upload here your receipts.'
)
