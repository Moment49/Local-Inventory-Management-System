import mysql.connector
import os
from dotenv import load_dotenv

def create_database(database_name):
    try:
        # Database connection setup
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )
        # Setup database cursor
        mycursor = mydb.cursor()

        # Check if database exists if not create the database
        mycursor.execute(f"""CREATE DATABASE IF NOT EXISTS {database_name}""")
        print(f"Database created")
    
    except mysql.connector.Error as err:
        print(f"Error: cant connect due to {err}")

    return mycursor, mydb
   


# Load Db from env
load_dotenv()
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Create DB
mycursor, mydb = create_database(DATABASE_NAME)


