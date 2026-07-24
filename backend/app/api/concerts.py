from fastapi import APIRouter
from pydantic import BaseModel

from app.services.llm import parse_concert_request
from app.services.ticketmaster import search_concerts

router = APIRouter()


@router.get("/concerts")
def get_concerts(
    city: str = None,
    start_date: str = None,
    end_date: str = None,
):
    return search_concerts(
        city, 
        start_date, 
        end_date, 
    )


class SearchRequest(BaseModel):
    message:str


@router.post("/concerts/search")
def search(request: SearchRequest):
    params = parse_concert_request(request.message)

    return search_concerts(
        city=params.city,
        start_date=params.start_date,
        end_date=params.end_date,
    )

    