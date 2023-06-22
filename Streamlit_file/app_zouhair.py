import streamlit as st
import pandas as pd
import numpy as np
import requests
from PIL import Image
# from PIL.ImageOps import exif_transpose
# import time
# import base64
# import io
# import cv2
# import Nominatim
# import folium


import requests
from urllib.request import urlopen
import json
import pyautogui

clear = st.sidebar.button("CLEAR")
location = st.sidebar.text_input("Enter Location ","")

def Clear():
    pyautogui.press("tab", interval=0.15)
    pyautogui.hotkey("ctrl", "a",'del', interval=0.15)
    pyautogui.press("return", interval=0.15)

# Clear location
if clear:
    Clear()

st.title("**" + "Sreamlit - HERE Location Services app" + "**")

@st.cache(allow_output_mutation=True)
def get_longitude_latitude(location):
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    api_key = 'UPDATE-YOUR-JAVASCRIPT-API-KEY'  # Acquire from developer.here.com
    PARAMS = {'apikey': api_key, 'q': location}
    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    latitude = data['items'][0]['position']['lat']
    longitude = data['items'][0]['position']['lng']

    # Read in the file
    with open('source.js', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('latval', str(latitude))
    filedata = filedata.replace('lngval', str(longitude))
    filedata = filedata.replace('rndlat', str(latitude).split(".")[0])
    filedata = filedata.replace('rndlng', str(longitude).split(".")[0])

    # Write the file out again
    with open('C:\\xampp\\htdocs\\demo.js', 'w') as file:
        file.write(filedata)


# if len(location) > 1:
#     try:
#         get_longitude_latitude(location)
#         st.markdown("**" + location.upper() + "**")
#         components.iframe("http://localhost/demo.html",width=900,height=1200)
#     except:
#         st.error("Invalid Location")


# ## Renseigner l'adresse où le papillon a été apercu

# location = st.text_input("Enter the location where the photo was taken")

# geolocator = Nominatim(user_agent="my_app")




# # # Créer un widget pour le menu hamburger
# menu_expanded = st.sidebar.checkbox('☰ Menu')

# # # Afficher les options du menu lorsque le menu est étendu
# if menu_expanded:
#     st.sidebar.write("Remonter un bug")
#     st.sidebar.write("About")

# if menu_expanded:
#     st.sidebar.subheader("Remonter un bug")

# #     # Option pour saisir un commentaire
#     commentaires = st.sidebar.text_area("Saisir un commentaire", value="", height=100)

#     # Afficher les commentaires saisis
#     if commentaires:
#         st.sidebar.subheader("Commentaires")
#         st.sidebar.write(commentaires)

#     # Afficher un GIF
#     st.image("/Users/zouhair/Documents/Streamlit_file/gif-insect1.gif", width=200)


# ### Input data 
# st.subheader("Input data")
# st.markdown("""
#     As a final note, you can use data that a user will insert when he/she interacts with your app.
#     This is called *input data*. To collect these, you can do two things:
#     * [Use any of the input widget](https://docs.streamlit.io/library/api-reference/widgets)
#     * [Build a form](https://docs.streamlit.io/library/api-reference/control-flow/st.form)

#     Depending on what you need to do, you will prefer one or the other. With a `form`, you actually group
#     input widgets together and send the data right away, which can be useful when you need to filter
#     by several variables.
#     # GETTING PHOTOS SAVED 
#     col_photos = st.columns(1)
#     with col_photos:
#         st.markdown("##### Show me what you have captured in the photo")
#         photos_uploader()
#         submit_photos = st.button("Submit moi")
#         if submit_photos:
#             st.session_state.insects = np.append(st.session_state.insects)
#             st.session_state.insects = st.session_state.insects.flatten()
# if location:
#     location_data = geolocator.geocode(location)
#     if location_data:
#         latitude = location_data.latitude
#         longitude = location_data.longitude

#         st.write("Location Address:", location)
#         st.write("Latitude:", latitude)
#         st.write("Longitude:", longitude)

#         # Afficher la carte Google avec l'emplacement
#         st.markdown(f"![Map](https://maps.google.com/maps?q={latitude},{longitude}&z=15&output=embed)")
#     else:
#         st.warning("Invalid location address")

# data_localisation = {
#     'Location': [location],
#     'Latitude': [latitude],
#     'Longitude': [longitude]
# }

# df_localisation = pd.DataFrame(data_localisation)

# # Ajouter les nouvelles données au fichier CSV existant ou créer un nouveau fichier
# df_localisation.to_csv('locations.csv', mode='a', header=not os.path.isfile('locations.csv'), index=False)



# geolocator = Nominatim(user_agent="my_app")

# # Liste pour stocker les coordonnées géographiques des adresses précédentes
# coordinates = []

# for index, row in data_localisation.iterrows():
#     address = row['Address']
#     location_data = geolocator.geocode(address)
#     if location_data:
#         latitude = location_data.latitude
#         longitude = location_data.longitude
#         coordinates.append((latitude, longitude))



# # Créez une carte centrée sur une position initiale
# map = folium.Map(location=[latitude, longitude], zoom_start=12)

# # Ajoutez un marqueur pour chaque coordonnée dans la liste "coordinates"
# for coordinate in coordinates:
#     latitude, longitude = coordinate
#     folium.Marker(location=[latitude, longitude]).add_to(map)

# # Affichez la carte dans Streamlit
# st.markdown(map._repr_html_(), unsafe_allow_html=True)

# ## Notation et commentaires sur la prédiction 

# from trubrics.integrations.streamlit import FeedbackCollector
# collector.st_feedback(feedback_type="faces")
# feedback = collector.st_feedback(
# 	feedback_type="thumbs",
# 	path="thumbs_feedback.json"
# )

# # print out the feedback object as a dictionary in your app
# feedback.dict() if feedback else None

# collector = FeedbackCollector()
# collector.st_feedback(feedback_type="faces")

# ### Footer 
# empty_space, footer = st.columns([1, 2])

# with empty_space:
#     st.write("")

# with footer:
#     st.markdown("""
#         🍇
#         If you want to learn more, check out [streamlit's documentation](https://docs.streamlit.io/) 📖
#     """)