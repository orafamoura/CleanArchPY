import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """Defining animals Types"""

    dog = ("dog",)
    cat = ("cat",)
    fish = ("fish",)
    turtle = "turtle"


class Pets(Base):  # uma classe com argumento dentro e a heranca
    """Pets Entity"""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return (
            f"Pet [name={self.name},"
            f" specie={self.specie}, "
            f"user_id={self.user_id}]"
        )
