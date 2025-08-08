from enum import Enum


class Element(str, Enum):
    PYRO = 'pyro'
    HYDRO = 'hydro'
    ELECTRO = 'electro'
    CRYO = 'cryo'
    DENDRO = 'dendro'
    ANEMO = 'anemo'
    GEO = 'geo'


class WeaponType(str, Enum):
    SWORD = 'sword'
    CLAYMORE = 'claymore'
    CATALYST = 'catalyst'
    POLEARM = 'polearm'
    BOW = 'bow'


class WeaponSubStatType(str, Enum):
    ATK = 'atk'
    DEF = 'def'
    HP = 'hp'
    CRIT_DMG = 'crit_dmg'
    CRIT_RATE = 'crit_rate'
    ELEMENTAL_MASTERY = 'elemental_mastery'
    ENERGY_RECHARGE = 'energy_recharge'
    PHYSICAL_DMG = 'physical_dmg'
