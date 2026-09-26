import sqlite3

conn = sqlite3.connect("database/optical.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS test_logs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

    red INTEGER,
    green INTEGER,
    blue INTEGER,

    message TEXT,

    signals_sent INTEGER,
    signals_received INTEGER,

    success_rate REAL,

    ambient_light TEXT

)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")