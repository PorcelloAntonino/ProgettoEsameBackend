from pydantic import BaseModel


class MagazzinoBase(BaseModel):
    id_macchina: int
    costo: int


class MagazzinoCreate(MagazzinoBase):
    pass


class MagazzinoOut(MagazzinoBase):
    id: int

    class Config:
        orm_mode = True
