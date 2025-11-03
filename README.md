# task-management-system-183027-183037

SQLite database and Node-based db_visualizer server that also exposes the Tasks REST API used by the React frontend.

Initialize the SQLite database
From: task-management-system-183027-183037/to_do_db

- Create/verify the DB and seed tasks:
  python3 init_db.py

- This will create:
  - myapp.db (SQLite database)
  - db_visualizer/sqlite.env with: export SQLITE_DB="<absolute-path-to-myapp.db>"

Run the backend (db_visualizer + Tasks API)
From: task-management-system-183027-183037/to_do_db/db_visualizer

- Install dependencies (first time only):
  npm install

- Ensure SQLITE_DB is set in your shell:
  source sqlite.env
  echo "Using SQLITE_DB=$SQLITE_DB"

- Start the server (defaults to port 4000):
  PORT=4000 npm start
  # Server starts at http://localhost:4000

Key endpoints
- Tasks API (used by frontend):
  GET    /api/tasks
  POST   /api/tasks
  PUT    /api/tasks/:id
  PATCH  /api/tasks/:id/toggle
  DELETE /api/tasks/:id

- Database viewer (multi-DB support; requires env vars for each DB type):
  GET    /api/databases
  GET    /api/:db/tables
  GET    /api/:db/tables/:table/data?limit=50

Environment variables
- SQLite:
  SQLITE_DB=/absolute/path/to/myapp.db
- Server:
  PORT=4000

Troubleshooting
- If the server reports "SQLite is not configured. Ensure SQLITE_DB is set in sqlite.env.":
  - Make sure you ran python3 init_db.py and then source db_visualizer/sqlite.env
- If the frontend cannot reach the API:
  - Start this server on port 4000
  - Or set REACT_APP_API_URL in the frontend env to http://<host>:<port>/api
