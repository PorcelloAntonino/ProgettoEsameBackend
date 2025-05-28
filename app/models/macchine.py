from sqlalchemy import String, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Macchine(Base):
    __tablename__ = "Macchine"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String)
    anno: Mapped[int] = mapped_column(Integer)
    telaio: Mapped[str] = mapped_column(String, unique=True)
    data_arrivo: Mapped[Date] = mapped_column(Date)
    marca: Mapped[str] = mapped_column(String)

    magazzino: Mapped["Magazzino"] = relationship(back_populates="macchina")
    vendite: Mapped[list["Vendite"]] = relationship(back_populates="macchina")
    controlli: Mapped[list["MacchineControlli"]] = relationship(back_populates="macchina")
