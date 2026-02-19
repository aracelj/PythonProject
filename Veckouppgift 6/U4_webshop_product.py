#Creates a class that has Products, Order, Shopping Cart

class Product:
    def __init__(self, product, product_id, price):
        self.product = product
        self.product_id = product_id
        self.id = id
        self.price = price

    def print_info(self):
        print(f"{self.product} (ID: {self.product_id})  Price: {self.price}")

class ShoppingCart:
    def __init__(self, order_id):
        self.order_id = order_id
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def product_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
        _
    def get_products(self):
        return self.products

p = Product("Banana", 100, 5)
p.print_info()