import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.markdown("# Segmentaion")
st.sidebar.markdown("# Segmentation")

imtype = option_menu("Select Target", ["Liver Tumor", "Spleen", "Lung"], menu_icon="image",default_index=0)
if imtype == "Liver Tumor":
    file = st.file_uploader('Upload An Image')
    st.write("For testing purposes, you can select a sample image [here](https://www.kaggle.com/datasets/andrewmvd/medical-mnist)")
    if file:
        img = Image.open(file)
        st.image(img, use_column_width=True)
        st.button("Click Here to Segment")

if imtype == "Spleen":
    file = st.file_uploader('Upload An Image')
    st.write("For testing purposes, you can select a sample image [here](https://www.kaggle.com/datasets/andrewmvd/medical-mnist)")
    if file:
        img = Image.open(file)
        st.image(img, use_column_width=True)
        st.button("Click Here to Segment")

if imtype == "Lung":
    file = st.file_uploader('Upload An Image')
    st.write("For testing purposes, you can select a sample image [here](https://www.kaggle.com/datasets/andrewmvd/medical-mnist)")
    if file:
        img = Image.open(file)
        st.image(img, use_column_width=True)
        st.button("Click Here to Segment")

