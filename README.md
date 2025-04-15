
# Drone Telemetry Dashboard

## Overview
A real-time drone dashboard simulation using FastAPI and WebSocket (Python) for backend, and HTML+JavaScript for frontend. It updates every second with live simulated telemetry data.

## Features
- Battery Voltage
- IMU (Roll, Pitch, Yaw)
- GPS (Lat, Long, Altitude)
- Temperature
- Signal Strength

## How to Run
1. Install FastAPI and Uvicorn:
```
pip install fastapi uvicorn
```
2. Run the backend:
```
uvicorn main:app --reload
```
3. Open `index.html` in a browser to view the dashboard.
