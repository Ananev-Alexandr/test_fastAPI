from fastapi import FastAPI, WebSocket, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("main_page.html", {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    now_val = 1
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"{now_val}: Message: {data}")
        now_val += 1
