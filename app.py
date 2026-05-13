from fastapi import FastAPI

from pydantic import BaseModel

from trip_planner.agent.agent_executor import (
    run_agent
)

app = FastAPI(
    title="AI Trip Planner"
)


class TravelRequest(BaseModel):

    query: str


@app.get("/")
def home():

    return {
        "message": "AI Trip Planner Backend Running"
    }


@app.post("/travel-planner")
def travel_planner(request: TravelRequest):

    response = run_agent(
        request.query
    )

    return {
        "response": response
    }