from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utilities.database import get_db
from app import schemas, models

router = APIRouter(prefix="/macchine", tags=["Macchine"])


@router.get("/", response_model=list[schemas.macchine.MacchinaOut])
def get_macchine(db: Session = Depends(get_db)):
    return db.query(models.Macchine).all()


@router.post("/", response_model=schemas.macchine.MacchinaOut)
def create_macchina(macchina: schemas.macchine.MacchinaCreate, db: Session = Depends(get_db)):
    db_macchina = db.query(models.Macchine).filter_by(telaio=macchina.telaio).first()
    if db_macchina:
        raise HTTPException(status_code=400, detail="Telaio già registrato")
    nuova = models.Macchine(**macchina.dict())
    db.add(nuova)
    db.commit()
    db.refresh(nuova)
    return nuova


@router.get("/{macchina_id}", response_model=schemas.macchine.MacchinaOut)
def get_macchina(macchina_id: int, db: Session = Depends(get_db)):
    macchina = db.query(models.Macchine).filter_by(id=macchina_id).first()
    if not macchina:
        raise HTTPException(status_code=404, detail="Macchina non trovata")
    return macchina


@router.delete("/{macchina_id}")
def delete_macchina(macchina_id: int, db: Session = Depends(get_db)):
    macchina = db.query(models.Macchine).filter_by(id=macchina_id).first()
    if not macchina:
        raise HTTPException(status_code=404, detail="Macchina non trovata")
    db.delete(macchina)
    db.commit()
    return {"detail": "Macchina eliminata"}
