from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Dipendenti(Base):
    __tablename__ = "Dipendenti"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String)
    cognome: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    hashed_password: Mapped[str] = mapped_column(String)
    admin: Mapped[bool] = mapped_column(Boolean, default=False)
