from .config import mydb

mycursor = mydb.cursor()
# Execute SQL statements using the execute() method on the cursor

# ADD PRODUCT TO DB



# Close connection to the databasse  
mycursor.close()
mydb.close()