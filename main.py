from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import random
import asyncio

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint for your frontend HTML
@app.get("/")
def read_root():
    return {"message": "Welcome to the Drone Dashboard API!"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = {
            "battery": round(random.uniform(10.0, 12.6), 2),
            "imu": {
                "roll": round(random.uniform(-180, 180), 2),
                "pitch": round(random.uniform(-90, 90), 2),
                "yaw": round(random.uniform(0, 360), 2)
            },
            "gps": {
                "lat": round(random.uniform(-90, 90), 6),
                "lon": round(random.uniform(-180, 180), 6),
                "alt": round(random.uniform(0, 500), 2)
            },
            "temperature": round(random.uniform(20, 40), 1),
            "signal": random.choice(["Excellent", "Good", "Poor", "No Signal"])
        }
        await websocket.send_json(data)
        await asyncio.sleep(1)

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9000)
