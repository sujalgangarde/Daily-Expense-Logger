import mysql.connector

def get_mysql_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",            # your MySQL username
        password="2580",# your MySQL password
        database="expense_tracker"
    )
