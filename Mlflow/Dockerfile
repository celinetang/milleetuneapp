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
ENV ARTIFACT_STORE_URI=$s3://insects-s3

CMD mlflow server -p $PORT \
    --host 0.0.0.0 \
    --backend-store-uri $postgresql://wujqcbshepvvkl:99166ded0f9c7ebf673e3f52dddd5b14422fd00717b115eff49c7ca5cf5c0af0@ec2-34-193-110-25.compute-1.amazonaws.com:5432/dbebk0buu8lf4q \
    --default-artifact-root $s3://insects-s3
