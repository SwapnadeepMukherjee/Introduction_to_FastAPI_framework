# Use HTML to respond in a route
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import logging

app = FastAPI()

@app.get("/")
async def read_root():
    logging.info("Root endpoint accessed")
    return HTMLResponse("<h1>Hello World</h1>")