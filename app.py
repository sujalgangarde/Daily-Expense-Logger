from flask import Flask, request, render_template, redirect, url_for
from db.mqsql_conn import get_mysql_connection
import csv, os
from datetime import datetime

app = Flask(__name__)
EXPORT_PATH = "exports/export.csv"

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_mysql_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        data = (
            request.form["description"],
            request.form["merchant"],
            request.form["amount"],
            request.form["date"],
            request.form["method"],
            request.form["notes"],
            request.form["tags"]
        )
        cursor.execute("""
            INSERT INTO expenses (description, merchant, amount, date, method, notes, tags)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, data)
        conn.commit()

    cursor.execute("SELECT * FROM expenses ORDER BY date DESC LIMIT 20")
    expenses = cursor.fetchall()
    conn.close()
    return render_template("index.html", expenses=expenses)

@app.route("/export")
def export():
    from_date = request.args.get("from_date")
    to_date = request.args.get("to_date")

    if not from_date or not to_date:
        return "Please provide both from and to dates"

    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT description, merchant, amount, date, method, notes, tags
        FROM expenses
        WHERE date BETWEEN %s AND %s
    """, (from_date, to_date))
    data = cursor.fetchall()
    conn.close()

    os.makedirs("exports", exist_ok=True)
    with open(EXPORT_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["description", "merchant", "amount", "date", "method", "notes", "tags"])
        writer.writerows(data)

    return f"✅ Exported to: {EXPORT_PATH}"

if __name__ == "__main__":
    os.makedirs("exports", exist_ok=True)
    app.run(debug=True)
