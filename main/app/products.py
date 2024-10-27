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

    @classmethod
    def category_add(cls, cat):
        if not cat in cls.category:
            cls.category.append(cat)
            print(type(cat))

            #Add to db
            database.Insert_cat(cat)
            return cat
        else:
            return "Category exists go ahead and add item",cat
    
    def add_product(self, category, **product_info):
        for cat in self.category:
            if category == cat:
                product_info['product_name'] = self._name
                product_info['price'] = self._price
                product_info['stock_quantity'] = self.stock_quantity
                product_info['category'] = category

                # Append all the product
                Product.all_products.append(product_info)

                # Get the connection
                mydb, mycursor = database.get_database_connection()
                # Get the category from the database 
                mycursor.execute("""SELECT * FROM category WHERE category_name = %s""", (category, ))
                cate = mycursor.fetchone()
                cate_id = cate[0]
                # Add product to db
                database.Insert_product(self._name, self._price, cate_id, self.stock_quantity)
                return product_info
     
        
        