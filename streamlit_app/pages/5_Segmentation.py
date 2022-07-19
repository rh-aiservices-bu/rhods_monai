import streamlit as st
from streamlit_option_menu import option_menu

st.markdown("# Segmentaion")
st.sidebar.markdown("# Segmentation")

imtype = option_menu("Select Image Type", ["2D Segmentation", "3D Segmentation"], menu_icon="image",default_index=0)
if imtype == "2D Segmentation": 
    file = st.file_uploader('Upload An Image')
    st.write("For testing purposes, you can select a sample image here")
    st.button("Rerun")

if imtype == "3D Segmentation":
    file = st.file_uploader('Upload An Image')
    st.write("For testing purposes, you can select a sample image here")
    st.button("Rerun")