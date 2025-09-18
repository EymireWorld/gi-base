from typing import Literal

from pydantic import BaseModel

from app.enums import Day, Weapon, WeaponSubStat


class Schema(BaseModel):
    id: int


class CommonUpgradeMaterialSchema(Schema):
    name_rarity_one: str
    name_rarity_two: str
    name_rarity_three: str


class SecondaryWeaponUpgradeMaterialSchema(Schema):
    name_rarity_one: str
    name_rarity_two: str
    name_rarity_three: str


class PrimaryWeaponUpgradeMaterialSchema(Schema):
    name_rarity_one: str
    name_rarity_two: str
    name_rarity_three: str
    name_rarity_four: str
    farm_days: list[Day]


class WeaponSchema(Schema):
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

    common_upgrade_material_id: int
    secondary_upgrade_material_id: int
    primary_upgrade_material_id: int
