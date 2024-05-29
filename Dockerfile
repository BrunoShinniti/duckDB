FROM python:3.12

LABEL maintainer="Bruno Shinniti"

USER root

RUN apt-get update && \
    apt-get install -y wget unzip curl git sudo iputils-ping

RUN mkdir /app
VOLUME /app

WORKDIR /app

COPY . .
RUN pip install -r ./requirements.txt

CMD ["/bin/bash"]
