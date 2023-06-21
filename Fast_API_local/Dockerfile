FROM python:3.10.10

WORKDIR /home/app

# RUN apt-get update -y 
# RUN apt-get install nano unzip
# RUN apt-get install -y python3.10
# RUN apt install curl -y

# RUN curl -fsSL https://get.deta.dev/cli.sh | sh

COPY requirements.txt /dependencies/requirements.txt
RUN pip install -r /dependencies/requirements.txt

COPY . /home/app


# Document to download aws cli : https://adityagoel123.medium.com/installing-aws-cli-sam-cli-inside-docker-ef91ceb4e250
# Download aws cli
# RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
# Unzip aws cli
# RUN unzip "awscli-bundle.zip"
# Install aws cli
# RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

# Check if aws is installed
# RUN aws --version


# Documentation to dowload the model from s3 with aws cli https://github.com/docker/build-push-action/issues/489
# Add your command to do it


CMD gunicorn app:app  --bind 0.0.0.0:$PORT --worker-class uvicorn.workers.UvicornWorker