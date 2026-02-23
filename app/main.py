from fastapi import FastAPI;
from engine.workflow_engine import run_workflow;

app = FastAPI()

@app.post("/process_request")

def process_request(payload: dict):
    result = run_workflow(payload);
    return result;