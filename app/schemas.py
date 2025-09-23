from typing import Literal

from pydantic import BaseModel

from app.enums import Day, Weapon, WeaponSubStat


class Schema(BaseModel):
    id: int


class CommonUpgradeMaterialModel(Schema):
    group_name: str

    one_name: str
    one_url: str
    two_name: str
    two_url: str
    three_name: str
    three_url: str


class SecondaryWeaponUpgradeMaterialModel(Schema):
    group_name: str

    one_name: str
    one_url: str
    two_name: str
    two_url: str
    three_name: str
    three_url: str


class PrimaryWeaponUpgradeMaterialModel(Schema):
    one_name: str
    one_url: str
    two_name: str
    two_url: str
    three_name: str
    three_url: str
    four_name: str
    four_url: str

    farm_days: list[Day]


class WeaponModel(Schema):
    name: str
    type: Weapon
    rarity: Literal[3, 4, 5]

    base_attack_min: int
    base_attack_max: int

    substat_name: WeaponSubStat
    substat_value_min: float
    substat_value_max: float

    icon_url: str

    passive_name: str
    passive_description_min: str
    passive_description_max: str | None = None

    common_upgrade_material_id: int
    secondary_upgrade_material_id: int
    primary_upgrade_material_id: int
