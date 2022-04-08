# Microservice pet project

## Get started:
- Python3.7 must be installed
- Docker must be installed

## Environments
For custom vars, set vars in docker-compose.yml

### RabbitMQ
- RABBITMQ_DEFAULT_USER:
- RABBITMQ_DEFAULT_PASS:

### Postgresql
- POSTGRES_USER:
- POSTGRES_PASSWORD:

### Api-services
- DB_USER 
- DB_PASSWORD:
- DB_HOST:
- DB_PORT: 5432 (default example)
- DB: 
- RABBITMQ_USER:
- RABBITMQ_PASSWORD:
- RABBITMQ_HOST: 
- RABBITMQ_PORT: 5672 (default example)

## Install
```angular2html
components/docker-compose up --build
```
