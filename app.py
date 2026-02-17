import streamlit as st
from agent import get_response

st.set_page_config(page_title="AI Banking Agent")

st.title("🏦 AI Banking Customer Support")

query = st.text_input("Ask your banking question:")

if st.button("Submit"):
    if query:
        answer = get_response(query)
        st.success(answer)
    else:
        st.warning("Please enter a question")
