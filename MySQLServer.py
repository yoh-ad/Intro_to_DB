import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server (no SELECT/SHOW anywhere)
        connection = mysql.connector.connect(
            host='localhost',  # update if needed
            user='root',       # update if needed
            password=''        # update if needed
        )
        cursor = connection.cursor()

        # Create database safely, no SELECT/SHOW statements used
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
