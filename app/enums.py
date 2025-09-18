from enum import Enum


class Server(str, Enum):
    AMERICA = 'america'
    EUROPE = 'europe'
    ASIA = 'asia'


class Day(str, Enum):
    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'


class Element(str, Enum):
    PYRO = 'pyro'
    HYDRO = 'hydro'
    ELECTRO = 'electro'
    CRYO = 'cryo'
    DENDRO = 'dendro'
    ANEMO = 'anemo'
    GEO = 'geo'


class Weapon(str, Enum):
    SWORD = 'sword'
    CLAYMORE = 'claymore'
    CATALYST = 'catalyst'
    POLEARM = 'polearm'
    BOW = 'bow'


class WeaponSubStat(str, Enum):
    ATK = 'atk'
    DEF = 'def'
    HP = 'hp'
    CRIT_DMG = 'crit_dmg'
    CRIT_RATE = 'crit_rate'
    ELEMENTAL_MASTERY = 'elemental_mastery'
    ENERGY_RECHARGE = 'energy_recharge'
    PHYSICAL_DMG = 'physical_dmg'
