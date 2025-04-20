from typing import Union

from fastapi import FastAPI

from llms import check_room_availability

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{room_number}/{bloc_id}/{session}")
def read_item(room_number: int, bloc_id: str, session: str):
    # Call the check_room_availability function with the parameters
    response = check_room_availability(room_number, bloc_id, session)
    
    # Return the response, including room number, bloc ID, and session
    return {"room_number": room_number, "bloc_id": bloc_id, "session": session, "response": response}

