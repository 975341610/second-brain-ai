import sqlite3
import os

db_path = "nova_repo/data/nova.db"
conn = sqlite3.connect(db_path)
try:
    conn.execute("ALTER TABLE note_links ADD COLUMN link_type VARCHAR DEFAULT 'ai'")
    conn.commit()
    print("Column added")
except Exception as e:
    print("Error:", e)
conn.close()
