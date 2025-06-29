import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (no database specified)
        connection = mysql.connector.connect(
            host='localhost',  # Change if your MySQL host is different
            user='root',       # Change to your MySQL username
            password=''        # Change to your MySQL password
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist (no SELECT or SHOW)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            cursor.close()
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
