import logging

from fastapi.routing import APIRouter

from src.dto.api_response import ApiResponse

logger = logging.getLogger(__name__)


router = APIRouter(prefix = "/api")

@router.get("/hello")
def hello():
    logger.info("hello world")
    return ApiResponse(200, "success", "hello").to_dict()