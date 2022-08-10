import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

import SimpleITK as sitk
import nibabel as nib
from nilearn import plotting, image

st.markdown("# Segmentaion")
st.sidebar.markdown("# Segmentation")

imtype = option_menu("Select Target", ["Liver Tumor", "Spleen", "Lung"], menu_icon="image",default_index=0)
if imtype == "Liver Tumor":
    st.write("The [HIPAA Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/privacy/index.html#:~:text=The%20HIPAA%20Privacy%20Rule&text=The%20Rule%20requires%20appropriate%20safeguards,information%20without%20an%20individual's%20authorization.) protects all individually identifiable health information held or transmitted by a covered entity or its business associate, in any form or media, whether electronic, paper, or oral.")
    st.write("By checking the box below, you certify that any media uploaded is your own or publicly accessible and comply with the HIPAA guidelines")
    agree = st.checkbox("I agree")
    if agree:
        file = st.file_uploader('Upload An Image')
        st.write("For testing purposes, you can select a sample image [here](https://www.kaggle.com/datasets/andrewmvd/medical-mnist)")
        if file:
            img = Image.open(file)
            st.image(img, use_column_width=True)
            st.button("Click Here to Segment")

if imtype == "Spleen":
    st.write("The [HIPAA Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/privacy/index.html#:~:text=The%20HIPAA%20Privacy%20Rule&text=The%20Rule%20requires%20appropriate%20safeguards,information%20without%20an%20individual's%20authorization.) protects all individually identifiable health information held or transmitted by a covered entity or its business associate, in any form or media, whether electronic, paper, or oral.")
    st.write("By checking the box below, you certify that any media uploaded is your own or publicly accessible and comply with the HIPAA guidelines")
    agree = st.checkbox("I agree")
    if agree:
        file = st.file_uploader('Upload A 3D Image (dcm)', accept_multiple_files=True)
        st.write("For testing purposes, you can select a sample image [here](https://www.kaggle.com/datasets/andrewmvd/medical-mnist)")
        if file:
            st.button("Click Here to Segment")

if imtype == "Lung":
    st.write("The [HIPAA Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/privacy/index.html#:~:text=The%20HIPAA%20Privacy%20Rule&text=The%20Rule%20requires%20appropriate%20safeguards,information%20without%20an%20individual's%20authorization.) protects all individually identifiable health information held or transmitted by a covered entity or its business associate, in any form or media, whether electronic, paper, or oral.")
    st.write("By checking the box below, you certify that any media uploaded is your own or publicly accessible and comply with the HIPAA guidelines")
    agree = st.checkbox("I agree")
    if agree:
        file = st.file_uploader('Upload An Image')
        st.write("For testing purposes, you can select a sample image [here](https://www.kaggle.com/datasets/andrewmvd/medical-mnist)")
        if file:
            img = Image.open(file)
            st.image(img, use_column_width=True)
            st.button("Click Here to Segment")

