from fastapi import FastAPI, WebSocket, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("main_page.html", {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    now_val = 1
    await websocket.accept()
    while True:
        data  = await websocket.receive_json()
        await websocket.send_json({
            "id" : now_val,
            "message": data['message']
        })
        now_val += 1
