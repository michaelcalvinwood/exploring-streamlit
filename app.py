# https://www.youtube.com/watch?v=oTbbfuH44Gg&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=8

import streamlit as st

test_me = "US"
def cats_clicked():
    print('cats state', st.session_state["cats"])

def radio_clicked():
    print("radio", st.session_state["radio"])

def buttonClicked():
    global test_me
    print("button clicked")
    test_me = "hello"

def selected_car():
    print("selected car", st.session_state["favorite_car"])

def selected_car2():
    print("selected car2", st.session_state["favorite_car2"])


st.checkbox("Cats", key="cats", on_change=cats_clicked)

radio = st.radio("Select One", options=("US", "UK", "Canada"), key="radio", on_change=radio_clicked)
st.button("Click Me", on_click=buttonClicked)

select=st.selectbox("What is your favorite car?",
                    options=("Audi", "BMW", "Mercedes", "Toyota"),
                    key="favorite_car",
                    on_change=selected_car)

multi_select=st.multiselect("What is your favorite car?",
                    options=("Audi", "BMW", "Mercedes", "Toyota"),
                    key="favorite_car2",
                    on_change=selected_car2)