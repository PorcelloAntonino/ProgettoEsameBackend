from pydantic import BaseModel


class ControlloBase(BaseModel):
    titolo_controllo: str
    descrizione: str
    controllo_comune: bool = False


class ControlloCreate(ControlloBase):
    pass


class ControlloOut(ControlloBase):
    id: int

    class Config:
        orm_mode = True
