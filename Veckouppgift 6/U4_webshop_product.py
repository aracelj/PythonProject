#Creates a class that has Products, Order, Shopping Cart
#Prints in table format all ordered items


def print_product_table(products):
    print("PRODUCT LIST")
    print("Product ID | Product Name                      | Unit Price SEK ")
    print("------------------------------------------------------------------")
    grand_total = 0
    for product in products:
        pid = product.get_id()
        price = product.get_price()
        total = price
        grand_total += total

        print(f"{pid:<10} | {product.name:<33} | {price:<6.2f}          ")

    print("-------------------------------------------------------------------")



class Product:
    pid = 1
    def __init__(self, name, price):
        self.__pid = Product.pid
        Product.pid += 1
        self.name = name
        self.price = price

    def get_id(self):
        return self.__pid

    def get_price(self):
        return self.price



class ShoppingCart:
    def __init__(self, pid):
        self.__pid = pid
        self.products = []

    def get_id(self):
        return self.__pid

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_products(self):
        return self.products


class Order:
    def __init__(self, pid, products):
        self.__pid = pid
        self.products = products

    def get_id(self):
        return self.__pid

    def compute_total(self):
        total = 0
        for product in self.products:
            total += product.get_price()
        return total

    def print_order_table(self):
        print(f"Order ID: {self.__pid}")
        print("Product ID | Product Name                      | Unit Price SEK  | Total SEK")
        print("-----------------------------------------------------------------------")
        grand_total = 0
        for product in self.products:
            pid = product.get_id()
            price = product.get_price()
            total = price
            name = product.name
            grand_total += total

            print(f"{pid:<10} | {name:<33} | {price:<6.2f}          | {total:<6.2f} ")

        print("-----------------------------------------------------------------------")
        print(f"{'':<53} Grand Total: {grand_total:.2f} SEK")



class WebShop:
    def __init__(self):
        self.products = []
        self.orders = []

    def add_product(self, product):
        self.products.append(product)

    def create_order(self, cart):
        order_id = len(self.orders) + 1                          #create unique order id
        order = Order(order_id, cart.get_products())             #create order object from the products in the cart
        self.orders.append(order)                                #append it to the order list
        return order



shop = WebShop()

p1 = Product("Screwdriver Set (Multi-bit)", 220)
p2 = Product("Tape Measure (5m)", 100)
p3 = Product("Pliers", 200)
p4 = Product("Hammer", 350)
p5 = Product("Utility Knife", 80)
p6 = Product("Handsaw", 120)
p7 = Product("Allen Key (Hex) Set", 100)
p8 = Product("Toolbox (simple set)", 450)
p9 = Product("Level (Simple spirit", 120)
p10 = Product("Adjustable Wrench", 150)

items = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
print_product_table(items)


cart = ShoppingCart(1)
items = [p1,p2,p3,p4,p5,p6,p10]
for item in items:
    cart.add_product(item)

items = [p2,p3,p4]
for item in items:
    cart.remove_product(item)


order = shop.create_order(cart)
order.print_order_table()