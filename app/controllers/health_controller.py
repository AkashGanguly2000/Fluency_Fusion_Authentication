from fastapi import APIRouter

router=APIRouter()

@router.get('/health')
def check_health():
    return "Fluency Fusion Authentication Service is running"
