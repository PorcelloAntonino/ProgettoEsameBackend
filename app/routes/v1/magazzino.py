from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utilities.database import get_db
from app import schemas, models

router = APIRouter(prefix="/magazzino", tags=["Magazzino"])


@router.get("/", response_model=list[schemas.magazzino.MagazzinoOut])
def get_magazzino(db: Session = Depends(get_db)):
    return db.query(models.Magazzino).all()


@router.post("/", response_model=schemas.magazzino.MagazzinoOut)
def create_magazzino(item: schemas.magazzino.MagazzinoCreate, db: Session = Depends(get_db)):
    nuovo = models.Magazzino(**item.dict())
    db.add(nuovo)
    db.commit()
    db.refresh(nuovo)
    return nuovo


@router.get("/{item_id}", response_model=schemas.magazzino.MagazzinoOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Magazzino).filter_by(id=item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Voce magazzino non trovata")
    return item


@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Magazzino).filter_by(id=item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Voce magazzino non trovata")
    db.delete(item)
    db.commit()
    return {"detail": "Voce eliminata"}
