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
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}

def load_system_prompt (prompt: str):
    with open("systemprompt.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
    # Assuming the `messages` format is correct for `llm.invoke`
    messages = [
        ("system", content),
        ("human", prompt),
    ]

    # Invoke the AI model
    ai_msg = llm.invoke(messages)

    ai_msg
    print(ai_msg.content)
    return (ai_msg.content)


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    response = load_system_prompt(item_id)
    
    
    # Assuming ai_msg.content returns the AI response as text
    return {"item_id": item_id, "response": response}
