from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="Verify the server is running properly", response_description="Server health")
def healthcheck():
	return { "status": "healthy" }
