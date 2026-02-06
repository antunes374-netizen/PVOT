from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/pvot", tags=["PVOT"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.PvotRead])
def list_pvots(db: Session = Depends(get_db)):
    return db.query(models.Pvot).order_by(models.Pvot.ano.desc()).all()
