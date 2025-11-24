# User & Transactions Relationship Visualization

Graph-based prototype using **Python + FastAPI + Neo4j + Cytoscape.js**.

## 1. Dependencies

- Docker
- Docker Compose
- (Optional) Python 3.11+ if you want to run backend without Docker

## 2. Project Layout

Main folders:

- `backend/` – FastAPI, Neo4j driver, data generator
- `frontend/` – Static site with Cytoscape visualization
- `docker-compose.yml` – Runs Neo4j + backend + frontend

## 3. Run With Docker (recommended)

```bash
# From project root (same folder as docker-compose.yml)
docker-compose up --build
```

Services:

- Neo4j Browser: http://localhost:7474  (user: `neo4j`, pass: `password`)
- API docs (Swagger): http://localhost:8000/docs
- Frontend: http://localhost:3000

## 4. Generate Data (100,000 transactions)

After containers are up:

```bash
curl -X POST "http://localhost:8000/generate-data?users=2000&transactions=100000"
```

This creates:

- Users with shared emails / phones / addresses / payment methods
- 100k transactions
- User-user, user-tx, and tx-tx (IP / device) relationships

## 5. Explore Graph

1. Open the frontend: http://localhost:3000
2. Use the panel:
   - Click **List Users** → pick something like `user_10`
   - Click **Load User Graph** to see all relationships for that user
   - Or pick a transaction (e.g. `tx_50`) and click **Load Transaction Graph**
3. Use **Filters** to toggle:
   - Users / Transactions nodes
   - Shared Attribute links
   - Money flow (SENT / RECEIVED)
   - Transaction-to-Transaction links

## 6. API Summary

- `POST /users` – Add/update user
- `POST /transactions` – Add/update transaction
- `GET /users` – List users (paginated via `limit`, `skip`)
- `GET /transactions` – List transactions (paginated)
- `GET /relationships/user/{id}` – All links for a user
- `GET /relationships/transaction/{id}` – All links for a transaction
- `POST /generate-data` – Generate sample users + transactions

Check full schema in Swagger UI at: http://localhost:8000/docs

## 7. Run Backend Without Docker (optional)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Ensure Neo4j is running somewhere and .env is set correctly
uvicorn app.main:app --reload --port 8000
```

Serve the frontend by opening `frontend/index.html` in a browser or using a simple HTTP server:

```bash
cd frontend
python -m http.server 3000
```
