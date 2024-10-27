from .config import  DATABASE_NAME, DATABASE_PASSWORD
from datetime import datetime
import os
from dotenv import load_dotenv
import mysql.connector


# Get database connection
def get_database_connection():
    # Database connection setup
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=DATABASE_PASSWORD,
        database=DATABASE_NAME
    )
    # Setup database cursor
    mycursor = mydb.cursor()
    return mydb, mycursor





# Create category Products
# mycursor.execute("""CREATE TABLE IF NOT EXISTS products(
#                 product_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
#                 name VARCHAR(255) NOT NULL,
#                 category_id INT,
#                 price DECIMAL(13, 2),
#                 stock_quantity BIGINT,
#                 date_created DATETIME,
#                 FOREIGN KEY(category_id) REFERENCES category(category_id) ON DELETE SET NULL  
#                 )""")

# Create category Table
# mycursor.execute("""CREATE TABLE IF NOT EXISTS category(
#                  category_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
#                  category_name VARCHAR(100) UNIQUE
#                  )""")

# mydb, mycursor = get_database_connection()

# # mycursor.execute("DROP TABLE category")
# # mycursor.execute("DROP TABLE products")
# mydb.commit()
# mycursor.close()
# mydb.close()

# INSERT Category TO DB
def Insert_cat(cat:str):
    mydb, mycursor = get_database_connection()
    mycursor.execute(f"USE {DATABASE_NAME}")
    mycursor.execute("INSERT INTO category(category_name) VALUES(%s)", (cat, ) )
    # Save entry
    mydb.commit()
    # Close connection to the databasse  
    mycursor.close()
    mydb.close()

# INSERT Product TO DB
def Insert_product(name, price, cat_id, stock_qua):
    mydb, mycursor = get_database_connection()
    mycursor.execute(f"USE {DATABASE_NAME}")
    mycursor.execute("INSERT INTO products(name, price, category_id, stock_quantity, date_created) VALUES(%s, %s, %s, %s, NOW())", (name, price, cat_id, stock_qua, ) )
    # Save entry
    mydb.commit()
    # Close connection to the databasse  
    mycursor.close()
    mydb.close()


