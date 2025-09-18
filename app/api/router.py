from fastapi import APIRouter

from .main.router import router as main_router
from .materials.router import router as materials_router
from .weapons.router import router as weapons_router


router = APIRouter()

router.include_router(
    main_router,
    tags=['Main'],
)
router.include_router(
    weapons_router,
    prefix='/weapons',
    tags=['Weapons'],
)
router.include_router(
    materials_router,
    prefix='/materials',
    tags=['Materials'],
)
