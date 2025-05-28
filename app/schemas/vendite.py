from pydantic import BaseModel
from datetime import date


class VenditaBase(BaseModel):
    id_macchina: int
    data_vendita: date
    compratore: str


class VenditaCreate(VenditaBase):
    pass


class VenditaOut(VenditaBase):
    id: int

    class Config:
        orm_mode = True
