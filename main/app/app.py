from .products import Product
from database import database
import mysql.connector

def main():
    main_prompt = "Welcome the Local Inventory Management store\n"
    main_prompt += "1 - Add new product to Inventory\n"
    main_prompt += "2 - View all Products in Inventory\n"
    main_prompt += "3 - Update a Product in Inventory by name and price\n"
    main_prompt += "4 - Delete a Product from inventory\n"
    main_prompt += "5 - Generate Product alert based on stock level\n"
    main_prompt += "6 - Search for a Product in Inventory by name\n"
    main_prompt += "7 - Sort Products in Inventory by stock quantity \n"
    main_prompt += "8 - Enter (exit or q) to close application\n\n"
    main_prompt += "Select an action to perform: "

    isAppStart = False

    while not isAppStart:
        program_inuput = input(main_prompt)

        if program_inuput == 'exit' or '8' or 'q' or 'Q':
            isAppStart = True
        
        if program_inuput == '1':
            product_cat = input("Enter product category: ")
            # Get the connection
            mydb, mycursor = database.get_database_connection()
            # Get the category from the database 
            mycursor.execute("""SELECT * FROM category WHERE category_name = %s""", (product_cat, ))
            cate = mycursor.fetchone()
            if not cate:
                user_category = Product.category_add(product_cat.title())
                # Get user Product 
                product_name = input("Enter product name: ")
                product_price = input("Enter product price: ")
                stock_quantity = input("Enter stock quantity: ")

                # Create a product Instance
                product_user = Product()
                # Add product
                product_info = product_user.add_product(user_category,product_name, product_price, stock_quantity)
                print(product_info)
            else:
                user_cate = cate['category_name']
                print(user_cate)
                print("Category exists")
                 # Get user Product 
                product_name = input("Enter product name: ")
                product_price = input("Enter product price: ")
                stock_quantity = input("Enter stock quantity: ")
               
                # Create a product instance
                product = Product()
                 # Add Product
                product_info = product_user.add_product(user_cate, product_name, product_price, stock_quantity)
                print(product_info)

        
        elif program_inuput == '2':
            # Call the view products methods
            Product.view_products()
        
        elif program_inuput == '3':
            print("Update a product by name and price:")
            old_name = input("Enter product name to update: ")
            new_prod_name = input("Enter new product name: ")
            new_price = float(input("Enter new product price: "))
            # Create the Product instance
            product = Product()
            # Update the product
            product.update_product(old_name, new_prod_name, new_price)
        
        elif program_inuput == '4':
            print("Select Product to Delete")
            # Reture a list of products so user can see what product to delete
            Product.view_products()
            user_prod_del = input("Enter a Product name you want to delete: ")
            message = input(f"Are you sure you want to delete {user_prod_del} (yes or no): ")
            if message == 'yes':
                # Create the Product instance
                product= Product()
                # Delete a product
                product.delete_product(user_prod_del)
            elif message == 'no':
                break
        
        elif program_inuput == '5':
            print("Notification for stock level of all products")
            Product.generate_stock_alert()
        
        elif program_inuput == '6':
            # Create the Product instance
            product = Product()
            product_name = input("Enter product name to search: ")
            # Search product name in Inventory
            print(f"Search Results for: {product_name}\n")
            product.search_product(product_name)

        elif program_inuput == '7':
            # Create the Product instance
            product = Product()
            # Sort Products
            print("Sort Porducts by stock level in Descending Order")
            product.sort_product()







if __name__ == "__main__":
    main()