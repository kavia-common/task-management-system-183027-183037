# Verify Tasks API Endpoint

This server already defines the Tasks REST API under the `/api/tasks` prefix and listens on PORT=4000 by default.

Endpoints:
- GET    /api/tasks
- POST   /api/tasks
- PUT    /api/tasks/:id
- PATCH  /api/tasks/:id/toggle
- DELETE /api/tasks/:id

Prerequisites:
1) Initialize the SQLite DB (run from to_do_db):
   python3 init_db.py

2) Start the backend (run from to_do_db/db_visualizer):
   npm install
   source sqlite.env
   PORT=4000 npm start

Quick verification (in a new shell):
curl -i -X POST "http://localhost:4000/api/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title":"Sample task from curl"}'

Expected: HTTP/1.1 201 Created with JSON body of the created task.

If you get "SQLite is not configured" make sure you ran `init_db.py` and then `source db_visualizer/sqlite.env` before starting the server.

Frontend integration notes:
- Ensure the frontend targets http://localhost:4000/api or uses a dev proxy to the backend at port 4000.
- If using Create React App proxy, set "proxy": "http://localhost:4000" in frontend package.json and call fetch("/api/tasks").
- Alternatively set REACT_APP_API_URL=http://localhost:4000/api and call fetch(process.env.REACT_APP_API_URL + "/tasks").
