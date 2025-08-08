from fastapi import APIRouter, Path, Query, Request

from app.dependencies import session_dep
from app.enums import WeaponSubStatType
from app.schemas import WeaponSchema

from . import services


router = APIRouter()


@router.get('')
async def get_weapons(
    request: Request,
    session: session_dep,
    offset: int = Query(0, ge=0),
    limit: int = Query(10, gt=0, le=100),
    rarity: int | None = Query(None, ge=3, le=5),
    substat_type: WeaponSubStatType | None = None,
) -> list[WeaponSchema]:
    weapons = await services.get_weapons(
        session,
        offset,
        limit,
        rarity,
        substat_type,
    )

    for weapon in weapons:
        weapon.icon_url = str(request.base_url).rstrip('/') + weapon.icon_url

    return weapons  # type: ignore


@router.get('/{id}')
async def get_weapon(
    request: Request,
    session: session_dep,
    weapon_id: int = Path(alias='id'),
) -> WeaponSchema:
    weapon = await services.get_weapon(
        session,
        weapon_id,
    )

    weapon.icon_url = str(request.base_url).rstrip('/') + weapon.icon_url

    return weapon
