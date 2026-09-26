import sqlite3

print("Inserting New Record...")

messages = [
    "SYNC",
    "START",
    "TEST_IDENTIFIER",
    "SESSION_TOKEN",
    "RESEARCH_PAYLOAD",
    "LAB_SAMPLE_DATA",
    "VALIDATION",
    "END"
]

conn = sqlite3.connect("database/optical.db")

cursor = conn.cursor()

# Count existing records
cursor.execute("SELECT COUNT(*) FROM test_logs")
count = cursor.fetchone()[0]

# Select next message in sequence
message = messages[count % len(messages)]

# Sample test values
red_values = [220, 200, 240, 180, 255, 210, 230, 190]
green_values = [65, 50, 80, 40, 100, 60, 75, 45]
blue_values = [100, 90, 110, 70, 120, 95, 105, 85]

ambient_conditions = [
    "Indoor Lighting",
    "Dark Room",
    "Bright Lighting",
    "Controlled Lab",
    "Indoor Lighting",
    "Dark Room",
    "Bright Lighting",
    "Controlled Lab"
]

index = count % len(messages)

red = red_values[index]
green = green_values[index]
blue = blue_values[index]

signals_sent = 120

received_values = [118, 115, 119, 110, 120, 117, 116, 118]
signals_received = received_values[index]

success_rate = round(
    (signals_received / signals_sent) * 100,
    2
)

ambient_light = ambient_conditions[index]

cursor.execute("""
INSERT INTO test_logs
(
    red,
    green,
    blue,
    message,
    signals_sent,
    signals_received,
    success_rate,
    ambient_light
)

VALUES
(
    ?, ?, ?, ?, ?, ?, ?, ?
)
""",
(
    red,
    green,
    blue,
    message,
    signals_sent,
    signals_received,
    success_rate,
    ambient_light
)
)

conn.commit()
conn.close()

print(f"Inserted Message: {message}")
print("Data Inserted Successfully!")