from sqlalchemy.orm import Session
from app import models, schemas


def get_all(db: Session):
    return db.query(models.MacchineControlli).all()


def get_by_id(db: Session, id_: int):
    return db.query(models.MacchineControlli).filter_by(id=id_).first()


def create(db: Session, mc: schemas.macchine_controlli.MacchinaControlloCreate):
    new = models.MacchineControlli(**mc.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


def delete(db: Session, id_: int):
    mc = get_by_id(db, id_)
    if mc:
        db.delete(mc)
        db.commit()
        return True
    return False
