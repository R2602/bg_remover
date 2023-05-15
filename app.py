import streamlit as st
from PIL import Image
import rembg

# Create a file upload widget
file = st.file_uploader("Upload an image file")

# If the user uploaded an image file
if file is not None:

    # Get the image file
    image = file.read()

    # Display the image file
    st.image(image)

    # Remove the background from the image
    img_bg_removed = rembg.remove(image)

    # Display the image with the background removed
    st.image(img_bg_removed)
