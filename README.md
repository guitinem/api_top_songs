# api_top_songs
Api utilizando o framework Flask para trazer as 10 músicas mais conhecidas de um dado artista

## Requisitos

- Python 3.6+
- Pip package manager
- Virtualenv (caso prefira, fique a vontade para instalar outro gerenciador de env's)
- [Redis versão 5.0.7](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04-pt)
- [Genius CLIENT ACCESS TOKEN (necessário criar uma conta)](https://genius.com/api-clients)
- [Serviço DynamoDB da Aws disponível](https://sa-east-1.console.aws.amazon.com/dynamodb/home?region=sa-east-1)

## Instalação

> Os comandos utilizados neste documento são baseados na distribuição Linux Ubuntu 20.04

Para evitar conflitos de pacotes, é recomendado a utilização de um ambiente virtual. Neste caso utilizaremos o virtualenv para a criação deste ambiente virtual e instalação de todas as dependências necessárias para o funcionamento correto do projeto.

Para podermos iniciar as instalações, no diretório do projeto clonado, devemos criar um ambiente virtual para o projeto, utilizaremos os seguintes comando para isso:


Instalação e atualização do Virtualenv:

```bash
pip3 install virtualenv
pip install --upgrade virtualenv
```

Criação do ambiente virtual com o virtualenv setando o Python3 como padrão:

```bash
virtualenv -p python3 envname
```

Para ativar o ambiente virtual, utilize o comando:

```bash
source envname/bin/activate

// Para desativar utilize o comando:
deactivate
```

Com o ambiente virtual ativo, utilizaremos o seguinte comando para instalar algumas dependências prévias:

```bash
sudo apt-get install python3-dev
```

Agora podemos instalar o as dependências contidas no arquivo requirements.txt

```bash
pip install -r requirements.txt
```

## Preparando o ambiente
No arquivo **request_manager.py**, coloque o token da genius api
> TOKEN = "" # Token Genius Api


### Preparando DynamoDB
**Não esqueça de ativar o ambiente virtual**

Precisamos configurar o aws para poder utilizar o DynamoDB, execute a linha de comando no terminal:

```shell
aws configure
```

Após isso, será requisitado suas credenciais de acesso da aws, para criação da tabela no dynamoDb, [elas podem ser encontradas aqui](https://console.aws.amazon.com/iam/home?region=sa-east-1#/security_credentials)

```shell
AWS Access Key ID [None]: ***Coloque o ID da chave de acesso aqui*** AWS Secret Access Key [None]: ***Coloque a chave de acesso secreta aqui*** Default region name [None]: sa-east-1	 Default output format [None]: json
```

Depois de configurar o aceso ao aws, vamos criar uma tabela no banco para começar a utilizar, execute o seguinte comando:

```shell
aws dynamodb create-table --cli-input-json file://src/static/table.json 
```

Pronto, já criamos uma tabela no banco e prontos para usar.

## Testando o projeto

execute o comando a abaixo para iniciar a api:
> python app.py

faça um teste com a seguinte rota:
http://localhost:5000/songs/iveteSangalo

Ou, para fazer uma consulta sem utilizar o cache:
http://localhost:5000/songs/u2?cache=False
