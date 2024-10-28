from database import database
import mysql.connector

class Product:
    all_products = []
    category = []
    def __init__(self, name, price, stock_quantity):
        self._name = name
        self._price = price
        self.stock_quantity = stock_quantity   
    
    def __repr__(self):
        return f'category : {self.category}, product : {self._name}, price : ${self._price}, quantity remaining {self.stock_quantity}'

            
    def add_product(self, category, **product_info):
        mydb, mycursor = database.get_database_connection()
        mycursor.execute("""SELECT * FROM category WHERE category_name = %s""", (category, ))
        cate = mycursor.fetchone()
        cate_id = cate[0]
        if cate[1] == category:
            product_info['product_name'] = self._name
            product_info['price'] = self._price
            product_info['stock_quantity'] = self.stock_quantity
            product_info['category'] = category

            # Append all the product
            Product.all_products.append(product_info)
            # Add product to db
            database.Insert_product(self._name, self._price, cate_id, self.stock_quantity)
            return product_info
        
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

    @classmethod
    def update_product(cls, old_name, new_name, new_price):
        # Get tje db connection
        mydb, mycursor = database.get_database_connection()
        mycursor.execute("""SELECT * FROM products WHERE name = %s""", (old_name, ))
        product = mycursor.fetchone()
    
        # Update based on name and price
        if product:
            mycursor.execute("""UPDATE products SET name = %s, price = %s WHERE product_id = %s""", (new_name, new_price,product['product_id'], ))
            mydb.commit()
            
        return print("Product updated sucessfully...")
    
        
        