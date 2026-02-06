from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/visitas", tags=["Visitas"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.VisitaRead])
def list_visitas(db: Session = Depends(get_db)):
    return db.query(models.Visita).order_by(models.Visita.data_inicio).all()
