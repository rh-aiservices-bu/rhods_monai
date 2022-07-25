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
from monai.deploy.operators.dicom_text_sr_writer_operator import DICOMTextSRWriterOperator, EquipmentInfo, ModelInfo
from monai.transforms import AddChannel, Compose, EnsureType, ScaleIntensity

MEDNIST_CLASSES = ["AbdomenCT", "BreastMRI", "CXR", "ChestCT", "Hand", "HeadCT"]


@md.input("image", Image, IOType.IN_MEMORY)
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
        import json

        import torch
        
        img = PILImage.open(file)
        image = np.asarray(img)/255
        image = resize(image, (64,64)) # (64, 64), uint8
        image_tensor = self.transform(image)  # (1, 64, 64), torch.float64
        image_tensor = image_tensor[None].float()  # (1, 1, 64, 64), torch.float32

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        image_tensor = image_tensor.to(device)

        model = context.models.get()  # get a TorchScriptModel object

        with torch.no_grad():
            outputs = model(image_tensor)

        _, output_classes = outputs.max(dim=1)

        result = MEDNIST_CLASSES[output_classes[0]]  # get the class name
        print(result)
        op_output.set(result, "result_text")

        # Get output (folder) path and create the folder if not exists
        # The following gets the App context's output path, instead the operator's.
        output_folder = context.output.get().path
        output_folder.mkdir(parents=True, exist_ok=True)

        # Write result to "output.json"
        output_path = output_folder / "output.json"
        with open(output_path, "w") as fp:
            json.dump(result, fp)


@md.resource(cpu=1, gpu=1, memory="1Gi")
class App(Application):
    """Application class for the MedNIST classifier."""

    def compose(self):
        load_pil_op = LoadPILOperator()
        classifier_op = MedNISTClassifierOperator()

        my_model_info = ModelInfo("MONAI WG Trainer", "MEDNIST Classifier", "0.1", "xyz")
        my_equipment = EquipmentInfo(manufacturer="MOANI Deploy App SDK", manufacturer_model="DICOM SR Writer")
        my_special_tags = {"SeriesDescription": "Not for clinical use. The result is for research use only."}
        dicom_sr_operator = DICOMTextSRWriterOperator(
            copy_tags=False, model_info=my_model_info, equipment_info=my_equipment, custom_tags=my_special_tags
        )

        self.add_flow(load_pil_op, classifier_op)
        self.add_flow(classifier_op, dicom_sr_operator, {"result_text": "classification_result"})


if __name__ == "__main__":   
    import numpy as np
    from PIL import Image as PILImage
    st.markdown("# Classification")
    st.sidebar.markdown("# Classification")

    imtype = option_menu("Select Image Type", ["2D Classification", "3D Classification"], menu_icon="image",default_index=0)
    if imtype == "2D Classification": 
        file = st.file_uploader('Upload An Image')
        st.write("For testing purposes, you can select a sample image here")
        if file:
            img = PILImage.open(file)
            st.image(img, use_column_width=True)
            if st.button("Click Here to Classify"):
                App(do_run=True)


if imtype == "3D Classification":
    file = st.file_uploader('Upload An Image')
    image = PILImage.open(file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("For testing purposes, you can select a sample image here")
    st.button("Rerun")
    