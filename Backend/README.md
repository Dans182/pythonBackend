# README

## Instalar paquetes FastAPI

pip install fastapi[all]
pip install python-jose[cryptography]
pip install passlib[bcrypt]
pip install pymongo

`curl -fsSL https://deta.space/assets/space-cli.sh | sh`

## Lanzar el servidor local

uvicorn main:app --reload

## Lanzar MongoDB

mongod --dbpath "/home/userti/MongoDB/data"

## Conectar MongoDB VS Code con Mongo Atlas

mongodb+srv://test:<password@cluster0.vibelps.mongodb.net>/

## Detener el servidor local

Ctrol + C

## Generador automático de documentación

En nuestro proyecto, al usar FastAPI, la documentación se crea de forma automática

### Swagger UI

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Redoc

[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Enlaces de interés

[FastAPI](https://fastapi.tiangolo.com/)

[Swagger UI](https://swagger.io/tools/swagger-ui/)

[redoc](https://dev.to/williamdelaespriella/redoc-documentacion-agil-libre-de-dependencias-1jhk)

## Enlace para encriptar contraseña - Bcrypt

[Bcrypt generator](https://bcrypt-generator.com/https://bcrypt-generator.com/)

## Enlace para instalar MongoDB

 -MongoDB Command Line Database Tools Download

 -MongoDB Community Server Download

[MongoDB](https://www.mongodb.com/try/download/bi-connector)

[MongoDB](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#std-label-install-mdb-community-ubuntu)

Para hacerla funcionar en local debemos
Lanzo instancia de DB en local.
Por terminal, primero lanzar la instancia
mongod --dbpath "/home/userti/MongoDB/data"

Despues desde VS Code, conectarla con su app
MongoDB for VS Code
usando esta url
mongodb://localhost

[Deta](https://deta.space/docs/en/build/new-apps)
