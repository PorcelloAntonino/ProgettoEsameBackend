from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class MacchineControlli(Base):
    __tablename__ = "MacchineControlli"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_macchina: Mapped[int] = mapped_column(ForeignKey("Macchine.id"))
    id_controllo: Mapped[int] = mapped_column(ForeignKey("Controlli.id"))
    completato: Mapped[bool] = mapped_column(Boolean, default=False)
    utente: Mapped[str] = mapped_column(String)
    commento: Mapped[str] = mapped_column(String)

    macchina: Mapped["Macchine"] = relationship(back_populates="controlli")
    controllo: Mapped["Controlli"] = relationship(back_populates="macchine")
