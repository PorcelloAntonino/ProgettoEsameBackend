from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Vendite(Base):
    __tablename__ = "Vendite"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_macchina: Mapped[int] = mapped_column(ForeignKey("Macchine.id"))
    data_vendita: Mapped[Date] = mapped_column(Date)
    compratore: Mapped[str] = mapped_column(String)

    macchina: Mapped["Macchine"] = relationship(back_populates="vendite")
