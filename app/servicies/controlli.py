from sqlalchemy.orm import Session
from app import models, schemas


def get_all(db: Session):
    return db.query(models.Controlli).all()


def get_by_id(db: Session, id_: int):
    return db.query(models.Controlli).filter_by(id=id_).first()


def create(db: Session, c: schemas.controlli.ControlloCreate):
    new = models.Controlli(**c.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


def delete(db: Session, id_: int):
    c = get_by_id(db, id_)
    if c:
        db.delete(c)
        db.commit()
        return True
    return False
