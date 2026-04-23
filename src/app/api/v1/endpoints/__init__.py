from fastapi import APIRouter
from app.api.v1.endpoints import status, cartesian

router = APIRouter()

router.include_router(status.router, prefix="/status", tags=["Status"])
router.include_router(cartesian.router, prefix="/cartesian", tags=["Cartesian"])
