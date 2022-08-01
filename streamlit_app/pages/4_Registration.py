import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.markdown("# Registration")
st.sidebar.markdown("# Registration")

st.write("The [HIPAA Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/privacy/index.html#:~:text=The%20HIPAA%20Privacy%20Rule&text=The%20Rule%20requires%20appropriate%20safeguards,information%20without%20an%20individual's%20authorization.) protects all individually identifiable health information held or transmitted by a covered entity or its business associate, in any form or media, whether electronic, paper, or oral.")
st.write("By checking the box below, you certify that any media uploaded is your own or publicly accessible and comply with the HIPAA guidelines")
agree = st.checkbox("I agree")
if agree:
    file = st.file_uploader('Upload An Image')
    st.write("For testing purposes, you can select a sample image [here](https://www.kaggle.com/datasets/andrewmvd/medical-mnist)")
    if file:
        img = Image.open(file)
        st.image(img, use_column_width=True)
        st.button("Click Here to Register")
