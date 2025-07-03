# 📘 Daily Expense Logger

A simple and efficient web application to **log your daily expenses**, store them in a **MySQL database**, and **export expense data as CSV** for easy tracking and reporting.

---

## 🚀 Features

- Add daily expenses via a web form
- Store expenses securely in MySQL
- View recent expense entries
- Export expenses to CSV by:
  - Custom date range
  - Monthly or yearly selection

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **Flask**
- **MySQL**
- **HTML/CSS (Jinja2)**
- **CSV Export**

---

## 📁 Project Structure

```
daily-expense-logger/
├── app.py                # Main Flask application
├── db/
│   └── mysql_conn.py     # MySQL DB connection helper
├── templates/
│   └── index.html        # Frontend (Jinja2 HTML)
├── exports/
│   └── export.csv        # Generated CSV files
├── requirements.txt      # Python dependencies
└── README.md
```

---

## 🧰 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sujalgangarde/daily-expense-logger.git
cd daily-expense-logger
```

### 2️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create MySQL Database and Table

Login to MySQL and run:

```sql
CREATE DATABASE expense_tracker;

USE expense_tracker;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255),
    merchant VARCHAR(255),
    amount DECIMAL(10,2),
    date DATE,
    method VARCHAR(50),
    notes TEXT,
    tags TEXT
);
```

### 4️⃣ Configure Database Connection

Edit `db/mysql_conn.py` with your MySQL credentials:

```python
return mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="expense_tracker"
)
```

### 5️⃣ Run the Application

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🧪 Usage Guide

### ➕ Add Expenses

Fill in the form fields:
- Description
- Merchant
- Amount
- Date
- Payment method
- Notes (optional)
- Tags (optional)

Click **"Add Expense"** to save to the database.

### 📤 Export CSV

Select:
- From Date
- To Date

Click **"Export CSV"** to download all expenses within the selected range as a CSV file.

Exported file is saved to:
```
/exports/export.csv
```

---

## 🧱 Dependencies

- Flask
- mysql-connector-python

Install using:

```bash
pip install flask mysql-connector-python
```

---

## 📌 Future Improvements

- PDF report generation
- User login/authentication
- Tag filters and category summaries
- Integration with ML-based expense categorizer

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

> **Note:** Replace `https://github.com/sujalgangarde/daily-expense-logger.git` with your actual GitHub repo URL before pushing.