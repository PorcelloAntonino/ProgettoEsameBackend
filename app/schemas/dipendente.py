from pydantic import BaseModel, EmailStr
from pydantic import EmailStr
from pydantic import ConfigDict

class DipendenteBase(BaseModel):
    nome: str
    cognome: str
    email: EmailStr
    username: str
    admin: bool = False


class DipendenteCreate(DipendenteBase):
    password: str


class DipendenteOut(DipendenteBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str

class PasswordChange(BaseModel):
    old_password: str
    new_password: str

class LoginRequest(BaseModel):
    username: str
    password: str
    model_config = ConfigDict(from_attributes=True)

class UsernameInput(BaseModel):
    username: str