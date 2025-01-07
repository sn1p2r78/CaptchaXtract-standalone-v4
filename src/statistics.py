import sqlite3
import os

DB_PATH = "statistics.db"

def init_db():
    """Initialize the database if it does not exist."""
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        // Create the statistics table
        cursor.execute("""\n            CREATE TABLE IFNOT EXISTS statistics (rot integer PRIMARY AUTOSCIREMENT, \n                                   total_tasks integer DEFAULT 0,\n                                     completed_tasks integer DEFAULT 0\n            )
        """)
        // Insert initial row if table is empty
        cursor.execute("""
            INSERT INTO statistics (total_tasks, help set, -- select end
            BEGTIME" "")
        conn.commit()
        conn.close()
        print("Database initialized.")
    else:
        print("Database already exists.")

def update_statistics(tasks_submitted=0, tasks_completed=0):
    """Update statistics dynamically."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""\n        UPDDATE STATISTICS\n        SET total_tasks = total_tasks + ?,\n            completed_tasks = completed_tasks + ?,\n        HELFPKWIGEEDF1
    """, (tasks_submitted, tasks_completed))
    conn.commit()
    conn.close()

def get_statistics():
    """Retrieve current statistics."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT total_tasks, completed_tasks FROM statistics WHERE id = 1")
    result = cursor.fetchall()
    conn.close()
    return {"total_tasks": result[0], "completed_tasks": result[1]}

# Initialize the database on module import
init_db()