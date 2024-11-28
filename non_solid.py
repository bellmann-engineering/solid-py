import random

class Product:
    def __init__(self, id, name, price, stock_quantity):
        self.id = id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        self.stock_quantity -= quantity

    def is_available(self, quantity):
        return self.stock_quantity >= quantity


class User:
    def __init__(self, id, name, email, address):
        self.id = id
        self.name = name
        self.email = email
        self.address = address
        self.cart = []

    def add_to_cart(self, product, quantity):
        if product.is_available(quantity):
            self.cart.append((product, quantity))
            print(f"Added {quantity} of {product.name} to the cart.")
        else:
            print(f"Not enough stock for {product.name}.")

    def view_cart(self):
        for item in self.cart:
            product, quantity = item
            print(f"{product.name} - {quantity} units")

    def checkout(self):
        total = 0
        for item in self.cart:
            product, quantity = item
            total += product.price * quantity
        print(f"Total checkout amount: {total}")
        return total

    def clear_cart(self):
        self.cart = []
        print("Cart cleared.")


class PaymentGateway:
    def process_payment(self, amount, user):
        print(f"Processing payment of {amount} for {user.name}.")
        success = random.choice([True, False])
        if success:
            print(f"Payment successful for {user.name}.")
        else:
            print(f"Payment failed for {user.name}.")
        return success


class Order:
    def __init__(self, user, total_amount, payment_status):
        self.id = random.randint(1000, 9999)
        self.user = user
        self.total_amount = total_amount
        self.payment_status = payment_status
        self.status = "Pending"

    def update_status(self, status):
        self.status = status
        print(f"Order {self.id} status updated to {status}.")

class OrderManager:
    def __init__(self):
        self.orders = []

    def create_order(self, user, total_amount, payment_status):
        order = Order(user, total_amount, payment_status)
        self.orders.append(order)
        print(f"Order {order.id} created.")
        return order

    def get_order(self, order_id):
        for order in self.orders:
            if order.id == order_id:
                return order
        return None

    def cancel_order(self, order):
        order.update_status("Cancelled")
        print(f"Order {order.id} cancelled.")


class ShippingService:
    def ship_order(self, order):
        print(f"Shipping order {order.id} for {order.user.name}.")

    def track_shipment(self, order):
        print(f"Tracking shipment for order {order.id}.")


class NotificationService:
    def send_email(self, user, message):
        print(f"Sending email to {user.email}: {message}")

    def send_sms(self, user, message):
        print(f"Sending SMS to {user.name} at {user.address}: {message}")


class Admin:
    def __init__(self):
        self.users = []
        self.products = []
        self.order_manager = OrderManager()
        self.payment_gateway = PaymentGateway()
        self.shipping_service = ShippingService()
        self.notification_service = NotificationService()

    def add_user(self, id, name, email, address):
        user = User(id, name, email, address)
        self.users.append(user)
        print(f"User {name} added.")

    def add_product(self, id, name, price, stock_quantity):
        product = Product(id, name, price, stock_quantity)
        self.products.append(product)
        print(f"Product {name} added.")

    def list_users(self):
        for user in self.users:
            print(f"User: {user.name}, Email: {user.email}, Address: {user.address}")

    def list_products(self):
        for product in self.products:
            print(f"Product: {product.name}, Price: {product.price}, Stock: {product.stock_quantity}")

    def process_checkout(self, user):
        total_amount = user.checkout()
        if total_amount == 0:
            print("No items to checkout.")
            return

        payment_success = self.payment_gateway.process_payment(total_amount, user)
        if payment_success:
            order = self.order_manager.create_order(user, total_amount, "Paid")
            self.notification_service.send_email(user, "Your order has been placed successfully!")
            self.shipping_service.ship_order(order)
            user.clear_cart()
        else:
            print("Payment failed. Order not processed.")


# Example usage

admin = Admin()
admin.add_user(1, "Alice", "alice@example.com", "123 Main St")
admin.add_user(2, "Bob", "bob@example.com", "456 Oak St")

admin.add_product(1, "Laptop", 1000, 10)
admin.add_product(2, "Smartphone", 500, 20)

alice = admin.users[0]
bob = admin.users[1]

laptop = admin.products[0]
phone = admin.products[1]

# Alice adds items to the cart
alice.add_to_cart(laptop, 2)
alice.add_to_cart(phone, 3)

# Alice checks out
admin.process_checkout(alice)

# Bob adds an item to the cart and checks out
bob.add_to_cart(phone, 2)
admin.process_checkout(bob)

# List users and products
admin.list_users()
admin.list_products()
