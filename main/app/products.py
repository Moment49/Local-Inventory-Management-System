from database import database

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
                return product_info
     
        
        
        



# print(Product.all_products)
    # def add_category(self, category):
    #     self._category = {}
        
    #     if category_name in self._category:
    #         return f'category {category_name} already exist'
    #     else:
    #         self._category[category_name] = {}
            
    # def add_product(self, category_name, name, price, stock_quantity):
    #     if category_name not in self._category:
    #         return f' category {category_name} does not exist, pls create it'
    #     else:  
    #         self._category[category_name] [self._name] = {self._price: price, self.stock_quantity: stock_quantity}
    #         return f'product {name} has been added to category {category_name}'
        

    # def view_product(self):
    #     for items in  self._category:
    #         print(items)
    #         for goods in self._name:
    #             print(goods)
    
    # def remove_product(self, category_name, product_name):
    #     if category_name not in self._category:
    #         if product_name not in category_name:
    #             return f'product {product_name} does not exist'
    #         else:
    #          self._category[category_name]