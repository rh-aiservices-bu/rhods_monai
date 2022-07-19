import streamlit as st
from streamlit_option_menu import option_menu

st.markdown("# Classification")
st.sidebar.markdown("# Classification")

imtype = option_menu("Select Image Type", ["2D Classification", "3D Classification"], menu_icon="image",default_index=0)
if imtype == "2D Classification": 
    file = st.file_uploader('Upload An Image')
    st.write("For testing purposes, you can select a sample image here")
    st.button("Rerun")

if imtype == "3D Classification":
    file = st.file_uploader('Upload An Image')
    st.write("For testing purposes, you can select a sample image here")
    st.button("Rerun")