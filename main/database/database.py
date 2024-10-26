from config import  mycursor, mydb, DATABASE_NAME


#User the database Instance created
mycursor.execute(f"USE {DATABASE_NAME}")

# Get the neccessary db connection and cursor
# Execute SQL statements using the execute() method on the cursor
mycursor.execute("""CREATE TABLE products(
                product_id INT PRIMARY KEY,
                product_name VARCHAR(255)
                )""")
mydb.commit()

# ADD PRODUCT TO DB



# Close connection to the databasse  
mycursor.close()
mydb.close()