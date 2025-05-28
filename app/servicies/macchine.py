from sqlalchemy.orm import Session
from app import models, schemas


def get_all(db: Session):
    return db.query(models.Macchine).all()


def get_by_id(db: Session, id_: int):
    return db.query(models.Macchine).filter_by(id=id_).first()


def create(db: Session, macchina: schemas.macchine.MacchinaCreate):
    new = models.Macchine(**macchina.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


def delete(db: Session, id_: int):
    m = get_by_id(db, id_)
    if m:
        db.delete(m)
        db.commit()
        return True
    return False
