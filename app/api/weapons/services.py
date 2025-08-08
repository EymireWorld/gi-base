from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.enums import WeaponSubStatType
from app.models import WeaponModel


async def get_weapons(
    session: AsyncSession,
    offset: int,
    limit: int,
    rarity: int | None,
    substat_type: WeaponSubStatType | None,
) -> list[WeaponModel]:
    stmt = select(WeaponModel).order_by(WeaponModel.id.asc()).offset(offset).limit(limit)

    if rarity:
        stmt = stmt.where(WeaponModel.rarity == rarity)

    if substat_type:
        stmt = stmt.where(WeaponModel.substat_type == substat_type)

    result = await session.execute(stmt)
    result = result.scalars().all()

    return result  # type: ignore


async def get_weapon(
    session: AsyncSession,
    weapon_id: int,
) -> WeaponModel:
    stmt = select(WeaponModel).where(WeaponModel.id == weapon_id)
    result = await session.execute(stmt)
    result = result.scalar_one_or_none()

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Weapons not found.',
        )

    return result
