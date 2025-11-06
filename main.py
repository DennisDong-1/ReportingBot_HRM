from fastapi import FastAPI

var = FastAPI()

@var.get("/")
def root():
    return {"question": "Show me who is on leave today."}