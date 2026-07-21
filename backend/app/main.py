from fastapi import FastAPI

app = FastAPI(title="ProjSpotify API")


@app.get("/health")
def health():
    return {"status": "ok"}
