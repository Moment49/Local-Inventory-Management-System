import mysql.connector
import os
from dotenv import load_dotenv

# Load Db from env
load_dotenv()
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")


def create_database(database_name):
    try:
        # Database connection setup
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password='',
        )
        # Setup database cursor
        mycursor = mydb.cursor()

        # Check if database exists if not create the database
        mycursor.execute(f"""CREATE DATABASE IF NOT EXISTS {database_name}""")
        print(f"Database created")
        return mycursor, mydb
    
    except mysql.connector.Error as err:
        print(f"Error: cant connect due to {err}")
        return None, None


    

# Create DB
mycursor, mydb = create_database(DATABASE_NAME)
if mycursor:
    mycursor.close()
    mydb.close()


