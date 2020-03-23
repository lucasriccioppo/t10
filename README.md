# Foobar

Projeto de teste da t10.
Api para a cervejaria Banquev.

## Installation

Para rodar o projeto é preciso ter instalado:

python3
pip3
docker

## Usage

Rodar os seguintes comandos

Instalar os pacotes necessários:
```bash
make requirements-install
```

Subir docker com imagem do postgres:
```bash
make create-db
```

Criar o banco:
```bash
make postgres
```

Rodar o projeto:
```bash
make run
```