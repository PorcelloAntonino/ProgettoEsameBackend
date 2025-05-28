from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utilities.database import get_db
from app import schemas, models

router = APIRouter(prefix="/vendite", tags=["Vendite"])


@router.get("/", response_model=list[schemas.vendite.VenditaOut])
def get_vendite(db: Session = Depends(get_db)):
    return db.query(models.Vendite).all()


@router.post("/", response_model=schemas.vendite.VenditaOut)
def create_vendita(vendita: schemas.vendite.VenditaCreate, db: Session = Depends(get_db)):
    nuova = models.Vendite(**vendita.dict())
    db.add(nuova)
    db.commit()
    db.refresh(nuova)
    return nuova


@router.get("/{vendita_id}", response_model=schemas.vendite.VenditaOut)
def get_vendita(vendita_id: int, db: Session = Depends(get_db)):
    v = db.query(models.Vendite).filter_by(id=vendita_id).first()
    if not v:
        raise HTTPException(status_code=404, detail="Vendita non trovata")
    return v


@router.delete("/{vendita_id}")
def delete_vendita(vendita_id: int, db: Session = Depends(get_db)):
    v = db.query(models.Vendite).filter_by(id=vendita_id).first()
    if not v:
        raise HTTPException(status_code=404, detail="Vendita non trovata")
    db.delete(v)
    db.commit()
    return {"detail": "Vendita eliminata"}
