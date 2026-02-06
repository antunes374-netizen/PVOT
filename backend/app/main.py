from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from .db import Base, engine
from .routers import dashboard, diarias, militares, pvot, trechos, ugas, visitas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SGVOT - Plano de Visitas de Orientação Técnica")

app.include_router(ugas.router)
app.include_router(militares.router)
app.include_router(trechos.router)
app.include_router(diarias.router)
app.include_router(pvot.router)
app.include_router(visitas.router)
app.include_router(dashboard.router)

frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "frontend"))

if os.path.isdir(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")


@app.get("/")
async def root():
    index_file = os.path.join(frontend_path, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"status": "SGVOT API online"}
