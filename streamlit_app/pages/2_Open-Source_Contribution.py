import streamlit as st

st.markdown("# Open-Source Contribution")
st.sidebar.markdown("# Open-Source Contribution")

st.header("\faIcon{github} Contribute via GitHub:")
st.write("Learn about the contribution process and guidelines here:")
st.write("[MONAI/CONTRIBUTING](https://github.com/Project-MONAI/MONAI/blob/dev/CONTRIBUTING.md)")
st.header("Or contribute here:")
file = st.file_uploader('Upload An Image')