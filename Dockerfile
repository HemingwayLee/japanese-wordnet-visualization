FROM python:3.8

RUN apt-get update && apt-get install -y nginx vim

RUN mkdir -p /home/proj
WORKDIR /home/proj
COPY . .

RUN cp /home/proj/nginx/default /etc/nginx/sites-enabled/default
RUN pip3 install -r requirements.txt

WORKDIR /home/proj/jpwordnet
RUN python3 manage.py migrate

ENTRYPOINT nginx && python3 manage.py runserver 0.0.0.0:8000 && /bin/bash

