import streamlit as st
import pandas as pd
import numpy as np
import requests
from PIL import Image
from PIL.ImageOps import exif_transpose
import time
import base64
import io

### Config
st.set_page_config(
    page_title="Which bug ?",
    page_icon="",
    layout="wide"
)

st.image("Zydoprion.jpg",caption="Zydodo")

def photos_uploader(): 
    # Displays a file uploader to upload a photo of the insect
    img_file = st.file_uploader("Upload a photo of your insect:")
    
    if img_file is not None:
        # Display the preview of the uploaded photo
        img = Image.open(img_file)
        st.image(img, width=50)

    return img_file




### App
st.title("Recognize which insect it is ! 🎨")

st.markdown("""
    Welcome to this awesome `streamlit` dashboard. This is our demo app to recognize insects. 
    
    You just need to upload a photo and we'll figure out which insect it is. 
    
    You can download the whole code here 👉 [Source code](à remplir)
""")


st.markdown("---")

### Input data 
st.subheader("Input data")
st.markdown("""
    As a final note, you can use data that a user will insert when he/she interacts with your app.
    This is called *input data*. To collect these, you can do two things:
    * [Use any of the input widget](https://docs.streamlit.io/library/api-reference/widgets)
    * [Build a form](https://docs.streamlit.io/library/api-reference/control-flow/st.form)

    Depending on what you need to do, you will prefer one or the other. With a `form`, you actually group
    input widgets together and send the data right away, which can be useful when you need to filter
    by several variables.

""")

if __name__ == '__main__':
    # GETTING PHOTOS AND TEXT AS INPUTS
    st.markdown("##### Let's BUG it !")
    img_file = photos_uploader()
    submit_photos = st.button("Submit photos")
    if submit_photos and img_file is not None:
        st.session_state = np.array([st.session_state])
        # Send the image to the API
        api_endpoint = "https://insects-api.herokuapp.com/predict"  # Replace with your API endpoint
        files = {"file": img_file}
        response = requests.post(api_endpoint, files=files)

        # Process the API response
        if response.status_code == 200:
            result = response.json()
            predictions = result["predictions"]
            # Do something with the predictions
            st.write(predictions)
        else:
            st.error("Failed to send the image to the API.")

### Footer 
empty_space, footer = st.columns([1, 2])

with empty_space:
    st.write("")

with footer:
    st.markdown("""
        🍇
        If you want to learn more, check out [streamlit's documentation](https://docs.streamlit.io/) 📖
    """)


