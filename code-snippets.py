import streamlit as st

json={"a": [1, 2, 3], "b": [4, 5, 6]}
st.json(json)

st.code("""
print("hello World")
x = 5
print("x", x)
""", language="python")
