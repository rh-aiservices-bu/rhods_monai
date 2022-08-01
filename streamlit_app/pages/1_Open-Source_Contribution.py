import streamlit as st

st.markdown("# Open-Source Contribution")
st.sidebar.markdown("# Open-Source Contribution")

st.header("Contribute via GitHub:")
st.write("Learn about the contribution process and guidelines here:")
st.write("Project MONAI [GitHub](https://github.com/Project-MONAI/MONAI/blob/dev/CONTRIBUTING.md)")
st.write("RHODS (this project) [GitHub](https://github.com/rh-aiservices-bu/rhods_monai)")
st.header("Or contribute here by sharing your medical images:")
file = st.file_uploader('Upload An Image')
st.write("Insert HIPAA disclaimer here")
agree = st.checkbox("I agree")
if agree:
     st.write("Great! We thank you for your contribution to open-source research!")