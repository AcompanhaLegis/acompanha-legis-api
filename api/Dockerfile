FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=1
ENV TZ=America/Sao_Paulo

WORKDIR /opt/acompanha_legis

COPY . .

RUN mkdir -p \
    /var/run/acompanha_legis &&\
    touch /var/run/acompanha_legis/api.pid

RUN apk update && apk --no-cache add --virtual build-dependencies \
    gcc \
    musl-dev \
    postgresql-dev \
    tzdata &&\
    pip install -U pip setuptools &&\
    ./setup.py install &&\
    api collectstatic &&\
    rm -rf /opt/acompanha_legis/*

COPY extras/nginx/api.conf /etc/nginx/conf.d/default.conf

VOLUME ["/var/acompanha_legis/api/static", "/etc/nginx/conf.d"]

CMD [ "gunicorn", "-b", ":8000", "-w", "4", "-p", "/var/run/acompanha_legis/api.pid", "--log-level=INFO", "--preload", "api.wsgi:application" ]
