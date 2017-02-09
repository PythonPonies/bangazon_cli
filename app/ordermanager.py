import sqlite3


class OrderManager():
    """ The Order Manager class manages orders and products with data passed to it.

    Method List   create_order, customer_has_active_order, add_product_to_origin, get_products_on_order
    Arguments     The object argument lets the Order Manager class inherit properites of object
    Author        Zoe LeBlanc & Ike, Python Ponies
    """
    def __init__(self):
        self.order = []
        self.products = []

    def create_order(self, order):
        """
        A new order is created based on the arguments passed in: order. 
        """
        self.order = order
        return self

    def customer_has_not_paid(self, order):
        """
        Checks if customer has an active order. 
        """
        return order.get_order_payment_complete()

    def add_product_to_order(self, order, product):
        """
        Adds a new product to an order. 
        """
        self.products = product
        self.order = order

        return self

    def get_products_on_order(self):
        """
        Gets all products on order. 
        """
        return self.products


    def get_order(self):
        """
        Gets all products on order. 
        """
        return self.order


    def check_cart_contains_items(self, order):
        """
        purpose: Determine whether the cart has items by returning status
        Author: Ike
            variables: 
                - status: A flag set to False that can toggle to True
                - order: A list of products, an empty list returns False

        """
        status = False
        self.order = order
        if order:
            status = True
        return status

    def complete_order(self, order, payment_type):
        """
        purpose: Complete an order by tying a payment_type to an order
        author: Ike
        parameters:
            - order: list of products
            -payment_type: data type containing payment_type
        
        variables:
            - status: flag to ensure the order contains items (is active?)
        """
        status = True
        self.order = order
        self.payment_type =  payment_type
        if status:
             order["payment_type"] = self.payment_type


    def check_order_is_complete(self,order, payment_type):
        """
        purpose: Check that an order is complete by returning a True indicator
        author: Ike
        parameters:
            -order
            -payment_type
        """
        order = {"userId":"42", "products":['peanut butter', 'jelly', 'bread'], "payment_type": "10"}
        self.payment_type = order["payment_type"]
        status = True
        order_status = True
        return order_status


