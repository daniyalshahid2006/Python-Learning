# E-Commerce Store System

A Python-based E-Commerce Store System built using **Object-Oriented Programming (OOP)**. The project manages products, customers, shopping carts, and orders, with **JSON-based data persistence**.

## Features

* Product management
* Customer management
* Shopping cart system
* Add products to cart
* Remove products from cart
* Update product quantities in cart
* Stock management
* Checkout system
* Automatic order creation
* Order status management

  * Pending
  * Packing
  * Shipped
  * Delivered
* Order cancellation
* Automatic stock restoration when an order is cancelled
* Calculate order totals
* Save data to JSON
* Load data from JSON
* Reconstruct Product, Customer, and Order objects from saved JSON data

## OOP Concepts Used

This project demonstrates several Object-Oriented Programming concepts:

* Classes and Objects
* Constructors
* Encapsulation
* Object relationships
* Composition
* Dictionaries containing objects
* Methods
* Object state management
* Serialization and deserialization
* Manager classes for managing collections of objects

## Main Classes

### `Product`

Represents a product in the store.

Handles:

* Product information
* Price
* Stock quantity
* Increasing stock
* Decreasing stock
* Converting product data to a dictionary

### `Customer`

Represents a customer.

Handles:

* Customer information
* Shopping cart
* Checkout
* Customer orders
* Viewing orders

### `Cart`

Represents a customer's shopping cart.

Handles:

* Adding products
* Removing products
* Updating quantities
* Displaying cart contents
* Calculating cart totals

### `Order`

Represents a completed customer order.

Handles:

* Order information
* Ordered products
* Order total
* Order status
* Status changes
* Order cancellation
* Restoring product stock after cancellation

### Manager Classes

The project also uses manager classes to organize objects:

* `ProductManager`
* `CustomerManager`
* `OrderManager`

These classes store and manage their respective objects using dictionaries.

## JSON Persistence

The system uses `data.json` to store:

* Products
* Customers
* Orders

Objects are converted into dictionaries using `to_dict()` before being saved.

When the program loads the JSON file, the dictionaries are converted back into Python objects.

Orders are also reconnected to the appropriate Customer and Product objects after loading.

## Example Workflow

```text
Create Products
      ↓
Create Customers
      ↓
Add Products to Cart
      ↓
Checkout
      ↓
Create Order
      ↓
Decrease Product Stock
      ↓
Save Data to JSON
      ↓
Load Data from JSON
      ↓
Reconstruct Objects
      ↓
Cancel Order
      ↓
Restore Product Stock
```

## Example

A customer can add products to their cart:

```python
customer1.cart.add_product(product1, 2)
```

Then checkout:

```python
customer1.checkout(order_manager)
```

An order can later be cancelled:

```python
order1.cancel_order()
```

When a valid pending or packing order is cancelled, the purchased quantity is returned to the product's stock.

## Technologies

* Python
* Object-Oriented Programming
* JSON
* CSV module imported for future development

## Project Status

**Completed**

This project was created as an OOP practice project focusing on object relationships, managers, JSON serialization/deserialization, and maintaining object references after loading saved data.
