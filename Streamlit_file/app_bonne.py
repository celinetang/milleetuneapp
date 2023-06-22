import streamlit as st
import pandas as pd
import numpy as np
import requests
from PIL import Image
from PIL.ImageOps import exif_transpose
import time
import base64
import io
import os



### Config
st.set_page_config(
    page_title="Which bug ?",
    page_icon="",
    layout="wide"
    )

# --------------------------------    DISPLAY USER PIC    -----------------------------   

def photos_uploader(): 
    # Displays a file uploader to upload a photo of the insect
    img_file = st.file_uploader("Upload a photo of your insect:")
    
    if img_file is not None:
        st.info('Thank you.')
        # Display the preview of the uploaded photo
        img = Image.open(img_file)
        st.image(img, width=50)

    return img_file


# ---------------------------------------------------------------------------------------   


### App

col1, col2, col3 = st.columns(3)
with col1:
    st.image("valid/ADONIS/1.jpg")
with col2:
    st.markdown("<h1 style='text-align: center; color: magenta;'>Welcome to 1001APP</h1>", unsafe_allow_html=True)
with col3:
    st.image("valid/VICEROY/1.jpg")

st.markdown("<h2 style='text-align: center; color: magenta;'>Recognize which insect it is ! </h2>", unsafe_allow_html=True)

st.markdown("""
    Just take or upload your picture, and we will discover which butterfly it is. 
    
    You will get additionnal information on your buddies too, and participate in a great tracking of butterflies around the world.
    
    You can download the whole code here 👉 [Source code](à remplir)
""")
st.markdown("---")


if __name__ == '__main__':

    
# -------------------------------------    TEST API     ----------------------------------   
    
    
    st.subheader("API test")  
    if st.button("click to obtain hello", key = "hello test") :
        r = requests.get("https://api-heroku-h5-55a38f5bd18c.herokuapp.com/hello")
        response = r.content
        if r.status_code == 200:           
             # Do something with the predictions
            st.write(response)
        else:
            st.error("Failed to say hello to the API.")


# ------------------------------------     PREDICTION    --------------------------------   
    
    st.subheader("Let's BUG it !")
    img_file = photos_uploader() 
    api_call = st.button("Analyze my butterfly", key = "predict butterfly")
    
    if api_call:

        # Barre de progression:
        import time
        progress_text = "Flying as fast as possible. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.05)
            my_bar.progress(percent_complete + 1, text=progress_text)

        api_endpoint = "https://api-heroku-h5-55a38f5bd18c.herokuapp.com/predict"  # Replace with your API endpoint
        files = {"file": img_file.getvalue()}
        response = requests.post(api_endpoint, files=files)
        # Process the API response
        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]
            # Do something with the predictions
            st.write("### What a beautiful",prediction,"!")
            st.balloons()

# -----------------------------     AFFICHAGE PREDICTION    ----------------------------   

            folder_prediction = str(prediction).upper()
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(f"valid/{folder_prediction}/1.jpg")
            with col2:
                st.image(f"valid/{folder_prediction}/2.jpg")
            with col3:
                st.image(f"valid/{folder_prediction}/3.jpg")

# -----------------------------     SCRAP WIKIPEDIA    ----------------------------   

            st.subheader("Wanna get more info ?")
            # Import package
            import wikipedia
            # Specify the title of the Wikipedia page
            wiki = wikipedia.page(f"{prediction}")
            # Extract the plain text content of the page
            text = wiki.content
            # Remove headers and shit
            import re
            text = re.sub(r'==.*?==+', '', text)
            text = text.replace('\n', '')
            st.write(text)


# -----------------------------     CLOSE LOOP    ----------------------------   

        else:
            st.error("Failed to send the image to the API.")


# -----------------------------     GEOLOC    ----------------------------   
    
    st.subheader("Geolocate you !")

    from geopy.geocoders import Nominatim
    from geopy.extra.rate_limiter import RateLimiter

    col1, col2 = st.columns(2)
    with col1:
        street = st.text_input("Street", "Charles de montesquieu")
        city = st.text_input("City", "antony")
        country = st.text_input("Country", "france")
    with col2:      
        geolocator = Nominatim(user_agent="GTA Lookup")
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
        location = geolocator.geocode(street+", "+city+", "+country)

        lat = location.latitude
        lon = location.longitude

        map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})

        st.map(map_data) 


# ---------------------------------     COMMENTAIRES    -----------------------------------
    
    # Option pour saisir un commentaire
    commentaires = st.text_area("Any problem with the app ?", value="", height=100)
    # Afficher les commentaires saisis
    if commentaires:
        if st.button("Submit", key = "Submit comment"):
            with open("comments.txt", "a") as file:
                file.write(commentaires + "\n")
                # # https://docs.streamlit.io/knowledge-base/tutorials/databases/postgresql
                # # Connect to the Heroku PostgreSQL database
                # database_url = os.environ["postgres://yrwkoeqtsqafif:dca641ba343d03114222584792d5954436b7c827ec086fbaf07814ff12565722@ec2-34-242-199-141.eu-west-1.compute.amazonaws.com:5432/dapfj9fsn6hogo"]
                # import psycopg2
                # conn = psycopg2.connect(database_url,sslmode='require')
                # cursor = conn.cursor()
                # # Prepare the data
                # comment = commentaires
                # # You can include additional information like user ID, timestamp, etc.
                # # Execute the database query
                # cursor.execute("INSERT INTO comments (comment) VALUES (%s)", (comment,))
                # conn.commit()
                # # Close the connection
                # cursor.close()
                # conn.close()

            st.success("Thanks for your comment ! !")

    # from trubrics.integrations.streamlit import FeedbackCollector
    # collector = FeedbackCollector()
    # collector.st_feedback(feedback_type="issue")
    # collector.st_feedback(feedback_type="faces")




### Footer 
empty_space, footer = st.columns([1, 2])

with empty_space:
    st.write("")

with footer:
    st.markdown("""
        🍇
        Thanks for your contribution, we hope to see you soon. 📖
    """)


# https://docs.streamlit.io/library/api-reference/widgets
# https://docs.streamlit.io/library/api-reference/control-flow/st.form

