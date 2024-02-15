FROM python:3.12-slim

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /usr/src/app/requirements.txt && rm /usr/src/app/requirements.txt

COPY ./* /usr/src/app