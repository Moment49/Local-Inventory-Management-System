from .config import  mycursor, mydb, DATABASE_NAME


#User the database Instance created
mycursor.execute(f"USE {DATABASE_NAME}")


# Create category Products
mycursor.execute("""CREATE TABLE IF NOT EXISTS products(
                product_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                name VARCHAR(255) NOT NULL,
                category_id INT,
                price DECIMAL(13, 2),
                stock_quantity BIGINT,
                date_created DATETIME,
                FOREIGN KEY(category_id) REFERENCES category(category_id) ON DELETE SET NULL  
                )""")

# Create category Table
mycursor.execute("""CREATE TABLE IF NOT EXISTS category(
                 category_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                 category_name VARCHAR(100) UNIQUE
                 )""")

# mycursor.execute("DROP TABLE category")
# mycursor.execute("DROP TABLE products")
mydb.commit()

# INSERT Category TO DB
def Insert_cat(cat:str):
    mycursor.execute(f"USE {DATABASE_NAME}")
    mycursor.execute("INSERT INTO category(category_name) VALUES(%s)", (cat, ) )
    # Save entry
    mydb.commit()
    # Close connection to the databasse  
    mycursor.close()
    mydb.close()

   
   
