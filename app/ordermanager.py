import sqlite3
import sys
sys.path.append('../')
from app.product import Product


class OrderManager():
    """ The Order Manager class manages orders and products with data passed to it.

    Method List   create_order, customer_has_active_order, add_product_to_origin, get_products_on_order
    Arguments     The object argument lets the Order Manager class inherit properites of object
    Author        Zoe LeBlanc, Python Ponies
    """
    def __init__(self):
        self.product_on_order = []

    def create_order(self, order):
        """
        A new order is created based on the arguments passed in: order. 
        """
        return "{}, {}, {}, {}, {}".format(order.get_order_date_created(), order.get_order_customer(), order.get_order_payment_type(), order.get_order_payment_complete(), order.get_order_status() )

    def customer_has_active_order(self, order):
        """
        Checks if customer has an active order. 
        """
        return order.get_order_status()

    def add_product_to_order(self, order, product):
        """
        Adds a new product to an order. 
        """
        self.product_on_order.append((order, product))
        return self.product_on_order

    def get_products_on_order(self, order):
        """
        Gets all products on order. 
        """
        product_1 = Product("bike", 100.00, 3)
        product_2 = Product("bike", 100.00, 3)
        self.product_on_order.append((order, product_1, product_2))
        return self.product_on_order
    

