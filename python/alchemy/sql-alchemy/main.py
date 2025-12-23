from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
	pass

class UserBase(Base):
	__tablename__ = "users"

	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str] = mapped_column(String(30))


class Human(Base):
    __tablename__ = "humans"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())


class Car(Base):
    __tablename__ = "cars"

    id: Mapped[id] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    owner_id: Mapped[int] = mapped_column(ForeignKey("Human.id"))


joe = Human(name="Joe")
vaz_1111 = Car(name="Ока", owner_id=1)