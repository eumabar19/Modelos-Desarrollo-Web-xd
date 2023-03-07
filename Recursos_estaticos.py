from fastapi import FastAPI 
from routers import routers_5
from fastapi.staticfiles import StaticFiles

app= FastAPI()

app.include_router(routers_5.router)
#Creamos una app para acceder al directorio de recursos estaticos***
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
