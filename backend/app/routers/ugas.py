from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/ugas", tags=["UGA"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.UgaRead])
def list_ugas(db: Session = Depends(get_db)):
    return db.query(models.Uga).order_by(models.Uga.sigla).all()


@router.get("/estados", response_model=list[models.EstadoBrasileiro])
def list_estados():
    """Retorna todas as siglas válidas para o seletor de estado da UGA."""
    return list(models.EstadoBrasileiro)
