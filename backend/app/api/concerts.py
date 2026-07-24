from fastapi import APIRouter
from app.services.ticketmaster import search_concerts

router = APIRouter()


@router.get("/concerts")
def get_concerts(
    city: str,
    start_date: str,
    end_date: str,
):
    return search_concerts(
        city,
        start_date,
        end_date,
    )