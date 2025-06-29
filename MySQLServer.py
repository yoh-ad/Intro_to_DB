import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host='localhost',      # update if needed
            user='root',           # update if needed
            password=''            # update if needed
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it does not exist, no SELECT or SHOW used
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
