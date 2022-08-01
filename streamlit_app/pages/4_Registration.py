import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.markdown("# Registration")
st.sidebar.markdown("# Registration")

imtype = option_menu("Select Image Type", ["2D Registration", "3D Registration"], menu_icon="image",default_index=0)
if imtype == "2D Registration": 
    file = st.file_uploader('Upload An Image')
    st.write("For testing purposes, you can select a sample image [here](https://www.kaggle.com/datasets/andrewmvd/medical-mnist)")
    if file:
        img = Image.open(file)
        st.image(img, use_column_width=True)
        st.button("Click Here to Register")

if imtype == "3D Registration":
    file = st.file_uploader('Upload An Image')
    st.write("For testing purposes, you can select a sample image [here](https://www.kaggle.com/datasets/andrewmvd/medical-mnist)")
    if file:
        img = Image.open(file)
        st.image(img, use_column_width=True)
        st.button("Click Here to Register")