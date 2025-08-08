from sqlalchemy.orm import Mapped, declarative_base, mapped_column

from app.enums import WeaponSubStatType, WeaponType


Base = declarative_base()


class WeaponModel(Base):
    __tablename__ = 'weapons'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]
    type: Mapped[WeaponType]
    rarity: Mapped[int]

    icon_url: Mapped[str]

    base_attack_min: Mapped[int]
    base_attack_max: Mapped[int]

    substat_type: Mapped[WeaponSubStatType]
    substat_value_min: Mapped[float]
    substat_value_max: Mapped[float]

    passive_name: Mapped[str]
    passive_description_min: Mapped[str]
    passive_description_max: Mapped[str | None] = mapped_column(default=None)
