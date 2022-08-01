import streamlit as st

st.markdown("# Image Processing")
st.sidebar.markdown("# Image Processing")

file = st.file_uploader('Upload An Image')
st.write("For testing purposes, you can select a sample image [here](https://www.kaggle.com/datasets/andrewmvd/medical-mnist)")
if file:
    img = PILImage.open(file)
    st.image(img, use_column_width=True)
    st.button("Click Here to Process")
