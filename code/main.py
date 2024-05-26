from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello world"}

@app.get("/countries/{country_name}")
async def index(country_name):
    return {"country_name": country_name}