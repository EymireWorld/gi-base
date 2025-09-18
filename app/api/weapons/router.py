from fastapi import APIRouter, Path, Query

from app.cache.decorator import cache
from app.dependencies import session_dep
from app.enums import WeaponSubStat
from app.schemas import WeaponSchema

from . import services


router = APIRouter()


@router.get('')
@cache(ignore_kwargs=['session'])
async def get_weapons(
    session: session_dep,
    offset: int = Query(0, ge=0),
    limit: int = Query(10, gt=0, le=100),
    rarity: int | None = Query(None, ge=3, le=5),
    substat_name: WeaponSubStat | None = None,
) -> list[WeaponSchema]:
    weapons = await services.get_weapons(
        session,
        offset,
        limit,
        rarity,
        substat_name,
    )

    return weapons  # type: ignore


@router.get('/{id}')
@cache(ignore_kwargs=['session'])
async def get_weapon(
    session: session_dep,
    weapon_id: int = Path(alias='id'),
) -> WeaponSchema:
    weapon = await services.get_weapon(
        session,
        weapon_id,
    )

    return weapon  # type: ignore
