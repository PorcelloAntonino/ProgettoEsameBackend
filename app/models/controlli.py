from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Controlli(Base):
    __tablename__ = "Controlli"

    id: Mapped[int] = mapped_column(primary_key=True)
    titolo_controllo: Mapped[str] = mapped_column(String)
    descrizione: Mapped[str] = mapped_column(String)
    controllo_comune: Mapped[bool] = mapped_column(Boolean, default=False)

    macchine: Mapped[list["MacchineControlli"]] = relationship(back_populates="controllo")
