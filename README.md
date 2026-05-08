# Docker + Node.js + Flask Deployment Project

A full-stack DevOps project demonstrating deployment of a containerized application using multiple deployment strategies including:

* Local development
* Docker Compose
* AWS EC2
* AWS ECS Fargate
* Amazon ECR
* Kubernetes (Minikube)

---

# AWS Deployment Assignment

This project was deployed using multiple AWS deployment strategies as part of a DevOps assignment.

---

# Task 1 — Single EC2 Deployment

## Objective

Deploy frontend and backend on a single Amazon EC2 instance.

## Deployment Details

* Flask backend deployed on port 5000
* Node.js frontend deployed on port 3000
* Both services hosted on the same EC2 instance

## Technologies Used

* Amazon EC2
* Ubuntu
* Flask
* Node.js
* Express

---

# Task 2 — Separate EC2 Deployment

## Objective

Deploy frontend and backend on separate EC2 instances.

## Deployment Details

* Backend deployed on dedicated EC2 instance
* Frontend deployed on separate EC2 instance
* Frontend communicates with backend using backend public IP

## Technologies Used

* Amazon EC2
* Security Groups
* Public IP communication

---

# Task 3 — ECS Fargate Deployment

## Objective

Deploy Dockerized frontend and backend applications using AWS ECS Fargate and Amazon ECR.

## Deployment Details

* Docker images pushed to Amazon ECR
* Containers deployed using AWS ECS Fargate
* Public networking configured using Security Groups
* Backend exposed on port 5000
* Frontend exposed on port 3000

## AWS Services Used

* Amazon ECR
* Amazon ECS Fargate
* IAM
* Security Groups
* CloudFormation

---

# Project Structure

```text
docker-flask-node/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.js
│   ├── package.json
│   ├── views/
│   │   ├── index.ejs
│   │   └── success.ejs
│   └── Dockerfile
├── docker-compose.yaml
├── k8s/
├── .gitignore
└── README.md
```

---

# Application Architecture

```text
User Browser
     ↓
Node.js Frontend (Port 3000)
     ↓
Flask Backend API (Port 5000)
```

---

# Tech Stack

| Layer              | Technology         |
| ------------------ | ------------------ |
| Frontend           | Node.js + Express  |
| Backend            | Python Flask       |
| Containerization   | Docker             |
| Orchestration      | Docker Compose     |
| Cloud Platform     | AWS                |
| Container Registry | Amazon ECR         |
| Container Runtime  | Amazon ECS Fargate |
| Kubernetes         | Minikube           |

---

# Local Development Setup

## Clone Repository

```bash
git clone https://github.com/prrernaa/docker-flask-node.git
cd docker-flask-node
```

---

# Backend Setup

```bash
cd backend
python3 app.py
```

Backend runs on:

```text
http://localhost:5000
```

Health API:

```text
http://localhost:5000/health
```

---

# Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs on:

```text
http://localhost:3000
```

---

# Docker Setup

## Build Backend Image

```bash
docker build -t flask-backend ./backend
```

## Build Frontend Image

```bash
docker build -t node-frontend ./frontend
```

---

# Docker Compose

Run both services together:

```bash
docker-compose up --build
```

---

# Docker Compose Architecture

```text
Browser
   ↓
Frontend Container
   ↓
Backend Container
```

---

# Amazon ECR Images

## Backend Image

```text
880690593684.dkr.ecr.us-east-1.amazonaws.com/flask-backend:latest
```

## Frontend Image

```text
880690593684.dkr.ecr.us-east-1.amazonaws.com/node-frontend:latest
```

---

# ECS Deployment Configuration

## ECS Cluster

```text
docker-assignment-cluster
```

## Launch Type

```text
AWS Fargate
```

---

# Backend ECS Configuration

| Parameter       | Value              |
| --------------- | ------------------ |
| Task Definition | flask-backend-task |
| Container Port  | 5000               |
| CPU             | 0.25 vCPU          |
| Memory          | 0.5 GB             |

---

# Frontend ECS Configuration

| Parameter       | Value              |
| --------------- | ------------------ |
| Task Definition | node-frontend-task |
| Container Port  | 3000               |
| CPU             | 0.25 vCPU          |
| Memory          | 0.5 GB             |

---

# Security Group Rules

## Backend Security Group

| Type       | Port | Source    |
| ---------- | ---- | --------- |
| Custom TCP | 5000 | 0.0.0.0/0 |

## Frontend Security Group

| Type       | Port | Source    |
| ---------- | ---- | --------- |
| Custom TCP | 3000 | 0.0.0.0/0 |

---

# Kubernetes Deployment (Minikube)

This project also supports Kubernetes deployment locally using Minikube.

---

# Start Minikube

```bash
minikube start
eval $(minikube docker-env)
```

---

# Build Images

```bash
docker build -t backend:v1 ./backend
docker build -t frontend:v1 ./frontend
```

---

# Deploy Kubernetes Resources

```bash
kubectl apply -f k8s/
```

---

# Verify Kubernetes Deployment

```bash
kubectl get pods
kubectl get svc
```

---

# Access Application

```bash
minikube service frontend-service
```

---

# Kubernetes Architecture

```text
Browser
   ↓
Frontend Service (NodePort)
   ↓
Frontend Pod
   ↓
Backend Service (ClusterIP)
   ↓
Backend Pod
```

---

# Challenges Faced

| Issue                     | Resolution                                                    |
| ------------------------- | ------------------------------------------------------------- |
| MongoDB connection issues | Temporarily bypassed DB integration during deployment testing |
| ECS networking timeout    | Corrected Security Group inbound rules                        |
| ECR token expiration      | Re-authenticated Docker using AWS CLI                         |
| Public access issue       | Enabled public IP and configured inbound rules                |

---

# Key Learnings

* Docker containerization
* Docker Compose networking
* ECS Fargate deployment
* ECR image management
* Security Group configuration
* Public vs private networking
* Cloud deployment debugging
* Kubernetes service communication

---

# Deployment URLs

## Task 1 — Single EC2

```text
ADD_SINGLE_EC2_URL_HERE
```

## Task 2 — Frontend EC2

```text
ADD_FRONTEND_EC2_URL_HERE
```

## Task 2 — Backend EC2

```text
ADD_BACKEND_EC2_HEALTH_URL_HERE
```

## Task 3 — ECS Frontend

```text
ADD_ECS_FRONTEND_URL_HERE
```

## Task 3 — ECS Backend

```text
ADD_ECS_BACKEND_HEALTH_URL_HERE
```

---

# GitHub Repository

Repository URL:

```text
https://github.com/prrernaa/docker-flask-node
```

---

# Conclusion

This project demonstrates complete end-to-end DevOps workflow including:

* Application development
* Docker containerization
* Local orchestration
* AWS cloud deployment
* ECS Fargate deployment
* Kubernetes deployment
* Infrastructure debugging

The project helped build practical understanding of modern deployment workflows and cloud-native application management.
