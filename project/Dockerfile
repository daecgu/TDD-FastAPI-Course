# Pull official base image
FROM python:3.11.2-slim-buster

# set working directoriy
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get -y install netcat gcc \
    && apt-get clean

COPY ./requirements.txt .
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

#add app
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
