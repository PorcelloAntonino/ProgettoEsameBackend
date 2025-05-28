from pydantic import BaseModel
from datetime import date


class MacchinaBase(BaseModel):
    nome: str
    anno: int
    telaio: str
    data_arrivo: date
    marca: str


class MacchinaCreate(MacchinaBase):
    pass


class MacchinaOut(MacchinaBase):
    id: int

    class Config:
        orm_mode = True
