from typing import Literal

from pydantic import BaseModel

from app.enums import Weapon, WeaponSubStat


__all__ = ['WeaponSchema']


class WeaponSchema(BaseModel):
    id: int

    name: str
    type: Weapon
    rarity: Literal[3, 4, 5]

    icon_url: str

    base_attack_min: int
    base_attack_max: int

    substat_name: WeaponSubStat
    substat_value_min: float
    substat_value_max: float

    passive_name: str
    passive_description_min: str
    passive_description_max: str | None = None
