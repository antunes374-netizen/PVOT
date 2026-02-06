from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/diarias", tags=["Diárias"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.DiariaValorRead])
def list_diarias(db: Session = Depends(get_db)):
    return db.query(models.DiariaValor).order_by(models.DiariaValor.id).all()
