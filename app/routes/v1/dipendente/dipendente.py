from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utilities.database import get_db
from app import schemas, models

router = APIRouter(prefix="/dipendenti", tags=["Dipendenti"])


@router.get("/", response_model=list[schemas.dipendente.DipendenteOut])
def get_dipendenti(db: Session = Depends(get_db)):
    return db.query(models.Dipendenti).all()


@router.post("/", response_model=schemas.dipendente.DipendenteOut)
def create_dipendente(dipendente: schemas.dipendente.DipendenteCreate, db: Session = Depends(get_db)):
    db_dip = db.query(models.Dipendenti).filter(
        (models.Dipendenti.username == dipendente.username) |
        (models.Dipendenti.email == dipendente.email)
    ).first()
    if db_dip:
        raise HTTPException(status_code=400, detail="Email o username già in uso")
    hashed = dipendente.password + "notreallyhashed"  # Simulazione hash
    nuovo = models.Dipendenti(
        nome=dipendente.nome,
        cognome=dipendente.cognome,
        email=dipendente.email,
        username=dipendente.username,
        hashed_password=hashed,
        admin=dipendente.admin
    )
    db.add(nuovo)
    db.commit()
    db.refresh(nuovo)
    return nuovo


@router.get("/{dip_id}", response_model=schemas.dipendente.DipendenteOut)
def get_dipendente(dip_id: int, db: Session = Depends(get_db)):
    dip = db.query(models.Dipendenti).filter_by(id=dip_id).first()
    if not dip:
        raise HTTPException(status_code=404, detail="Dipendente non trovato")
    return dip


@router.delete("/{dip_id}")
def delete_dipendente(dip_id: int, db: Session = Depends(get_db)):
    dip = db.query(models.Dipendenti).filter_by(id=dip_id).first()
    if not dip:
        raise HTTPException(status_code=404, detail="Dipendente non trovato")
    db.delete(dip)
    db.commit()
    return {"detail": "Dipendente eliminato"}
