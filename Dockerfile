FROM quay.io/guimou/s2i-monai-notebook-ubi9-py39:0.1.0

EXPOSE 8080

COPY streamlit_app /opt/app-root/src/rhods_monai/streamlit_app

CMD streamlit run rhods_monai/streamlit_app/RHODS_x_MONAI.py --server.port 8080 --server.headless true --server.address 0.0.0.0