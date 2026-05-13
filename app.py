from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

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

    try:

        response = run_agent(
            request.query
        )

        return JSONResponse(
            content={
                "response": response
            }
        )

    except Exception as e:

        return JSONResponse(

            status_code=500,

            content={
                "error": str(e)
            }
        )