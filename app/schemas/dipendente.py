from typing import Optional

from pydantic import ConfigDict, BaseModel


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class DipendenteBase(BaseModel):
    username: str
    admin: bool



class DipendenteBaseAdmin(DipendenteBase):
    id: int


class UserLogin(DipendenteBase):
    password: str
    model_config = ConfigDict(from_attributes=True)


class UserCreate(DipendenteBase):
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    admin: Optional[bool] = None
    email: Optional[str] = None


class PasswordChange(BaseModel):
    old_password: str
    new_password: str


class Dipendente(DipendenteBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class DipendenteDelete(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)


class DipendenteList(BaseModel):
    dipendenti: list[Dipendente]
    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    username: str
    password: str
    model_config = ConfigDict(from_attributes=True)