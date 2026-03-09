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
