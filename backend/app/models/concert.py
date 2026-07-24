from pydantic import BaseModel


class Concert(BaseModel):
    name: str
    date: str | None = None
    time: str | None = None
    venue: str | None = None
    city: str | None = None
    ticket_url: str | None = None
    image: str | None = None