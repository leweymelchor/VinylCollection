FROM python:3.9-alpine3.13
LABEL maintainer="vinylcollection.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
