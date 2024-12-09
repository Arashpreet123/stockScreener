# app/db.py
import pyodbc

def get_db_connection():
    try:
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=LEAGUE321\MSSQLSERVER02;'  # Replace with your server
            'DATABASE=stockApp;'  # Replace with your database
            'Trusted_Connection=yes;'  # Replace with your password
        )
        return connection
    except pyodbc.Error as e:
        print("Error connecting to the database:", e)
        raise

def fetch_all(table_name):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"SELECT * FROM {table_name} WHERE user_id = 1"
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in rows]
        cursor.close()
        conn.close()
        return results
    except Exception as e:
        print(f"Error fetching data from table {table_name}: {e}")
        raise