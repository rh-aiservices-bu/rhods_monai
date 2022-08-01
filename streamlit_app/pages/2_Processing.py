import streamlit as st
from PIL import Image

st.markdown("# Image Processing")
st.sidebar.markdown("# Image Processing")

file = st.file_uploader('Upload An Image')
st.write("For testing purposes, you can select a sample image [here](https://www.kaggle.com/datasets/andrewmvd/medical-mnist)")
if file:
    img = Image.open(file)
    st.image(img, use_column_width=True)
    st.button("Click Here to Process")
