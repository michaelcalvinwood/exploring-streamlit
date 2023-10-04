import streamlit as st


name = st.text_input("My name", key="user_name", max_chars=60)

bio = st.text_area("My bio", key="user_bio")
