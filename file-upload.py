# https://www.youtube.com/watch?v=oTbbfuH44Gg&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=8

import streamlit as st

st.title("Upload File")
st.markdown("---")
image = st.file_uploader("Please upload an image", type=['png', 'jpg', 'jpeg', 'gif', 'webp'])
if image is not None:
    st.image(image)

images = st.file_uploader("Please upload images", type=['png', 'jpg', 'jpeg', 'gif', 'webp'], accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image)