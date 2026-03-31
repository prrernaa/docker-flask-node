# Docker + Node.js + Flask + MongoDB

A full-stack dockerized project with a **Node.js/Express frontend** and **Flask backend**, connected via Docker Compose on the same network, with data stored in **MongoDB Atlas**.

## Project Structure
```
docker-flask-node/
├── backend/
│   ├── app.py              # Flask backend API
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Backend Docker image
├── frontend/
│   ├── index.js            # Express server
│   ├── package.json        # Node.js dependencies
│   ├── views/
│   │   ├── index.ejs       # Form page
│   │   └── success.ejs     # Success page
│   └── Dockerfile          # Frontend Docker image
├── docker-compose.yaml     # Connects both services
├── .gitignore
└── README.md
```

## How It Works
```
User visits localhost:3000
        ↓
Node.js/Express (Frontend)
        ↓ POST /submit
Flask Backend (port 5000)
        ↓
MongoDB Atlas (stores data)
        ↓
Success response back to user
```

## Setup & Run

### Prerequisites
- Docker
- Docker Compose
- MongoDB Atlas account

### 1. Clone the repo
```bash
git clone git@github.com:prrernaa/docker-flask-node.git
cd docker-flask-node
```

### 2. Add your MongoDB URI
Edit `docker-compose.yaml` and replace the MONGO_URI:
```yaml
- MONGO_URI=mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/flask_assignment
```

### 3. Run with Docker Compose
```bash
docker-compose up --build
```

### 4. Visit the app
Open **http://localhost:3000**

## Docker Hub Images
```bash
docker pull prrernaa/flask-backend:latest
docker pull prrernaa/node-frontend:latest
```

## API Routes

| Service  | Route     | Method | Description                 |
|----------|-----------|--------|-----------------------------|
| Frontend | /         | GET    | Show the submission form    |
| Frontend | /submit   | POST   | Forward data to Flask       |
| Backend  | /submit   | POST   | Save data to MongoDB        |
| Backend  | /health   | GET    | Health check                |

## Tech Stack

| Layer     | Technology        |
|-----------|-------------------|
| Frontend  | Node.js + Express |
| Backend   | Python + Flask    |
| Database  | MongoDB Atlas     |
| DevOps    | Docker + Compose  |


## ☸️ Kubernetes Deployment (Minikube)

This project is also deployed using Kubernetes locally via Minikube.

### 📦 Architecture (Kubernetes)

```
Browser
   ↓
Frontend Service (NodePort)
   ↓
Frontend Pod (Node.js)
   ↓
Backend Service (ClusterIP)
   ↓
Backend Pod (Flask)
   ↓
MongoDB Service (ClusterIP)
   ↓
MongoDB Pod
```

---

### 🚀 Steps to Run (Kubernetes)

#### 1. Start Minikube

```
minikube start
eval $(minikube docker-env)
```

#### 2. Build Docker Images

```
docker build -t backend:v1 ./backend
docker build -t frontend:v1 ./frontend
```

#### 3. Deploy to Kubernetes

```
kubectl apply -f k8s/
```

#### 4. Verify Deployment

```
kubectl get pods
kubectl get svc
```

#### 5. Access Application

```
minikube service frontend-service
```

---

### 📌 Services Used

| Component        | Type      | Purpose         |
| ---------------- | --------- | --------------- |
| frontend-service | NodePort  | Expose UI       |
| backend-service  | ClusterIP | Internal API    |
| mongo-service    | ClusterIP | Database access |

---

### ⚠️ Important Notes

* Frontend communicates with backend using:

  ```
  http://backend-service:5000
  ```
* Backend connects to MongoDB using:

  ```
  mongodb://mongo-service:27017
  ```
* `localhost` is NOT used inside Kubernetes for service communication.

---

## 🧠 Design Decisions

* **Why separate frontend and backend deployments?**
  They scale independently and can be updated without affecting each other.

* **Why use Services instead of localhost?**
  Kubernetes assigns dynamic IPs to pods, so Services provide stable DNS-based communication.

* **Why NodePort for frontend?**
  Frontend must be accessible from browser (external access).

* **Why ClusterIP for backend and MongoDB?**
  These are internal services and should not be exposed publicly.

---

## 🛠️ Common Issues & Fixes

* **ImagePullBackOff**

  * Cause: Image not available in Minikube Docker
  * Fix: Run `eval $(minikube docker-env)` and rebuild images

* **404 Error**

  * Cause: Incorrect API route
  * Fix: Use `/health` or `/submit`

* **500 Internal Server Error**

  * Cause: Missing `MONGO_URI`
  * Fix: Add environment variable in backend deployment

---

## 🔗 Kubernetes Learning Outcome

This project demonstrates:

* Containerization using Docker
* Orchestration using Kubernetes
* Service-to-service communication using DNS
* Environment variable management
* Debugging real deployment issues


