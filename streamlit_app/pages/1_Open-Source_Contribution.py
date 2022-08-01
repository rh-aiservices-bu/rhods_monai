import streamlit as st

st.markdown("# Open-Source Contribution")
st.sidebar.markdown("# Open-Source Contribution")

st.header("Contribute via GitHub:")
st.write("Learn about the contribution process and guidelines here:")
st.write("Project MONAI [GitHub](https://github.com/Project-MONAI/MONAI/blob/dev/CONTRIBUTING.md)")
st.write("RHODS (this project) [GitHub](https://github.com/rh-aiservices-bu/rhods_monai)")
st.header("Or contribute here by sharing your medical images:")
st.write("The [HIPAA Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/privacy/index.html#:~:text=The%20HIPAA%20Privacy%20Rule&text=The%20Rule%20requires%20appropriate%20safeguards,information%20without%20an%20individual's%20authorization.) protects all individually identifiable health information held or transmitted by a covered entity or its business associate, in any form or media, whether electronic, paper, or oral.")
st.write("By checking the box below, you certify that any media uploaded is your own or publicly accessible and comply with the HIPAA guidelines")
agree = st.checkbox("I agree")
if agree:
    file = st.file_uploader('Upload An Image')
    st.write("Great! We thank you for your contribution to open-source research!")