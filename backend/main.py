from fastapi import FastAPI
from routes import agent, comands

app = FastAPI(title="hacknoverRMM API")
app.include_router(agents.router)
app.include_router(commands.router)

@app.get("/")
def root():
    return {"status": "RMM Backend Online"}
