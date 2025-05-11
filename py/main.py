from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from router import llm

app = FastAPI() 

app.include_router(llm.api)
app.mount("/public", StaticFiles(directory="public"), name="public")