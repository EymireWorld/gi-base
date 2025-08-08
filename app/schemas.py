from typing import Literal

from pydantic import BaseModel

from app.enums import WeaponSubStatType, WeaponType


class WeaponSchema(BaseModel):
    id: int

    name: str
    type: WeaponType
    rarity: Literal[3, 4, 5]

    icon_url: str

    base_attack_min: int
    base_attack_max: int

    substat_type: WeaponSubStatType
    substat_value_min: float
    substat_value_max: float

    passive_name: str
    passive_description_min: str
    passive_description_max: str | None = None
