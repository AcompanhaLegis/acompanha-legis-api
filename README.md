## Acompanha Legis

This is a project for compile data from Dados Abertos da Camara and serve though API to [Camara data portal](https://github.com/AcompanhaLegis/camara-data-portal).


## Docker

Setting up for development:

```
$ cp .env.example .env

$ docker-compose -f docker-compose.dev.yml up

$ docker-compose -f docker-compose.dev.yml exec api python ./api/manage.py migrate
```
