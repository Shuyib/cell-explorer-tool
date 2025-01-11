import streamlit as st
from PIL import Image, ImageEnhance
import pandas as pd
import numpy as np
import io
import os

def zoom_at(img, x, y, zoom):
    w, h = img.size
    zoom2 = zoom * 2
    img = img.crop((x - w / zoom2, y - h / zoom2,
                    x + w / zoom2, y + h / zoom2))
    return img.resize((w, h), Image.LANCZOS)

st.title("Cell Explorer")

uploaded_files = st.file_uploader("Upload Images", accept_multiple_files=True, type="jpg")

if uploaded_files:
    img_index = st.selectbox("Select Image", range(len(uploaded_files)))
    x = st.slider("X Coordinate", 0, 500, 205)
    y = st.slider("Y Coordinate", 0, 500, 250)
    zoom = st.slider("Zoom", 1, 10, 5)
    contrast = st.slider("Contrast", 0.0, 5.0, 1.0)
    brightness = st.slider("Brightness", 0.0, 5.0, 1.0)
    sharpness = st.slider("Sharpness", 0.0, 2.0, 1.0)
    save_image = st.checkbox("Save Image")

    img_data = uploaded_files[img_index].read()
    img = Image.open(io.BytesIO(img_data)).resize((500, 500))
    img_zoomed = zoom_at(img, x, y, zoom)
    img_contrast = ImageEnhance.Contrast(img_zoomed).enhance(contrast)
    img_bright = ImageEnhance.Brightness(img_contrast).enhance(brightness)
    img_sharp = ImageEnhance.Sharpness(img_bright).enhance(sharpness)

    if save_image:
        img_sharp.save("image-processed.jpg")
        st.success("Image saved as image-processed.jpg")

    st.image(img_sharp, caption="Processed Image", use_column_width=True)

    description = st.text_area("Describe the image", "")
    if st.button("Save Description"):
        with open("saved_image_description.txt", "w") as f:
            f.write(description)
        st.success("Description saved as saved_image_description.txt")

    if st.button("Save Image Parameters"):
        params = {
            "coordinates_x": x,
            "coordinates_y": y,
            "zoom": zoom,
            "contrast": contrast,
            "brightness": brightness,
            "sharpness": sharpness
        }
        with open("saved_image_parameters.json", "w") as f:
            f.write(pd.DataFrame([params]).to_json(orient="records"))
        st.success("Image parameters saved as saved_image_parameters.json")

    if st.button("Rename Files"):
        file_ext = str(np.random.randint(100))
        os.rename("image-processed.jpg", f"img_processed{file_ext}.jpg")
        os.rename("saved_image_parameters.json", f"saved_image_parameters{file_ext}.json")
        os.rename("saved_image_description.txt", f"saved_image_description{file_ext}.txt")
        st.success("Files renamed successfully")
