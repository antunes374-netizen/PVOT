from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/trechos", tags=["Trechos"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.TrechoRead])
def list_trechos(db: Session = Depends(get_db)):
    return db.query(models.Trecho).order_by(models.Trecho.id).all()
