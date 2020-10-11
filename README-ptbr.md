# Acompanha Legis

Esse projeto compila dados dos Dados Abertos da Camara e os disponibiliza atravÃ©s de uma API para [Camara data portal](https://github.com/AcompanhaLegis/camara-data-portal).


## ComeÃ§ando

Essas instruÃ§Ãµes vÃ£o te ajudar a ter uma cÃ³pia do projeto rodando no seu computador com docker para desenvolvimento.
Se quiser, fazer o deploy do projeto, veja mais nas notas de deploy


### PrÃ©-requisitos

Primeiro, instale docker, e siga os passos de instalaÃ§Ã£o.

Se quiser rodar localmente, Ã© possÃ­vel. Mas ainda nÃ£o temos instruÃ§Ãµes aqui. Foi mal :(


### InstalaÃ§Ã£o

#### Docker

1. Instale docker
Para instalar, vÃ¡ ao [site do docker](https://docs.docker.com/get-docker/)
e siga as instruÃ§Ãµes de instalaÃ§Ã£o para o seu sistema operacional.

1. Copie o arquivo de ambiente de exemplo

```
$ cp .env.example .env
```


#### Local

Queremos ter as instruÃ§Ãµes de instalaÃ§Ã£o local, mas ainda nÃ£o temos.


## Rodar o projeto

#### Docker
Para rodar a api com docker, execute o seguinte comando
```
$ docker-compose up
```
Se quiser deixar o projeto rodando sem ocupar o seu terminal, basta adicionar a flag `-d` ao final do comando acima.

Depois abra `http://localhost:8000/` no seu navegador

## Problemas

Para algumas pessoas que fizeram o "build" do projeto anteriorment (docker-compose.dev.yml) você pode enfrentar algums problemas, tente os seguintes comandos:

````
$ docker-compose down && docker-compose build --no-cache
````

> :warning: Se problema persistir por favor abra uma issue para conseguir ajudar, vocÃ pode tentar remover manualmente as imagens api e task e rodar novamente `docker-compose up` 


## Desenvolvimento

Algumas dicas...


### Migrations

Quando alterar alguma model, vocÃª precisarÃ¡ criar uma nova `migration` e aplicÃ¡-las para alterar o banco de dados.

Para criar novas `migrations` baseadas nas alteraÃ§Ãµes das models, execute o comando.

```
$ docker-compose -f docker-compose.dev.yml exec api python ./manage.py makemigrations
```

Para aplicar, basta executar o comando a seguir

```
$ docker-compose exec api python ./manage.py migrate
```


## Deploy

Adicionar informaÃ§Ãµes para fazer deploy do sistema

## Feito com

* [Django](https://www.djangoproject.com/) - DjangoThe web framework for perfectionists with deadlines.

## Quer contribuir?

Para contribuir, leia o arquivo [CONTRIBUTING.md](tobedone) e veja mais detalhes de como enviar `pull requests`.

## CÃ³digo de conduta
Por favor leia o [CÃ³digo de conduta](https://github.com/AcompanhaLegis/code-of-conduct).
E sempre respeite as pessoas da comunidade.

## Versionamento

Ainda nÃ£o estamos usando nenhum. Mas quando resolvermos isso, usaremos [SemVer](http://semver.org/).

## License

Esse projeto estÃ¡ sob MIT License. Veja mais detalhes em [LICENSE.md](LICENSE.md).

---
Veja quem jÃ¡ contribuiu com o projeto na pÃ¡gina [contributors](https://github.com/your/project/contributors).
