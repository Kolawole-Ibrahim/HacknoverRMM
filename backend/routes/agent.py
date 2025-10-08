from fastapi import APIRouter

router = APIRouter(prefix="/agents", tags=["Agents"])

agents = []

@router.post("/register")
def register_agent(data: dict):
    agents.append(data)
    return {"status": "registered", "agents": len(agents)}

@router.get("/list")
def list_agents():
    return agents
