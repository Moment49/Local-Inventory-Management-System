class Product:
    
    def __init__(self, name, price, stock_quantity, category):
        self._name = name
        self._price = price
        self.stock_quantity = stock_quantity
        self._category = category
        
    def __repr__(self):
        return f'category : {self._category}, product : {self._name}, price : ${self._price}, quantity remaining {self.stock_quantity}'
    
   
    def add_category(self, category_name):
        
        self._category = {}
        
        if category_name in self._category:
            return f'category {category_name} already exist'
        else:
            self._category[category_name] = {}
            
    def add_product(self, category_name, name, price, stock_quantity):
        if category_name not in self._category:
            return f' category {category_name} does not exist, pls create it'
        else:
            self._category[category_name] [self._name] = {self._price: price, self.stock_quantity: stock_quantity}
            return f'product {name} has been added to category {category_name}'
        
    def view_product(self):
        for items in  self._category:
            print(items)
            for goods in self._name:
                print(goods)
    
    def remove_product(self, category_name, product_name)
        if category_name not in self._category:
            if product_name not in category_name:
                return f'product {product_name} does not exist'
            else:
             self._category[category_name]