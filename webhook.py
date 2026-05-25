from fastapi import FastAPI, Request
import os

app = FastAPI()

@app.post("/webhook")
async def github_webhook(request: Request):

    print("GitHub push detected")

    os.system("python3 auto_deploy.py")

    return {"status": "Deployment Started"}
