import os
import json
from datetime import date

from dotenv import load_dotenv
from openai import OpenAI
from app.models.search import ConcertSearchParams

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))


def parse_concert_request(message: str) -> ConcertSearchParams:
    today = date.today().isoformat()

    system_prompt = f"""Today's date is {today}.

Extract a city and a date range from the user's concert request, if mentioned.

A "weekend" always means Friday, Saturday, and Sunday inclusive — never
just Saturday and Sunday. So "this weekend" should resolve to the Friday,
Saturday, and Sunday of the current week (start_date = that Friday,
end_date = that Sunday). "Next weekend" should resolve to the Friday,
Saturday, and Sunday of the following week.

If today itself is a Friday, Saturday, or Sunday, "this weekend" should
still include the full Friday-to-Sunday span for that same weekend,
even if some of those days have already passed.

Resolve any other relative date phrases (e.g. "next week", "in two weeks")
similarly, always erring toward the fuller/more generous date range
rather than a single day.

If the user doesn't mention a city or dates, leave those fields as null —
do not guess or default them.

Respond with ONLY a JSON object, no other text, matching this schema:
{{"city": "string or null", "start_date": "YYYY-MM-DD or null", "end_date": "YYYY-MM-DD or null"}}"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ],
        response_format={"type": "json_object"},
        temperature=0,
    )

    raw = response.choices[0].message.content.strip()
    data = json.loads(raw)
    print("Parsed params:", data)
    return ConcertSearchParams(**data)