######################################################################
# Importing Libraries
######################################################################

from fastapi import FastAPI;
from engine.workflow_engine import run_workflow;

######################################################################
# Instantiate the FastAPI Server
######################################################################

app = FastAPI()

@app.post("/process_request")
def process_request(payload: dict):

    user_message = payload["message"]
    sn_data = payload["data"]

    return run_workflow(user_message, sn_data)