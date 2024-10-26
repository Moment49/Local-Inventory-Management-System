from config import  mycursor, mydb, DATABASE_NAME


#User the database Instance created
mycursor.execute(f"USE {DATABASE_NAME}")


# Create category Products
# mycursor.execute("""CREATE TABLE products(
#                 product_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
#                 name VARCHAR(255) NOT NULL,
#                 category_id INT,
#                 price DECIMAL(13, 2),
#                 stock_quantity BIGINT,
#                 date_created DATETIME,
#                 FOREIGN KEY(category_id) REFERENCES category(category_id)  
#                 )""")

# Create category Table
# mycursor.execute("""CREATE TABLE category(
#                  category_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
#                  category_name VARCHAR(100)
#                  )""")

mydb.commit()

# mycursor.execute("""DROP TABLE category""")
# mydb.commit()

# ADD PRODUCT TO DB



# Close connection to the databasse  
mycursor.close()
mydb.close()