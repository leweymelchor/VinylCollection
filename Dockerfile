FROM python:3.9-alpine3.13
LABEL maintainer="vinylcollection.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./vinyl_collection /vinyl_collection

WORKDIR /vinyl_collection
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app

ENV PATH="/bin:$PATH"

USER app
