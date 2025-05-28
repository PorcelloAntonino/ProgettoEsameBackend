from sqlalchemy.orm import Session
from app import models, schemas


def get_all(db: Session):
    return db.query(models.Dipendenti).all()


def get_by_id(db: Session, dip_id: int):
    return db.query(models.Dipendenti).filter_by(id=dip_id).first()


def create(db: Session, dipendente: schemas.dipendenti.DipendenteCreate):
    new = models.Dipendenti(
        nome=dipendente.nome,
        cognome=dipendente.cognome,
        email=dipendente.email,
        username=dipendente.username,
        hashed_password=dipendente.password + "notreallyhashed",  # esempio hash
        admin=dipendente.admin
    )
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


def delete(db: Session, dip_id: int):
    dip = get_by_id(db, dip_id)
    if dip:
        db.delete(dip)
        db.commit()
        return True
    return False
