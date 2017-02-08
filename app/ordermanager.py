import sqlite3
import sys
sys.path.append('../')
# from app.order import Order
from app.product import Product
class OrderManager():
    def __init__(self):
        self.product_on_order = []

    def create_order(self, order):
        return "{}, {}, {}, {}, {}".format(order.get_order_date_created(), order.get_order_customer(), order.get_order_payment_type(), order.get_order_payment_complete(), order.get_order_status() )

    def customer_has_active_order(self, order):
        return order.get_order_status()

    def add_product_to_order(self, order, product):
        
        self.product_on_order.append((order, product))
        return self.product_on_order

    def get_products_on_order(self, order, product):
        product_on_order = [(product, order)]
        return product_on_order
    

