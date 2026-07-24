from pydantic import BaseModel


class ConcertSearchParams(BaseModel):
    city: str | None = None
    start_date: str | None = None  # YYYY-MM-DD
    end_date: str | None = None   
    
    