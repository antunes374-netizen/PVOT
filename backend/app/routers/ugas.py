from fastapi import APIRouter, Depends, HTTPException, status
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


@router.post("/", response_model=schemas.UgaRead, status_code=status.HTTP_201_CREATED)
def create_uga(payload: schemas.UgaBase, db: Session = Depends(get_db)):
    existente = db.query(models.Uga).filter(models.Uga.sigla == payload.sigla).first()
    if existente:
        raise HTTPException(status_code=409, detail="Já existe uma UGA com essa sigla.")
    dados = payload.model_dump()
    dados["estado"] = payload.estado.value
    dados["tipo_ug"] = payload.tipo_ug
    uga = models.Uga(**dados)
    db.add(uga)
    db.commit()
    db.refresh(uga)
    return uga
