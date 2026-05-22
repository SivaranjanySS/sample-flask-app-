from fastapi import FastAPI, Request
import os

app = FastAPI()

@app.post("/webhook")
async def github_webhook(request: Request):

    data = await request.json()

    print("GitHub push detected")

    os.system("python auto_deploy.py")

    return {"message": "Deployment triggered"}
