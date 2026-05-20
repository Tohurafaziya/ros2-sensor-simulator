# ROS2 Sensor Simulator (Dockerized)

Author

Tohura Faziya
Driverless Team, Schanzer Racing e.V.
Email: tohura.faziya@schanzer-racing.de



This project is a simple ROS2-based sensor simulator built using Python. It contains a publisher and subscriber node that communicate in real time. The whole system is containerized using Docker.

---

## 📌 Project Features
- ROS2 Publisher node (generates random sensor values)
- ROS2 Subscriber node (receives and processes data)
- Real-time communication using ROS2 topics
- Launch file to run both nodes together
- Fully Dockerized setup

---

## 📂 Project Structure


src/
└── sensor_pkg/
├── sensor_pkg/
│ ├── publisher.py
│ ├── subscriber.py
│ └── init.py
├── launch/
│ └── sensor_launch.py
├── package.xml
├── setup.py
└── setup.cfg
Dockerfile
README.md



---

## 🚀 How to Run (Docker)

### 1. Build the image
```bash
docker build -t ros2_sensor .

2. Run the container
docker run --rm -it ros2_sensor