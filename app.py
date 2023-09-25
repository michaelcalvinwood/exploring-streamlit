import streamlit as st

st.title("I am a Title")
st.header("I am a Header")
st.subheader("I am a Subheading")
st.text("I am text.")

st.markdown("### I am *Markdown*.")
st.markdown(">This is a markdown block quote.")
st.markdown(">>This is a nested markdown block quote.")

st.markdown("[Google](https://google.com)")

st.markdown("""
            1. One
            2. Two
            3. Three""")
st.markdown("""
            - b1
            - b2
            - b3
            """)

st.markdown("That is a joyful emoji :joy:")

json={"a": [1, 2, 3], "b": [4, 5, 6]}
st.json(json)

st.code("""
print("hello World")
x = 5
print("x", x)
""", language="python")
