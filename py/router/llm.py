from fastapi import APIRouter
import subprocess

api = APIRouter()

# /llm?prompt=text prompt
@api.get("/api/llm")
async def execute(prompt):
    output = subprocess.getoutput("bash bin/generate_text.sh \"" + str(prompt) + "\"")
    print(output)
    return output