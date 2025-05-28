from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utilities.database import get_db
from app import schemas, models

router = APIRouter(prefix="/macchineControlli", tags=["MacchineControlli"])


@router.get("/", response_model=list[schemas.macchineControlli.MacchinaControlloOut])
def get_all(db: Session = Depends(get_db)):
    return db.query(models.MacchineControlli).all()


@router.post("/", response_model=schemas.macchineControlli.MacchinaControlloOut)
def create(item: schemas.macchineControlli.MacchinaControlloCreate, db: Session = Depends(get_db)):
    nuova = models.MacchineControlli(**item.dict())
    db.add(nuova)
    db.commit()
    db.refresh(nuova)
    return nuova


@router.get("/{item_id}", response_model=schemas.macchineControlli.MacchinaControlloOut)
def get(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.MacchineControlli).filter_by(id=item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Associazione non trovata")
    return item


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.MacchineControlli).filter_by(id=item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Associazione non trovata")
    db.delete(item)
    db.commit()
    return {"detail": "Associazione eliminata"}
