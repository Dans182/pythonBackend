# Importamos fastAPI
from fastapi import FastAPI
# Instanciamos fastAPI
app = FastAPI()
#Con esto estamos usando fastAPI
@app.get("/")

#Y aca una operación que nos dice hola fastAPI
async def root():
    return "¡Hola FastAPI!"

# Siempre que llamamos a un servidor, la operación que se ejecuta tiene que ser asincrona
# La aplicación no se paraliza durante la llamada al servidor, continua ejecutando tareas y procesos.
# Si fuera síncrona, le tocaría esperar la respuesta del servidor, tarde lo que tarde
# Por eso la asincronía, tiene que ir haciendo cosas en segundo plano e ir devolviendo datos

