from fastapi import APIRouter, Depends
from app.models.blockchain import ProtocolRequest
from app.services.analytics import analyze_upgrade

router = APIRouter()

@router.post("/analyze")
async def analyze_protocol_upgrade(request: ProtocolRequest):
    """Endpoint for upgrade analysis"""
    return await analyze_upgrade(request)