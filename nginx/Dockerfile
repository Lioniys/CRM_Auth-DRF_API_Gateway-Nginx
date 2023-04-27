FROM nginx:latest

WORKDIR /var/www/html

RUN apt-get update \
    && apt-get install -y nginx-module-njs

COPY ./nginx.conf /etc/nginx/nginx.conf