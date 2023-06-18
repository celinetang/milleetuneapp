FROM continuumio/miniconda3

WORKDIR /home/app

RUN apt-get update
RUN apt-get install nano unzip
RUN apt install curl -y

RUN curl -fsSL https://get.deta.dev/cli.sh | sh

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install

COPY requirements.txt /dependencies/requirements.txt
RUN pip install -r /dependencies/requirements.txt

ENV AWS_ACCESS_KEY_ID=your-private-secret-key
ENV AWS_SECRET_ACCESS_KEY=your-private-secret-key
ENV BACKEND_STORE_URI=our-private-secret-key
ENV ARTIFACT_STORE_URI=your-own-store

CMD mlflow server -p $PORT \
    --host 0.0.0.0 \
    --backend-store-uri your-back-end-store \
    --default-artifact-root your-own-store
