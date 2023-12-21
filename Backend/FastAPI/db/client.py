#gestiona conexion a nuestra db de mongodb
from pymongo import MongoClient

#Base de datos local
#db_client = MongoClient().local #dentro de los parentesis especificaríamos si se conecta a una direccion en remoto

#Base de datos Mongo Atlas Remoto
#Esta es otra forma de conectarte a la DB
db_client = MongoClient("mongodb+srv://test:test@cluster0.vibelps.mongodb.net/?retryWrites=true&w=majority").test