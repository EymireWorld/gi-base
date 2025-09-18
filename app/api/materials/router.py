from fastapi import APIRouter, Path, Query

from app.cache.decorator import cache
from app.dependencies import session_dep
from app.enums import Server
from app.schemas import (
    CommonUpgradeMaterialSchema,
    PrimaryWeaponUpgradeMaterialSchema,
    SecondaryWeaponUpgradeMaterialSchema,
    WeaponSchema,
)

from . import services


router = APIRouter()


@router.get('/today/weapons')
@cache(ignore_kwargs=['session'])
async def get_today_weapons_to_upgrade(
    session: session_dep,
    server: Server = Query(...),
) -> list[WeaponSchema]:
    result = await services.get_today_weapons_to_upgrade(
        session,
        server,
    )

    return result  # type: ignore


@router.get('/weapon/primary/{id}')
@cache(ignore_kwargs=['session'])
async def get_weapon_primary_material(
    session: session_dep,
    material_id: int = Path(alias='id'),
) -> PrimaryWeaponUpgradeMaterialSchema:
    result = await services.get_weapon_primary_material(
        session,
        material_id,
    )

    return result  # type: ignore


@router.get('/weapon/secondary/{id}')
@cache(ignore_kwargs=['session'])
async def get_weapon_secondary_material(
    session: session_dep,
    material_id: int = Path(alias='id'),
) -> SecondaryWeaponUpgradeMaterialSchema:
    result = await services.get_weapon_secondary_material(
        session,
        material_id,
    )

    return result  # type: ignore


@router.get('/common/{id}')
@cache(ignore_kwargs=['session'])
async def get_common_material(
    session: session_dep,
    material_id: int = Path(alias='id'),
) -> CommonUpgradeMaterialSchema:
    result = await services.get_common_material(
        session,
        material_id,
    )

    return result  # type: ignore
