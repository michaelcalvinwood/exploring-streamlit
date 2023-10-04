# https://www.youtube.com/watch?v=oTbbfuH44Gg&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=11

import streamlit as st

st.markdown("<h1 style='text-align:center'>User Registration</h1>", unsafe_allow_html=True)

# Form Method #1
form=st.form("my_form")
form.text_input("User Name", key="user_name")
form.form_submit_button("Submit")

# Form Method #2
with st.form("other_form"):
    st.text_input("Password", key="user_password")
    st.form_submit_button("Submit")

# Form with Columns
with st.form("third_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    first_name=col1.text_input("First Name", key="user_first_name")
    last_name=col2.text_input("Last Name", key="user_last_name")
    email=st.text_input("Email Address", key="user_email_address")
    st.markdown("Date of Birth")
    day, month, year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    submit_state=st.form_submit_button("Submit")
    if submit_state:
        if first_name == "" or last_name == "":
            st.warning("Please enter a first name and last name")
        else:
            st.success("Logged in!")