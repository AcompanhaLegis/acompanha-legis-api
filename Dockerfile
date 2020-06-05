FROM python:3.7-alpine

WORKDIR /opt/acompanha-legis

ADD . .

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "./api/manage.py", "runserver", "0.0.0.0:8000"]
