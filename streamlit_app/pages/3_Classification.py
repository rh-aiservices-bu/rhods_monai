import streamlit as st
from streamlit_option_menu import option_menu
from typing import Text

import monai.deploy.core as md
from monai.deploy.core import (
    Application,
    DataPath,
    ExecutionContext,
    Image,
    InputContext,
    IOType,
    Operator,
    OutputContext,
)
from monai.transforms import AddChannel, Compose, EnsureType, ScaleIntensity

MEDNIST_CLASSES = ["AbdomenCT", "BreastMRI", "CXR", "ChestCT", "Hand", "HeadCT"]

@md.output("image", Image, IOType.IN_MEMORY)
@md.env(pip_packages=["pillow"])
class LoadPILOperator(Operator):
    """Load image from the given input (DataPath) and set numpy array to the output (Image)."""

    def compute(self, op_input, op_output: OutputContext, context: ExecutionContext):
        import numpy as np
        from PIL import Image as PILImage

        image = PILImage.open(file)
        image = image.convert("L")  # convert to greyscale image
        image_arr = np.asarray(image)

        output_image = Image(image_arr)  # create Image domain object with a numpy array
        op_output.set(output_image)


@md.input("image", Image, IOType.IN_MEMORY)
@md.output("result_text", Text, IOType.IN_MEMORY)
@md.env(pip_packages=["monai"])
class MedNISTClassifierOperator(Operator):
    """Classifies the given image and returns the class name."""

    @property
    def transform(self):
        return Compose([AddChannel(), ScaleIntensity(), EnsureType()])

    def compute(self, op_input: InputContext, op_output: OutputContext, context: ExecutionContext):

        import torch
        from torch import jit

        img = op_input.get().asnumpy()  # (64, 64), uint8
        image_tensor = self.transform(img)  # (1, 64, 64), torch.float64
        image_tensor = image_tensor[None].float()  # (1, 1, 64, 64), torch.float32
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        image_tensor = image_tensor.to(device)
        model = context.models.get()  # get a TorchScriptModel object
        model = jit.load("/opt/app-root/src/rhods_monai/streamlit_app/models/classifier.zip")

        with torch.no_grad():
            outputs = model(image_tensor)

        _, output_classes = outputs.max(dim=1)
        print(outputs)
        result = MEDNIST_CLASSES[output_classes[0]]  # get the class name
        print(result)
        st.write("Your image was classified as:", result)


@md.resource(cpu=1, gpu=1, memory="2Gi")
class App(Application):
    """Application class for the MedNIST classifier."""

    def compose(self):
        load_pil_op = LoadPILOperator()
        classifier_op = MedNISTClassifierOperator()
        self.add_flow(load_pil_op, classifier_op)


if __name__ == "__main__":   
    from PIL import Image as PILImage
    st.markdown("# Classification")
    st.sidebar.markdown("# Classification")
    st.sidebar.write("Uploaded image will be classified as one of the following:")
    st.sidebar.write("AbdomenCT") 
    st.sidebar.write("BreastMRI") 
    st.sidebar.write("CXR")
    st.sidebar.write("ChestCT")
    st.sidebar.write("Hand") 
    st.sidebar.write("HeadCT")

    st.write("The [HIPAA Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/privacy/index.html#:~:text=The%20HIPAA%20Privacy%20Rule&text=The%20Rule%20requires%20appropriate%20safeguards,information%20without%20an%20individual's%20authorization.) protects all individually identifiable health information held or transmitted by a covered entity or its business associate, in any form or media, whether electronic, paper, or oral.")
    st.write("By checking the box below, you certify that any media uploaded is your own or publicly accessible and comply with the HIPAA guidelines")
    agree = st.checkbox("I agree")
    if agree:
            file = st.file_uploader('Upload An Image')
            st.write("For testing purposes, you can select a sample image [here](https://www.kaggle.com/datasets/andrewmvd/medical-mnist)")
            if file:
                img = PILImage.open(file)
                st.image(img, use_column_width=True)
                if st.button("Click Here to Classify"):
                    App(do_run=True)
               # app = App()
                #app.run(input="input", output="output", model="/opt/app-root/src/rhods_monai/streamlit_app/models/classifier.zip")
