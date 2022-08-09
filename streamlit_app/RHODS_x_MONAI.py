import streamlit as st
import webbrowser

st.markdown("# RHODS x MONAI")
st.sidebar.markdown("# RHODS x MONAI")

st.write("This application was developed, packaged, and deployed using RHODS (Red Hat OpenShift Data Science) services with the goal of showcasing the development capabilities that RHODS provides.")
st.write("The MONAI (Medical Open Network for Artificial Intelligence) framework was implemented within the application, adding tools such as Medical Image Processing, Classification, and Segmentation.")

st.write("### Feedback")
st.write("Please consider sharing your feedback via the form below. All suggestions are welcome and appreciated!")
st.button("Feedback Form")

st.write("### Source Code")
st.write("This is an open source project. All source code and documentation can be found on GitHub.")
if st.button("GitHub Repo"): 
  webbrowser.open_new_tab('https://github.com/rh-aiservices-bu/rhods_monai.git')
