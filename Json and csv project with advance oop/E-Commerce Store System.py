class Product:
    def __init__(self, name, product_id, price, quantity):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.quantity = quantity


class Customer:
    def __init__(self, customer_id, first_name, last_name, email, address):
        self.cart = Cart(customer_id)
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.gmail = email
        self.address = address


class Cart:
    def __init__(self, cart_id):
        self.cart_id = cart_id
        self.products = {}

    def add_product(self, product, quantity):

        if product.product_id in self.products:
            existing_quantity = self.products[product.product_id][1]
            if existing_quantity + quantity > product.quantity:
                print("sorry not enough items")
            else:
                self.products[product.product_id][1] += quantity
                print("added to cart")
        else:
            if quantity > product.quantity:
                print("sorry not enough items")
            else:
               self.products.update({product.product_id: [product,quantity]})

    def show_products(self):
     for key, values in self.products.items():
        print(key, values[0].name, values[0].price, values[1])


    def show_total(self):
     total = 0
     for keys, value in self.products.items():
         total += value[0].price * value[1]
     print("your total is", total)
class Order:
    def __init__(self,order_id,h):
        self.order_id = order_id
        self.customer = customer
        self.order_products = {}
        for key, values in self.customer.cart.products.items():
            self.order_products.update({key:values})
        self.total = 0
        for key, values in self.order_products.items():
            self.total += values[0].price * values[1]
    def display_order(self):
        print(self.customer.customer_id)
        print(self.customer.first_name)
        print(self.customer.last_name)
        print(self.customer.gmail)
        print(self.customer.address)
        for key, values in self.order_products.items():
            print(f"product id is {key} \nproduct name is {values[0].name} \nproduct price is { values[0].price} \nquantity is { values[1]}")
        print("total is", self.total)



product1 = Product("mouse", 1, 100, 1)
product2 = Product("keyboard", 2, 300, 1)
customer1 = Customer(1, "dani", "pani", "@h", "lahore")
customer1.cart.add_product(product1, 1)

customer2 = Customer(2, "pani","dani00","@k", "karachi")
customer2.cart.add_product(product2, 1)

order1 = Order(1, customer1)

order1.display_order()
