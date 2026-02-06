from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/militares", tags=["Militares"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.MilitarRead])
def list_militares(db: Session = Depends(get_db)):
    return db.query(models.Militar).order_by(models.Militar.nome_guerra).all()
