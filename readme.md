# AI Concert Finder

An AI-powered concert discovery app that lets users search for concerts using natural language.

For example:

> "I'm going to Berlin next weekend. Find me some concerts I'd like."

The application uses an LLM to extract structured search parameters such as location and dates, then searches the Ticketmaster API for relevant events.

## Tech Stack

* Python
* FastAPI
* Ticketmaster Discovery API
* OpenAI API
* React / Next.js

## Architecture

```text
User
  ↓
Natural Language Request
  ↓
LLM → Structured Search Parameters
  ↓
FastAPI
  ↓
Ticketmaster API
  ↓
Concert Recommendations
```

## Planned Features

* Natural language concert search
* Spotify integration for personalised recommendations
* Artist similarity and preference matching
* AI-powered concert recommendations
* OpenAI Agents SDK with API tools
