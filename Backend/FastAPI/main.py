# Importamos fastAPI
from fastapi import FastAPI
from routers import products, users, user, product
from fastapi.staticfiles import StaticFiles

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

#Routers
app.include_router(products.router)
app.include_router(product.router)
app.include_router(users.router)
app.include_router(user.router)

#Para exponer recursos estáticos
app.mount("/static", StaticFiles(directory="static"), name = "static")

@app.get("/url")
async def root():
    return {"url_curso": "https://mouredev.com/python"}