# Acompanha Legis
> Para ler esse arquivo em português, vá ao [README-ptbr.md](https://github.com/AcompanhaLegis/acompanha-legis-api/blob/master/README-PTBR.md)

This is a project for compile data from Dados Abertos da Camara and serve though API to [Camara data portal](https://github.com/AcompanhaLegis/camara-data-portal).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine with docker for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

First, have docker, please. Then follow installation steps.
If you want to run locally, iit is possible But I have no instructions here. Sorry.


### Installing

#### Docker

1. Install docker
To install docker, please refer to [their website](https://docs.docker.com/get-docker/)
and follow the instructions for your operational system.

1. Copy the example environment file

```
$ cp .env.example .env
```


#### Locally

We plan to have the tutorial to install locally, but we do not yet.


## Running

#### Docker
To run the api with docker, just run the following command
```
$ docker-compose -f docker-compose.dev.yml up
```

## Development

Here are some tips...

### Migrations

When changing a model, you will need to create new migrations and migrate them so they be applied on the database schema.

To create migrations based on the the changes in the model, run the following command

```
$ docker-compose -f docker-compose.dev.yml exec api python ./manage.py makemigrations
```

To migrate and apply them to the database, run the following command

```
$ docker-compose -f docker-compose.dev.yml exec api python ./manage.py migrate
```


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Django](https://www.djangoproject.com/) - DjangoThe web framework for perfectionists with deadlines.

## Contributing

Please read [CONTRIBUTING.md](tobedone) for details on the process for submitting pull requests to us.

## Code of Conduct
Please read [Code of Conduct](https://github.com/AcompanhaLegis/code-of-conduct).
And always be considerate and respectful.

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

---
Go to the [contributors](https://github.com/your/project/contributors) page to see who participated in this project.
