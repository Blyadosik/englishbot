FROM python:3.7-slim

RUN mkdir /src
WORKDIR /src
COPY . /src
RUN pip install -r requirements.txt