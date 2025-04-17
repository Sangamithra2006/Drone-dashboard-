# Drone Telemetry Dashboard

A real-time dashboard to visualize drone telemetry data including GPS, IMU (pitch, roll, yaw), battery, signal, and more.

## Features

- Live WebSocket data updates
- Real-time location on a Leaflet map
- Orientation chart using Chart.js
- Battery low alert
- Responsive UI

## How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/drone-dashboard.git
   cd drone-dashboard
   ```

2. Serve the `index.html` using any local server:
   ```bash
   npx serve .
   ```

3. Make sure your backend WebSocket server is running at `ws://localhost:8000/ws`.

4. Open in browser:
   ```
   http://localhost:3000
   ```

## Sample WebSocket Data Format

```json
{
  "battery": 11.7,
  "imu": {
    "gyro_x": 0.3,
    "gyro_y": 0.1,
    "gyro_z": -0.2,
    "accel_x": 0.0,
    "accel_y": 9.8,
    "accel_z": 0.2,
    "pitch": 5.6,
    "roll": -2.3,
    "yaw": 45.0
  },
  "gps": {
    "lat": 12.9716,
    "lon": 77.5946,
    "alt": 920.5,
    "speed": 12.4,
    "heading": 180
  },
  "temperature": 36.5,
  "signal": "Strong"
}
```

## License

MIT
