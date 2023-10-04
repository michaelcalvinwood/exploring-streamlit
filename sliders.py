import streamlit as st

def slider_val():
    print(st.session_state["my_slider"])

val = st.slider('Slider', min_value=0, max_value=100, step=5, on_change=slider_val, key="my_slider")
