from re import sub as re_sub

from sqlalchemy import Enum, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

from app.enums import Day, Weapon, WeaponSubStat


class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(self) -> str:
        temp = re_sub('(.)([A-Z][a-z]+)', r'\1-\2', self.__name__[:-5])
        result = re_sub('([a-z0-9])([A-Z])', r'\1-\2', temp).lower() + 's'

        return result

    id: Mapped[int] = mapped_column(primary_key=True)


class CommonUpgradeMaterialModel(Base):
    group_name: Mapped[str]

    one_name: Mapped[str]
    one_url: Mapped[str]
    two_name: Mapped[str]
    two_url: Mapped[str]
    three_name: Mapped[str]
    three_url: Mapped[str]


class SecondaryWeaponUpgradeMaterialModel(Base):
    group_name: Mapped[str]

    one_name: Mapped[str]
    one_url: Mapped[str]
    two_name: Mapped[str]
    two_url: Mapped[str]
    three_name: Mapped[str]
    three_url: Mapped[str]


class PrimaryWeaponUpgradeMaterialModel(Base):
    one_name: Mapped[str]
    one_url: Mapped[str]
    two_name: Mapped[str]
    two_url: Mapped[str]
    three_name: Mapped[str]
    three_url: Mapped[str]
    four_name: Mapped[str]
    four_url: Mapped[str]

    farm_days: Mapped[list[Day]] = mapped_column(ARRAY(Enum(Day)))


class WeaponModel(Base):
    name: Mapped[str]
    type: Mapped[Weapon]
    rarity: Mapped[int]

    base_attack_min: Mapped[int]
    base_attack_max: Mapped[int]

    substat_name: Mapped[WeaponSubStat]
    substat_value_min: Mapped[float]
    substat_value_max: Mapped[float]

    icon_url: Mapped[str]

    passive_name: Mapped[str]
    passive_description_min: Mapped[str]
    passive_description_max: Mapped[str | None] = mapped_column(default=None)

    common_upgrade_material_id: Mapped[int] = mapped_column(
        ForeignKey('common-upgrade-materials.id')
    )
    secondary_upgrade_material_id: Mapped[int] = mapped_column(
        ForeignKey('secondary-weapon-upgrade-materials.id')
    )
    primary_upgrade_material_id: Mapped[int] = mapped_column(
        ForeignKey('primary-weapon-upgrade-materials.id')
    )
