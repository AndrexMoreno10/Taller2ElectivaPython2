from fastapi import FastAPI
from starlette.responses import RedirectResponse

#Base de datos
from routes.user import users_route
from routes.animal import animals_route
from routes.vehicle import vehicles_route
from routes.product import products_route
from routes.venta import ventas_route


from contextlib import asynccontextmanager
from database import database as connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    #conectar a la base de datos si la conexion esta cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aqui es donde se ejecutara la aplicacion
    finally:
        # Cerrar la conexion cuando la aplicacion se detenga
        if not connection.is_closed():
            connection.close()


app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

#Rutas
app.include_router(users_route, prefix="/users", tags=["Users"])
app.include_router(animals_route, prefix="/animals", tags=["Animals"])
app.include_router(vehicles_route, prefix="/vehicles", tags=["Vehicles"])
app.include_router(products_route, prefix="/products", tags=["Products"])
app.include_router(ventas_route, prefix="/ventas", tags=["Ventas"])