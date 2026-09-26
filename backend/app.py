from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def dashboard():

    conn = sqlite3.connect("database/optical.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM test_logs
    ORDER BY id DESC
    LIMIT 1
    """)

    row = cursor.fetchone()

    if row:
        reliability = (
        row[7] / row[6] * 100
        if row[6] > 0
        else 0
        )

    conn.close()

    if row:

        data = {

            "transmitter_status": "Online",

            "receiver_status": "Online",

            "current_test": "Baseline Test",

            "red": row[2],
            "green": row[3],
            "blue": row[4],

            "last_message": row[5],

            "signals_sent": row[6],
            "signals_received": row[7],

            "success_rate": row[8],

            "ambient_light": row[9],

            "accuracy": row[8],

            "reliability": round(reliability, 2)
        }

    else:

        data = {

            "transmitter_status": "Offline",

            "receiver_status": "Offline",

            "current_test": "No Data",

            "red": 0,
            "green": 0,
            "blue": 0,

            "last_message": "N/A",

            "signals_sent": 0,
            "signals_received": 0,

            "success_rate": 0,

            "ambient_light": "Unknown",

            "accuracy": 0
        }

    print(data)
    return render_template(
        "index.html",
        data=data
    )


@app.route("/history")
def history():

    conn = sqlite3.connect("database/optical.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM test_logs
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    conn.close()

    reliability_data = []

    for row in records:
        sent = row[6]
        received = row[7]

        if sent > 0:
            reliability = round((received / sent) * 100, 2)
        else:
            reliability = 0

        reliability_data.append(reliability)

    return render_template(
        "historical.html",
        records=records,
        reliability_data=reliability_data[::-1]
)

if __name__ == "__main__":
    app.run(debug=True)
