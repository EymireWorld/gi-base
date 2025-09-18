from collections.abc import Sequence
from datetime import datetime, timedelta, timezone

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.enums import Day, Server
from app.models import (
    CommonUpgradeMaterialModel,
    PrimaryWeaponUpgradeMaterialModel,
    SecondaryWeaponUpgradeMaterialModel,
    WeaponModel,
)


async def get_today_weapons_to_upgrade(
    session: AsyncSession,
    server: Server,
) -> Sequence[WeaponModel]:
    server_to_timezone = {
        Server.AMERICA: timezone(timedelta(hours=8)),
        Server.EUROPE: timezone(timedelta(hours=1)),
        Server.ASIA: timezone(timedelta(hours=-5)),
    }
    day = Day(datetime.now(server_to_timezone[server]).strftime('%A').lower())
    stmt = (
        select(WeaponModel)
        .join(
            PrimaryWeaponUpgradeMaterialModel,
            WeaponModel.primary_upgrade_material_id == PrimaryWeaponUpgradeMaterialModel.id,
        )
        .where(PrimaryWeaponUpgradeMaterialModel.farm_days.contains((day,)))
    )
    result = await session.execute(stmt)
    result = result.scalars().all()

    return result


async def get_weapon_primary_material(
    session: AsyncSession,
    material_id: int,
) -> PrimaryWeaponUpgradeMaterialModel:
    stmt = select(PrimaryWeaponUpgradeMaterialModel).where(
        PrimaryWeaponUpgradeMaterialModel.id == material_id,
    )
    result = await session.execute(stmt)
    result = result.scalar_one_or_none()

    if not result:
        raise HTTPException(
            status_code=404,
            detail='Material not found.',
        )

    return result


async def get_weapon_secondary_material(
    session: AsyncSession,
    material_id: int,
) -> SecondaryWeaponUpgradeMaterialModel:
    stmt = select(SecondaryWeaponUpgradeMaterialModel).where(
        SecondaryWeaponUpgradeMaterialModel.id == material_id,
    )
    result = await session.execute(stmt)
    result = result.scalar_one_or_none()

    if not result:
        raise HTTPException(
            status_code=404,
            detail='Material not found.',
        )

    return result


async def get_common_material(
    session: AsyncSession,
    material_id: int,
) -> CommonUpgradeMaterialModel:
    stmt = select(CommonUpgradeMaterialModel).where(
        CommonUpgradeMaterialModel.id == material_id,
    )
    result = await session.execute(stmt)
    result = result.scalar_one_or_none()

    if not result:
        raise HTTPException(
            status_code=404,
            detail='Material not found.',
        )

    return result
