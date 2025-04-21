from typing import Union

from fastapi import FastAPI

from llms import check_room_availability

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{preference}")
def read_item(preference:str):
    # Call the check_room_availability function with the parameters
    response = check_room_availability(preference)
    
    # Return the response, including room number, bloc ID, and session
    return {"subject": preference, "response": response}

