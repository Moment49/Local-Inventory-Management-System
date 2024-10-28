from database import database
import mysql.connector

class Product:
    all_products = []
    category = []
    def __init__(self):
        self._name = ''
        self._price = 0
        self.stock_quantity = 0   
    
    def __repr__(self):
        return f'category : {self.category}, product : {self._name}, price : ${self._price}, quantity remaining {self.stock_quantity}'

    def add_product(self, category, name, price, stock_quantity, **product_info):
        self._name = name
        self._price = price
        self.stock_quantity = stock_quantity
        mydb, mycursor = database.get_database_connection()
        mycursor.execute("""SELECT * FROM category WHERE category_name = %s""", (category, ))
        cate_all = mycursor.fetchone()
        if cate_all:
            cate_id = cate_all['category_id']
            if cate_all['category_name'] == category:
                product_info['product_name'] = self._name
                product_info['price'] = self._price
                product_info['stock_quantity'] = self.stock_quantity
                product_info['category'] = category

                # Append all the product
                Product.all_products.append(product_info)
                # Add product to db
                database.Insert_product(self._name, self._price, cate_id, self.stock_quantity)

        return Product.all_products, 'Product added succesfully'
            
    @classmethod
    def category_add(cls, cat):
       if cat not in cls.category:
            database.Insert_cat(cat)
            print(f"Category Added: {cat}")
            cls.category.append(cat)

    @classmethod
    def view_products(cls):
        all_products = database.view_all_products()
        if all_products:
            print("\nALL PRODUCTS IN INVENTORY:")
            for products in all_products:
                print(f"""Product_name:{products['name']}, Price:${products['price']}
            Stock_quantity:{products['stock_quantity']}, Category:{products['category_name']}\n""")

    
    def update_product(self, old_name, new_name, new_price):
        # Get the db connection
        mydb, mycursor = database.get_database_connection()
        mycursor.execute("""SELECT * FROM products WHERE name = %s""", (old_name, ))
        product = mycursor.fetchone()
    
        # Update based on name and price
        if product:
            mycursor.execute("""UPDATE products SET name = %s, price = %s WHERE product_id = %s""", (new_name, new_price,product['product_id'], ))
            mydb.commit()
            # close connections
            mycursor.close()
            mydb.close()
        
        return print("Product updated sucessfully...")
            
        
    def delete_product(self, prod_name):
        mydb, mycursor = database.get_database_connection()
        mycursor.execute("""SELECT * FROM products WHERE name = %s""", (prod_name, ))
        prod = mycursor.fetchone()
        if prod:
            mycursor.execute("""DELETE FROM products WHERE name = %s""", (prod_name, ))
            mydb.commit()
            mycursor.close()
            mydb.close()
            return print(f"Product name: {prod_name} deleted successfully")
        else:
            print("Sorry product does not exist")
            
        # close connections
        mycursor.close()
        mydb.close()

    @staticmethod
    def generate_stock_alert():
        mydb, mycursor = database.get_database_connection()
        mycursor.execute("""SELECT * FROM products """)
        all_prod = mycursor.fetchall()
        # print(all_prod)
        for prod in all_prod:
            print(prod)
            if prod['stock_quantity'] < 5:
                print(f"ALERT: {prod['name']} stock level  is low, please restock!!!")
            else:
                continue    
        # close connections
        mycursor.close()
        mydb.close()

    def search_product(self, product_name):
        mydb, mycursor = database.get_database_connection()
        mycursor.execute("""SELECT * FROM products WHERE name LIKE  concat('%', %s, '%')""", (product_name, ))
        searched_products = mycursor.fetchall()
        
        for search_product in searched_products:
            print(f"Product_name: {search_product['name']}, Price: {search_product['price']}, Stock_quantity: {search_product['stock_quantity']}")

        # close connections
        mycursor.close()
        mydb.close()
    
    def sort_product(self):
        mydb, mycursor = database.get_database_connection()
        mycursor.execute("""SELECT * FROM products ORDER BY stock_quantity DESC""")
        sort_products = mycursor.fetchall()
        for sort_product in sort_products:
            print(f"Product_name: {sort_product['name']}, Stock_quantity:{sort_product['stock_quantity']}")
        mycursor.close()
        mydb.close()

