from pydantic import BaseModel


class MacchinaControlloBase(BaseModel):
    id_macchina: int
    id_controllo: int
    completato: bool
    utente: str
    commento: str


class MacchinaControlloCreate(MacchinaControlloBase):
    pass


class MacchinaControlloOut(MacchinaControlloBase):
    id: int

    class Config:
        orm_mode = True
