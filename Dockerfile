FROM python:3.7

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install datetime pytest

