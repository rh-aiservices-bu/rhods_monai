FROM quay.io/guimou/s2i-monai-notebook:latest

EXPOSE 8080

RUN pip install monai-deploy-app-sdk streamlit-option-menu

COPY streamlit_app /opt/app-root/src/rhods_monai/streamlit_app

CMD streamlit run rhods_monai/streamlit_app/RHODS_x_MONAI.py --server.port 8080 --server.headless true --server.address 0.0.0.0