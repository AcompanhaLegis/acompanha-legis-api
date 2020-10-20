# Acompanha Legis

Esse projeto compila dados dos Dados Abertos da Camara e os disponibiliza através de uma API para [Camara data portal](https://github.com/AcompanhaLegis/camara-data-portal).


## Começando

Essas instruções vão te ajudar a ter uma cópia do projeto rodando no seu computador com docker para desenvolvimento.
Se quiser, fazer o deploy do projeto, veja mais nas notas de deploy


### Pré-requisitos

Primeiro, instale docker, e siga os passos de instalação.

Se quiser rodar localmente, é possível. Mas ainda não temos instruções aqui. Foi mal :(


### Instalação

#### Docker

1. Instale docker
Para instalar, vá ao [site do docker](https://docs.docker.com/get-docker/)
e siga as instruções de instalação para o seu sistema operacional.

1. Copie o arquivo de ambiente de exemplo

```
$ cp .env.example .env
```


#### Local

Queremos ter as instruções de instalação local, mas ainda não temos.


## Rodar o projeto

#### Docker
Para rodar a api com docker, execute o seguinte comando
```
$ docker-compose up
```
Se quiser deixar o projeto rodando sem ocupar o seu terminal, basta adicionar a flag `-d` ao final do comando acima.

Depois abra `http://localhost:8000/` no seu navegador


## Problemas

Para algumas pessoas que fizeram o "build" do projeto anteriormente (docker-compose.dev.yml) você pode enfrentar algums problemas, tente os seguintes comandos:

````
$ docker-compose down && docker-compose build --no-cache
````

> :warning: Se problema persistir por favor abra uma issue para conseguir ajudar, você pode tentar remover manualmente as imagens api e task e rodar novamente `docker-compose up`.


## Desenvolvimento

Algumas dicas...


### Migrations

Quando alterar alguma model, você precisará criar uma nova `migration` e aplicá-las para alterar o banco de dados.

Para criar novas `migrations` baseadas nas alterações das models, execute o comando.

```
$ docker-compose exec api python ./manage.py makemigrations
```

Para aplicar, basta executar o comando a seguir

```
$ docker-compose exec api python ./manage.py migrate
```

### Teste de emails 

Para testar os emails, incluímos no projeto o [mailhog](https://github.com/mailhog/MailHog), com isso é possível testar o envio de emials  e também o recebimento acessando: `localhost:8025`, por padrão o django já está configurado para usuá-lo.


## Deploy

Adicionar informações para fazer deploy do sistema

## Feito com

* [Django](https://www.djangoproject.com/) - DjangoThe web framework for perfectionists with deadlines.

## Quer contribuir?

Para contribuir, leia o arquivo [CONTRIBUTING.md](tobedone) e veja mais detalhes de como enviar `pull requests`.

## Código de conduta
Por favor leia o [Código de conduta](https://github.com/AcompanhaLegis/code-of-conduct).
E sempre respeite as pessoas da comunidade.

## Versionamento

Ainda não estamos usando nenhum. Mas quando resolvermos isso, usaremos [SemVer](http://semver.org/).

## License

Esse projeto está sob MIT License. Veja mais detalhes em [LICENSE.md](LICENSE.md).

---
Veja quem já contribuiu com o projeto na página [contributors](https://github.com/your/project/contributors).
