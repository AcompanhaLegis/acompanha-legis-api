FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=1
ENV TZ=America/Sao_Paulo

WORKDIR /opt/acompanha_legis

COPY . .

RUN apk update && apk --no-cache add --virtual build-dependencies \
    gcc \
    musl-dev \
    postgresql-dev \
    tzdata

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
