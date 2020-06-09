FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1
ENV TZ=America/Sao_Paulo

WORKDIR /opt/acompanha_legis

COPY . .

RUN mkdir -p \
    /var/acompanha_legis

RUN apk update && apk --no-cache add --virtual build-dependencies \
    gcc \
    musl-dev \
    postgresql-dev \
    tzdata &&\
    pip install -U pip setuptools &&\
    ./setup.py install &&\
    rm -rf /opt/acompanha_legis/*

CMD [ "acompanha_legis", "-d", "Paula Belmonte", "-o", "/var/acompanha_legis" ]
