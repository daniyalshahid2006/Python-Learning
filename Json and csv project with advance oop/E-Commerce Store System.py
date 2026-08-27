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

    def checkout(self):
        # orders = len(self.orders) +1
        #
        # order = Order(orders,self)
        # self.orders[orders] = order
        for key, values in self.cart.products.items():
            if values[1] > values[0].quantity:
                print(f"sorry for some reason our product reduce to{values[0].quantity}please reduce {values[1]-values[0].quantity} amount of products")
                return

        order_id = self.next_order_id
        order = Order(order_id, self)
        self.orders[order_id] = order
        self.next_order_id += 1
        for key, values in self.cart.products.items():
                 values[0].decrease_stock(values[1])
        self.cart.products ={}

    def show_orders(self):
        for key,values in self.orders.items():
            values.display_order()





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
        self.order_products = {}
        self.status = "pending"
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
    def change_status(self,new_status):
        if self.status == "pending":
            if new_status == "packing":
                self.status = new_status
            else:
                print("invalid status")
        elif self.status == "packing":
            if new_status == "shipped":
                self.status = new_status
            else:
                print("invalid status")
        elif self.status == "shipped":
            if new_status == "delivered":
                self.status = new_status
            else:
                print("invalid status")
        elif self.status == "delivered":
            print("invalid attempt")
    def cancel_order(self):
        if self.status == "pending":
            pick = input("are you sure you want to cancel this order?(y/n)").lower()
            if pick == "y":
                self.status = "canceled"
                for key, values in self.order_products.items():
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
                for key, values in self.order_products.items():
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








# product1 = Product("mouse", 1, 100, 5)
# product2 = Product("keyboard", 2, 300, 5)
# customer1 = Customer(1, "dani", "pani", "@h", "lahore")
# customer1.cart.add_product(product1, 1)
#
# customer2 = Customer(2, "pani","dani00","@k", "karachi")
# customer2.cart.add_product(product2, 1)
#
# order1 = Order(1, customer1)
#
# order1.display_order()
product1 = Product("mouse",1,100,10)
product2 = Product("keyboard",2,300,5)
customer1 = Customer(1,"dani","lani","@","lahore")
# customer1.cart.add_product(product1,1)
# customer1.cart.add_product(product2,1)
# print(product1.quantity)
# customer1.cart.show_products()
# customer1.checkout()
# print(product1.quantity)
# customer1.cart.show_products()
# customer1.show_orders()
customer1.cart.add_product(product1,1)
customer1.cart.update_product(1,2)
customer1.cart.show_products()
customer1.cart.update_product(1,5)
customer1.cart.update_product(1,0)
customer1.cart.show_products()
customer1.show_orders()
