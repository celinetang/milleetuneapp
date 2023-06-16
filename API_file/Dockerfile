# FROM continuumio/miniconda3

# WORKDIR /home/app

# RUN apt-get update -y 
# RUN apt-get install nano unzip
# RUN apt-get install -y python3.10
# RUN apt install curl -y

# RUN curl -fsSL https://get.deta.dev/cli.sh | sh

# COPY requirements.txt /dependencies/requirements.txt
# RUN pip install -r /dependencies/requirements.txt

# COPY . /home/app

# CMD gunicorn api:app  --bind 0.0.0.0:$PORT --worker-class uvicorn.workers.UvicornWorker 
FROM python

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /home/app

COPY . /home/app

CMD gunicorn app:app  --bind 0.0.0.0:$PORT --worker-class uvicorn.workers.UvicornWorker 

# api1 cest le nom du fichier à appeler et app c'est le nom de la CLASSE FastAPI qu'on a déf
# gunicorn c'est pcq FastAPI ca sutilise avec uvicorn , meme si le fichier utilise python
# en dessous avec un $PORT ca c'est transparent enfait on va se ocnnecter au nom de 
#  domaine de notre API
# worker-class ca dit qu'on utilise uvicorn

# explications JULIE:
# First we use gunicorn which is the normal web server Heroku is using for deploying web applications.
# Then we are mapping the app.py to the app variable within this file that contains the FastAPI instance. The way we do it is simply by writting app:app.
# Then we specified that we are binding our host URL 0.0.0.0 to a PORT environment variable. This will let Heroku link your Host URL to HTTP and HTTPS access (which are respectively at port 40 and port 443).
# Then we specified --worker-class uvicorn.workers.UvicornWorker flag. This means that normally FastAPI is uvicorn based, which is an asynchronous server whereas Heroku uses a synchronous server (gunicorn) which raises compatibility issues. This flag alleviates this.

# il va falloir faire comme hier:
# create container, heroku login, heroku create -a nom_de_app, heroku push..., 
# heroku web release.., heroku open
# rentrer les credebntials dans heroku

#  pour lancer localement, sans faire heroku tout ca, d'abord créer une image
# ensuite docker run -it -v "$(pwd):/home/app" -p 4001:4000 -e PORT=4000 nom_image
