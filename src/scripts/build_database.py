import os
import sqlite3
from db.database import build_database   # adjust import path as needed

def build_mesh_database():
    print("[buildDatabase] Initializing database...")

    # Resolve data directory and file path
    cwd = os.getcwd()
    db_dir = os.path.join(cwd, "data")
    db_file = os.path.join(db_dir, "meshmanager.db")

    # Ensure data directory exists
    if not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
        print(f"[buildDatabase] Created data directory at {db_dir}")

    # Opening the DB will create the file if it doesn't exist
    print(f"[buildDatabase] Creating or opening database at {db_file}...")
    conn = sqlite3.connect(db_file)

    try:
        build_database(conn)
        print("[buildDatabase] ✅ Database build complete.")
    except Exception as err:
        print(f"[buildDatabase] ❌ Failed to build database: {err}")
    finally:
        conn.close()

if __name__ == "__main__":
    build_mesh_database()
