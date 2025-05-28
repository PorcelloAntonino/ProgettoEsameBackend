from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utilities.database import get_db
from app import schemas, models

router = APIRouter(prefix="/controlli", tags=["Controlli"])


@router.get("/", response_model=list[schemas.controlli.ControlloOut])
def get_controlli(db: Session = Depends(get_db)):
    return db.query(models.Controlli).all()


@router.post("/", response_model=schemas.controlli.ControlloOut)
def create_controllo(c: schemas.controlli.ControlloCreate, db: Session = Depends(get_db)):
    nuovo = models.Controlli(**c.dict())
    db.add(nuovo)
    db.commit()
    db.refresh(nuovo)
    return nuovo


@router.get("/{controllo_id}", response_model=schemas.controlli.ControlloOut)
def get_controllo(controllo_id: int, db: Session = Depends(get_db)):
    c = db.query(models.Controlli).filter_by(id=controllo_id).first()
    if not c:
        raise HTTPException(status_code=404, detail="Controllo non trovato")
    return c


@router.delete("/{controllo_id}")
def delete_controllo(controllo_id: int, db: Session = Depends(get_db)):
    c = db.query(models.Controlli).filter_by(id=controllo_id).first()
    if not c:
        raise HTTPException(status_code=404, detail="Controllo non trovato")
    db.delete(c)
    db.commit()
    return {"detail": "Controllo eliminato"}
