import streamlit as st
from PIL import Image

st.markdown("# About MONAI")
st.sidebar.markdown("# About MONAI")

st.write("**(Medical Open Network for Artificial Intelligence)**")

image = Image.open('../images/monai_logo.png')
st.image(image, caption='Sunrise by the mountains')

st.write("Project MONAI was originally started by NVIDIA & King’s College London to establish an inclusive community of AI researchers for the development and exchange of best practices for AI in healthcare imaging across academia and enterprise researchers.")

st.write("The MONAI framework is the open-source foundation being created by Project MONAI and it wouldn’t have been possible to accelerate this development without the development of existing toolkits such as Nvidia Clara Train, NiftyNet, DLTK, and DeepNeuro.")

st.write("For more information about MONAI, check out their [website](https://monai.io/) or [GitHub](https://github.com/Project-MONAI)")
