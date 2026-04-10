import sqlite3
import os

db_path = "nova_repo/data/nova.db"
conn = sqlite3.connect(db_path)
try:
    conn.execute('''
    CREATE TABLE note_links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_note_id INTEGER NOT NULL,
        target_note_id INTEGER NOT NULL,
        score FLOAT,
        link_type VARCHAR DEFAULT 'ai',
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (source_note_id) REFERENCES notes(id),
        FOREIGN KEY (target_note_id) REFERENCES notes(id)
    )
    ''')
    conn.commit()
    print("Table created")
except Exception as e:
    print("Error:", e)
conn.close()
