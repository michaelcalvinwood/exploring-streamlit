# https://www.youtube.com/watch?v=oTbbfuH44Gg&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=11

import streamlit as st

st.markdown("<h1>User Registration</h1>", unsafe_allow_html=True)

# Form Method #1
form=st.form("my_form")
form.text_input("User Name", key="user_name")
form.form_submit_button("Submit")

# Form Method #2
with st.form("other_form"):
    st.text_input("Password", key="user_password")
    st.form_submit_button("Submit")

# Form with Columns
with st.form("third_form"):
    col1, col2 = st.columns(2)
    col1.text_input("First Name", key="user_first_name")
    col2.text_input("Last Name", key="user_last_name")
    st.text_input("Email Address", key="user_email_address")
    st.form_submit_button("Submit")