import os
import requests
from dotenv import load_dotenv

load_dotenv()


def search_concerts(city, start_date, end_date):

    url = "https://app.ticketmaster.com/discovery/v2/events.json"

    params = {
        "apikey": os.getenv("TICKETMASTER_API_KEY"),
        "city": city,
        "classificationName": "music",
        "startDateTime": f"{start_date}T00:00:00Z",
        "endDateTime": f"{end_date}T23:59:59Z",
        "size": 20,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    events = data.get("_embedded", {}).get("events", [])

    concerts = []

    for event in events:

        venue = event.get("_embedded", {}).get(
            "venues", [{}]
        )[0]

        concert = {
            "name": event.get("name"),
            "date": event.get("dates", {})
                              .get("start", {})
                              .get("localDate"),
            "time": event.get("dates", {})
                              .get("start", {})
                              .get("localTime"),
            "venue": venue.get("name"),
            "city": venue.get("city", {})
                           .get("name"),
            "ticket_url": event.get("url"),
            "image": event.get("images", [{}])[0].get("url"),
        }

        concerts.append(concert)

    return concerts