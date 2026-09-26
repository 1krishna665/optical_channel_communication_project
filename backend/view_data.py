import sqlite3

conn = sqlite3.connect("database/optical.db")

cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM test_logs
""")

rows = cursor.fetchall()

print("\n===== DATABASE RECORDS =====\n")

for row in rows:
    print(row)

conn.close()