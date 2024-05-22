import streamlit as st

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
expander1 = st.expander("Tab 1: Introduction")
expander2 = st.expander("Tab 2: Data Analysis")
expander3 = st.expander("Tab 3: Conclusion")

# Add content specific to each expander
with expander1:
    st.write("Content for the introduction section.")

with expander2:
    st.write("Data analysis and visualizations here.")

with expander3:
    st.write("Summary and concluding remarks.")
