import getpass
import os
from typing import Union

from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] =os.getenv("API_KEY")

from langchain_groq import ChatGroq
llm = ChatGroq(
    model="compound-beta",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}

def load_system_prompt (prompt: str, prompt_file:str, data_file:str):

    with open(data_file, "r", encoding="utf-8") as df:
        room_data = df.read()

    with open(prompt_file, "r", encoding="utf-8") as file:
        prompt_brut = file.read()
        filled_prompt = prompt_brut.format(availability_data=room_data.strip())
        print(filled_prompt)
    # Assuming the `messages` format is correct for `llm.invoke`
    messages = [
        ("system", filled_prompt),
        ("human", prompt),
    ]

    # Invoke the AI model
    ai_msg = llm.invoke(messages)

    ai_msg
    print(ai_msg.content)
    return (ai_msg.content)

@app.get("/items/{room_number}/{bloc_id}/{session}")
async def check_room_availability(room_number: int, bloc_id: str, session: str):
    # Construct the prompt using the parameters
    prompt = f"Check availability for Room {room_number} in Bloc {bloc_id} for Session {session}"

    # Call the system prompt function to get the AI's response
    response = load_system_prompt(
        prompt=prompt,
        prompt_file="promptcreation/systemprompt.txt",
        data_file="promptcreation/data.txt"
        )
    return {
    "message": f"For Room {room_number} in Bloc {bloc_id} for Session {session}",
    "response": response
}

 
    
    
    
 
