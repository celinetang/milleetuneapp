import os 
from rembg import remove

dossier_images = "archive (1)/insects/Abacarus hystrix (Nalepa)"
dossier_sortie = 'Images_Clean'

if not os.path.exists(dossier_sortie):
    os.makedirs(dossier_sortie)
print("folder created")
# Parcourir les fichiers du dossier d'images
for nom_fichier in os.listdir(dossier_images):
    chemin_fichier = os.path.join(dossier_images, nom_fichier)
    
    # Vérifier si le fichier est une image
    if os.path.isfile(chemin_fichier) and nom_fichier.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Charger l'image
        with open(chemin_fichier, 'rb') as image_fichier:
            image = image_fichier.read()
        
        # Supprimer l'arrière-plan de l'image
        image_sans_arriere_plan = remove(image)
        
        # Chemin de sortie pour l'image sans arrière-plan
        chemin_sortie = os.path.join(dossier_sortie, nom_fichier)
        
        # Enregistrer l'image sans arrière-plan
        with open(chemin_sortie, 'wb') as sortie_fichier:
            sortie_fichier.write(image_sans_arriere_plan)


print("c'est bon, j'ai enleve les fonds de ces images.")
       
