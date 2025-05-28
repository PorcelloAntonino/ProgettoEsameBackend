from sqlalchemy.orm import Session
from app import models, schemas


def get_all(db: Session):
    return db.query(models.Vendite).all()


def get_by_id(db: Session, id_: int):
    return db.query(models.Vendite).filter_by(id=id_).first()


def create(db: Session, v: schemas.vendite.VenditaCreate):
    new = models.Vendite(**v.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


def delete(db: Session, id_: int):
    v = get_by_id(db, id_)
    if v:
        db.delete(v)
        db.commit()
        return True
    return False
