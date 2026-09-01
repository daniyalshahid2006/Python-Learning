import csv
import json
data = {}
with open("data.json","w") as file:
 json.dump(data,file)

class Product:
    def __init__(self, name, product_id, price, quantity):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.quantity = quantity
    def increase_stock(self,new_quantity):
        if new_quantity <= 0:
            print("product cant be negative or zero here")
        else:
            self.quantity += new_quantity
    def decrease_stock(self,new_quantity):
        if new_quantity > self.quantity:
            print("not enough stock")
        elif new_quantity <= 0:
            print("product cant be negative or zero here")
        else:
            self.quantity -= new_quantity
    def to_dict(self):
        row = {}
        row["product_id"] = self.product_id
        row["name"] = self.name
        row["price"] = self.price
        row["quantity"] = self.quantity
        return row



class Customer:
    def __init__(self, customer_id, first_name, last_name, email, address):
        self.cart = Cart(customer_id)
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.gmail = email
        self.address = address
        self.orders = {}
        self.next_order_id = 1

    def checkout(self,order_manager):
        # orders = len(self.orders) +1
        #
        # order = Order(orders,self)
        # self.orders[orders] = order
        for key, values in self.cart.products.items():
            if values[1] > values[0].quantity:
                print(f"sorry for some reason our product reduce to{values[0].quantity}please reduce {values[1]-values[0].quantity} amount of products")
                return

        order_id = order_manager.id_giver()
        order = Order(order_id, self)
        self.orders[order_id] = order
        order_manager.add_order(order)
        for key, values in self.cart.products.items():
                 values[0].decrease_stock(values[1])
        self.cart.products ={}

    def show_orders(self):
        for key,values in self.orders.items():
            values.display_order()
    def show_specific_order(self,check_id):
        if check_id in self.orders:
            self.orders[check_id].display_order()
        else:
            print("order not found")
    def to_dict(self):
        row = {}
        row["customer_id"] = self.customer_id
        row["first_name"] = self.first_name
        row["last_name"] = self.last_name
        row["gmail"] = self.gmail
        row["address"] = self.address
        return row





class Cart:
    def __init__(self, cart_id,):
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
    def remove_product(self,product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("removed product successfully")
        else:
            print("product not exist")
    def update_product(self,product_id,new_quantity):
        if product_id in self.products:
            if new_quantity > self.products[product_id][0].quantity:
                print("sorry not enough items")
            elif new_quantity == 0:
                self.remove_product(product_id)
            elif new_quantity <0:
                print("no negative quantity")
            else:
                self.products[product_id][1] = new_quantity
        else:
            print("product not exist")

# class CheckOut(Cart):

class Order:
    def __init__(self,order_id,customer):
        self.order_id = order_id
        self.customer = customer
        self.status = "pending"
        self.order_products = {}
        self.order_stock_products = {}
        for key, values in self.customer.cart.products.items():
            self.order_stock_products.update({key:[values[0],values[1]]})
        for key, values in self.customer.cart.products.items():
            self.order_products.update({key:[values[0].name,values[0].price,values[1]]})
        self.total = 0
        for key, values in self.order_products.items():
            self.total += values[1] * values[2]
    def display_order(self):
        print(self.customer.customer_id)
        print(self.customer.first_name)
        print(self.customer.last_name)
        print(self.customer.gmail)
        print(self.customer.address)
        for key, values in self.order_products.items():
            print(f"product id is {key} \nproduct name is {values[0]} \nproduct price is { values[1]} \nquantity is { values[2]}")
        print("total is", self.total)
    def change_status(self,new_status):
        if self.status == "pending":
            if new_status == "packing":
                self.status = new_status
                return True
            else:
                print("invalid status")
                return False
        elif self.status == "packing":
            if new_status == "shipped":
                self.status = new_status
                return True
            else:

                print("invalid status")
                return False
        elif self.status == "shipped":
            if new_status == "delivered":
                self.status = new_status
                return True
            else:
                print("invalid status")
                return False
        elif self.status == "delivered":
            print("invalid attempt")
            return False
        return False
    def cancel_order(self):
        if self.status == "pending":
            pick = input("are you sure you want to cancel this order?(y/n)").lower()
            if pick == "y":
                self.status = "canceled"
                for key, values in self.order_stock_products.items():
                    values[0].increase_stock(values[1])
                print("you order has been canceled")
            elif pick == "n":
                return
            else:
                print("invalid input")
        elif self.status == "packing":
            pick = input("are you sure you want to cancel this order?(y/n)").lower()
            if pick == "y":
                self.status = "canceled"
                for key, values in self.order_stock_products.items():
                    values[0].increase_stock(values[1])
                print("you order has been canceled")
                print("you have a fine of 1 billion dollars")
            elif pick == "n":
                return
            else:
                print("invalid input")
        elif self.status == "shipped":
            print("you cant cancel this order")
        elif self.status == "delivered":
            print("seriously bruh")
    def to_dict(self):
        row = {}
        row["order_id"] = self.order_id
        row["customer_id"] = self.customer.customer_id
        row["status"] = self.status
        row["order_products"] = self.order_products
        row["total"] = self.total
        return row
class OrderManager:
    def __init__(self,):
        self.orders = {}
        self.count = 1
    def add_order(self,order):
        self.orders[order.order_id] = order
    def change_status(self, order_id,new_status):
        if order_id in self.orders:
            result =self.orders[order_id].change_status(new_status)
            if result:
             print("order status changed")
            else:
                print("order status not changed")
        else:
            print("order id not exist")
    def id_giver(self):
        order_id = self.count
        self.count += 1
        return order_id

class ProductManager:
    def __init__(self,):
        self.products = {}
    def add_product(self,product):
        self.products[product.product_id] = product


class CustomerManager:
    def __init__(self):
        self.customers = {}
    def add_customer(self,customer):
        self.customers[customer.customer_id] = customer








# # product1 = Product("mouse", 1, 100, 5)
# # product2 = Product("keyboard", 2, 300, 5)
# # customer1 = Customer(1, "dani", "pani", "@h", "lahore")
# # customer1.cart.add_product(product1, 1)
# #
# # customer2 = Customer(2, "pani","dani00","@k", "karachi")
# # customer2.cart.add_product(product2, 1)
# #
# # order1 = Order(1, customer1)
# #
# # order1.display_order()
# product1 = Product("mouse",1,100,10)
# product2 = Product("keyboard",2,300,5)
# customer1 = Customer(1,"dani","lani","@","lahore")
# # customer1.cart.add_product(product1,1)
# # customer1.cart.add_product(product2,1)
# # print(product1.quantity)
# # customer1.cart.show_products()
# # customer1.checkout()
# # print(product1.quantity)
# # customer1.cart.show_products()
# # customer1.show_orders()
# customer1.cart.add_product(product1,1)
# customer1.cart.update_product(1,2)
# customer1.cart.show_products()
# customer1.cart.update_product(1,5)
# customer1.cart.update_product(1,0)
# customer1.cart.show_products()
# customer1.show_orders()

product_manager = ProductManager()
order_manager = OrderManager()
customer_manager = CustomerManager()
product1 = Product("Mouse", 1, 100, 10)
product2 = Product("Keyboard", 2, 300, 5)
product_manager.add_product(product1)
product_manager.add_product(product2)
Products = []
for key ,values in product_manager.products.items():
    Products.append(values.to_dict())
data["products"] = Products
with open('data.json','w') as file:
    json.dump(data, file)
with open('data.json','r') as file:
    data = json.load(file)
for row in data['products']:
    product = Product(
        row["name"],
        row["product_id"],
        row["price"],
        row["quantity"])
    product_manager.add_product(product)
product1 = product_manager.products[1]
product2 = product_manager.products[2]


customer1 = Customer(1, "Dani", "Lani", "@", "Lahore")
customer2 = Customer(2, "Ali", "Khan", "@", "Karachi")
customer_manager.add_customer(customer1)
customer_manager.add_customer(customer2)
Customers = []
for keys,values in customer_manager.customers.items():
    Customers.append(values.to_dict())
data["customers"] = Customers
with open('data.json','w') as file:
    json.dump(data, file)
with open('data.json','r') as file:
    data = json.load(file)
for row in data['customers']:
    customer = Customer(
        row["customer_id"],
        row["first_name"],
        row["last_name"],
        row["gmail"],
        row["address"]
    )
    customer_manager.add_customer(customer)
customer1 = customer_manager.customers[1]
customer2 = customer_manager.customers[2]



customer1.cart.add_product(product1, 2)
customer2.cart.add_product(product2, 3)

customer1.checkout(order_manager)
customer2.checkout(order_manager)
order = []
for key,values in order_manager.orders.items():
    order.append(values.to_dict())
data["orders"] = order
with open('data.json','w') as file:
    json.dump(data, file)
with open('data.json','r') as file:
    data = json.load(file)
    for row in data['orders']:
        order = Order(
            row["order_id"],
            customer = customer_manager.customers[row["customer_id"]],
        )
        order.status = row["status"]
        for key, value in row["order_products"].items():
            product_id = int(key)
            product_obj = product_manager.products[product_id]
            order.order_stock_products[product_id] = [product_obj,value[2]]
        order.total = row["total"]
        order_manager.add_order(order)
for key,values in order_manager.orders.items():
    values.display_order()
order1 = order_manager.orders[1]
order1.cancel_order()
print(product_manager.products[1].quantity)
print(product1.quantity)



# print("\n--- CUSTOMER 1 ORDERS ---")
# customer1.show_orders()
#
# print("\n--- CUSTOMER 2 ORDERS ---")
# customer2.show_orders()
#
# print("\n--- ALL MANAGER ORDERS ---")
# for order_id, order in order_manager.orders.items():
#     print("Order ID:", order_id)
#     order.display_order()
#
# print("\n--- REMAINING STOCK ---")
# print("Mouse:", product1.quantity)
# print("Keyboard:", product2.quantity)


