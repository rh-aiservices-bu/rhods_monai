import streamlit as st
from PIL import Image as PILImage

import monai.deploy.core as md
from monai.deploy.core import DataPath, ExecutionContext, Image, InputContext, IOType, Operator, OutputContext


@md.input("image", Image, IOType.IN_MEMORY)
@md.output("image", Image, IOType.DISK)
# If `pip_packages` is specified, the definition will be aggregated with the package dependency list of other
# operators and the application in packaging time.
# @md.env(pip_packages=["scikit-image >= 0.17.2"])
class GaussianOperator(Operator):
    """This Operator implements a smoothening based on Gaussian.
    It ingests a single input and provides a single output.
    """

    def compute(self, op_input: InputContext, op_output: OutputContext, context: ExecutionContext):
        from skimage.filters import gaussian
        from skimage.io import imsave

        data_in = op_input.get().asnumpy()
        data_out = gaussian(data_in, sigma=0.2)
        
        # Display Processed Image
        st.image(data_out, caption="Processed Image", use_column_width=True)

      #  output_folder = op_output.get().path
      #  output_path = output_folder / "final_output.png"
      #  imsave(output_path, data_out)


@md.input("image", Image, IOType.IN_MEMORY)
@md.output("image", Image, IOType.IN_MEMORY)
# If `pip_packages` is specified, the definition will be aggregated with the package dependency list of other
# operators and the application in packaging time.
# @md.env(pip_packages=["scikit-image >= 0.17.2"])
class MedianOperatorBase(Operator):
    """This Operator implements a noise reduction.
    The algorithm is based on the median operator.
    It ingests a single input and provides a single output.
    """

    # Define __init__ method with super().__init__() if you want to override the default behavior.
    def __init__(self):
        super().__init__()
        # Do something

    def compute(self, op_input: InputContext, op_output: OutputContext, context: ExecutionContext):
        print("Executing base operator...")


class MedianOperator(MedianOperatorBase):
    """This operator is a subclass of the base operator to demonstrate the usage of inheritance."""

    # Define __init__ method with super().__init__() if you want to override the default behavior.
    def __init__(self):
        super().__init__()
        # Do something

    def compute(self, op_input: InputContext, op_output: OutputContext, context: ExecutionContext):
        # Execute the base operator's compute method.
        super().compute(op_input, op_output, context)

        from skimage.filters import median
        model = context.models.get()  # a model object that inherits Model class

        if model:  # if model is not a null model
            print(model.items())

        data_in = op_input.get().asnumpy()
        data_out = median(data_in)
        op_output.set(Image(data_out))


@md.output("image", Image, IOType.IN_MEMORY)
class SobelOperator(Operator):
    """This Operator implements a Sobel edge detector.
    It has a single input and single output.
    """

    def compute(self, op_input: InputContext, op_output: OutputContext, context: ExecutionContext):
        from skimage import filters, io
        import numpy as np
        
        image = PILImage.open(file)
        image = image.convert("L")  # convert to greyscale image
        image_arr = np.asarray(image)
        
        data_out = filters.sobel(image_arr)

        op_output.set(Image(data_out))

from monai.deploy.core import Application, env, resource


@resource(cpu=1)
@env(pip_packages=["scikit-image >= 0.17.2"])
class App(Application):
    
    def compose(self):
        sobel_op = SobelOperator()
        median_op = MedianOperator()
        gaussian_op = GaussianOperator()

        self.add_flow(sobel_op, median_op)
        self.add_flow(median_op, gaussian_op)


if __name__ == "__main__":

    st.markdown("# Image Processing")
    st.sidebar.markdown("# Image Processing")

    st.write("The [HIPAA Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/privacy/index.html#:~:text=The%20HIPAA%20Privacy%20Rule&text=The%20Rule%20requires%20appropriate%20safeguards,information%20without%20an%20individual's%20authorization.) protects all individually identifiable health information held or transmitted by a covered entity or its business associate, in any form or media, whether electronic, paper, or oral.")
    st.write("By checking the box below, you certify that any media uploaded is your own or publicly accessible and comply with the HIPAA guidelines")
    agree = st.checkbox("I agree")
    if agree:
        file = st.file_uploader('Upload An Image')
        st.write("For testing purposes, you can select a sample image [here](https://www.kaggle.com/datasets/andrewmvd/medical-mnist)")
        if file:
            img = PILImage.open(file)
            st.image(img, caption = "Uploaded Image", use_column_width=True)
            go = st.button("Click Here to Process")
            if go:
                App(do_run=True)
