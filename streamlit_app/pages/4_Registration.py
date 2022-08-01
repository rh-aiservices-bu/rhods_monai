import streamlit as st
from streamlit_option_menu import option_menu

st.markdown("# Registration")
st.sidebar.markdown("# Registration")

imtype = option_menu("Select Image Type", ["2D Registration", "3D Registration"], menu_icon="image",default_index=0)
if imtype == "2D Registration": 
    file = st.file_uploader('Upload An Image')
    st.write("For testing purposes, you can select a sample image [here](https://www.kaggle.com/datasets/andrewmvd/medical-mnist)")
    st.button("Rerun")

if imtype == "3D Registration":
    file = st.file_uploader('Upload An Image')
    st.write("For testing purposes, you can select a sample image [here](https://www.kaggle.com/datasets/andrewmvd/medical-mnist)")
    st.button("Rerun")