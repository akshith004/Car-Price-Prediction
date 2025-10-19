import streamlit as st

st.title("Hello How are you")
st.write("What are you doing right there")
name = st.text_input("Enter your name")
if st.button("namaste"):
    st.success(f'Hello {name}')