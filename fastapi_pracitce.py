# Import FastAPI 
from fastapi import FastAPI  
import logging

# Create app instance
app = FastAPI()

# Define a route using the @app.get decorator
@app.get("/")  
def read_root():
    logging.info("Root endpoint accessed")
    return {"hello": "world"}
