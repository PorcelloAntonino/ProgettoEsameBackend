from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

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

# in caso di stampa(o converti) restituisce questa stingra
#  def __repr__(self):
#      return (f"Utente(id={self.id!r}, username={self.username!r}, admin={self.admin!r},"
#             f" temporaneo={self.temporaneo!r}, gruppo_id={self.gruppo_id!r})")
