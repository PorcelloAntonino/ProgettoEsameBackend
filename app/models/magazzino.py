from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Magazzino(Base):
    __tablename__ = "Magazzino"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_macchina: Mapped[int] = mapped_column(ForeignKey("Macchine.id"))
    costo: Mapped[int] = mapped_column(Integer)

    macchina: Mapped["Macchine"] = relationship(back_populates="magazzino")
