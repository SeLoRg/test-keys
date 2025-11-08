from .incidents_router import incidents_router as incidents_router
from fastapi import APIRouter

router = APIRouter(prefix="/v1")
router.include_router(incidents_router)
