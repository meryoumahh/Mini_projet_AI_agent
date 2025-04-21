from typing import Union

from fastapi import FastAPI

from llms import check_pfe_availability

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/domain/{preference}")
def read_item(preference:str):
    # Call the check_room_availability function with the parameters
    response = check_pfe_availability(preference)
    
    # Return the response, including room number, bloc ID, and session
    return {"for the subject": preference, "response": response}

