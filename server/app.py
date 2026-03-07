"""FastAPI application serving the TicTacToe OpenEnv environment."""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from server.tictactoe_env import TicTacToeEnvironment

app = FastAPI(title="lebot-gameon", version="0.1.0")
env = TicTacToeEnvironment()

# Serve web UI
app.mount("/static", StaticFiles(directory="web/static"), name="static")


@app.get("/")
async def index():
    return FileResponse("web/static/index.html")


@app.post("/reset")
async def reset():
    return env.reset()


@app.post("/step")
async def step(action: dict):
    return env.step(action)


@app.get("/state")
async def state():
    return env.state()


# WebSocket for real-time UI updates
@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            data = await ws.receive_json()
            if data.get("type") == "reset":
                result = env.reset()
            elif data.get("type") == "move":
                result = env.step({"position": data["position"]})
            else:
                result = {"error": "unknown action"}
            await ws.send_json(result)
    except WebSocketDisconnect:
        pass
