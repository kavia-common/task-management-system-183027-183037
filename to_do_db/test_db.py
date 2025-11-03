#!/usr/bin/env python3
"""Test SQLite database connection and presence of tasks table"""

import sqlite3
import sys
import os

DB_NAME = "myapp.db"

try:
    # Check if database file exists
    if not os.path.exists(DB_NAME):
        print(f"Database file '{DB_NAME}' not found")
        sys.exit(1)
    
    # Connect to database and get version
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT sqlite_version()")
    version = cursor.fetchone()[0]

    # Smoke check: ensure tasks table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks'")
    row = cursor.fetchone()
    if not row:
        print("Smoke check failed: tasks table does not exist")
        conn.close()
        sys.exit(2)

    # Optional: ensure essential columns
    cursor.execute("PRAGMA table_info(tasks)")
    cols = {c[1] for c in cursor.fetchall()}
    required = {"id", "title", "completed", "created_at", "updated_at"}
    missing = required - cols
    if missing:
        print(f"Smoke check failed: tasks table missing columns: {', '.join(sorted(missing))}")
        conn.close()
        sys.exit(3)

    conn.close()
    print(f"SQLite version: {version} | tasks table OK")
    sys.exit(0)
    
except sqlite3.Error as e:
    print(f"Connection failed: {e}")
    sys.exit(1)
