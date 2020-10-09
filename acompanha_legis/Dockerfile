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
    tzdata
RUN pip install -U pip setuptools
RUN pip install Django
CMD [ "python", "./setup.py" ]
RUN rm -rf /opt/acompanha_legis/*

ENTRYPOINT [ "acompanha_legis" ]
# CMD [ "-d", "", "-o", "/var/acompanha_legis" ]
