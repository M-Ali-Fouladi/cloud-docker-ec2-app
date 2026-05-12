# FastAPI Dockerized Application (AWS EC2 Deployment)

## Overview
This project demonstrates how to containerize and deploy a simple Python web application using **FastAPI**, **Docker**, and **AWS EC2**.  
The goal of the project is to practice core **DevOps and Cloud engineering concepts** such as containerization, infrastructure deployment, and running applications in a cloud environment.

The application is a lightweight REST API that returns a simple response and provides a health check endpoint. It is packaged inside a Docker container and deployed on a cloud server.

---

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- Docker
- AWS EC2
- Git & GitHub

---

## Project Structure

```
fastapi-docker-app
│
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Application Endpoints

**Root endpoint**

```
GET /
```

Response:

```
{
  "message": "Hello from Docker + FastAPI"
}
```

**Health check**

```
GET /health
```

Response:

```
{
  "status": "ok"
}
```

---

## Running the Project Locally

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/fastapi-docker-app.git
cd fastapi-docker-app
```

### 2. Build the Docker image

```
docker build -t fastapi-docker-app .
```

### 3. Run the container

```
docker run -p 8000:8000 fastapi-docker-app
```

### 4. Open the application

```
http://localhost:8000
```

API documentation:

```
http://localhost:8000/docs
```

---

## Cloud Deployment (AWS EC2)

This project can also be deployed on an AWS EC2 instance.

### Steps

1. Launch an EC2 instance (Ubuntu 22.04)
2. Open the following ports in the security group:

```
22   SSH
80   HTTP
8000 Application
```

3. Connect to the server

```
ssh -i key.pem ubuntu@YOUR_PUBLIC_IP
```

4. Install Docker

```
sudo apt update
sudo apt install docker.io -y
```

5. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/fastapi-docker-app.git
cd fastapi-docker-app
```

6. Build the Docker image

```
sudo docker build -t fastapi-app .
```

7. Run the container

```
sudo docker run -d -p 8000:8000 fastapi-app
```

---

## Accessing the Application

After deployment, the application will be available at:

```
http://YOUR_PUBLIC_IP:8000
```

---

## Learning Goals

This project demonstrates practical experience with:

- Building REST APIs with FastAPI
- Containerizing applications using Docker
- Creating Docker images and containers
- Deploying applications on AWS EC2
- Managing cloud servers and networking basics

---

## Author

Your Name  
Cloud / DevOps Enthusiast
```
