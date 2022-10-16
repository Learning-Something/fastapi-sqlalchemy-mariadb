from fastapi import Query
from fastapi_pagination import Params as BaseParams


class Params(BaseParams):
    page: int = Query(1, ge=1, description="Page number")
    size: int = Query(10, ge=1, le=100, description="Page size")
