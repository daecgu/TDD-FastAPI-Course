# Pull official base image
FROM python:3.11.2-slim-buster

# set working directoriy
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get -y installnetcat gcc \
    &&apt-get clean

COPY ./requirements.txt .
RUN pip install --upgrade \
    && pip install -r requirements.txt

#add app
COPY . .
