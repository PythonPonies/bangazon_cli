import sys
sys.path.append('../')
from app.customer import *
from app.order import *
from app.ordermanager import *
from app.product import *
from app.productmanager import *
from app.productonordermanager import *

class bcolors:
    """
        The bcolors class contains variables relevant to adding color to the command line interface.

        Resource: 'http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python'

    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class CLIAddProduct():
    '''
    The CLIAddProduct class allows a customer to add products to order from the command line interface.

    Methods: add_product

    Author: Zoe LeBlanc, Python Ponies
    '''
    def add_product():
        '''
        The add_product method lists all the products available to a customer command line interface. It takes all required inputs and then passes them to input_product.
        '''
        with sqlite3.connect('bangazon.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Customers
                WHERE active = {}
                """.format(1))
            selected_user = cursor.fetchone()
        cursor.close()
        new_order = Order(selected_user)
        new_order_manager = OrderManager('bangazon.db')
        new_order_manager.create_order(new_order)
        list_of_products = ProductOnOrderManager('bangazon.db').get_all_products_not_on_order()
        products_list = "Number. Product Price Quantity \n"
        for product in list_of_products:
            products_list += "{}. {}, {}, {} \n".format(product[0], product[1], product[3], product[4])
        products_list += "Type 'done' to finish adding products"
        print(products_list)
        active_product = input("Select a product to add to order:")
        if active_product == 'done':
            print("""
            *********************************************************
            **  Welcome to Bangazon! Command Line Ordering System  **
            *********************************************************
            1. Create a customer account
            2. Choose active customer
            3. Create a payment option
            4. Add product to shopping cart
            5. Complete an order
            6. List products by popularity
            7. Leave Bangazon!
        """
        )
        else:
            active_product = int(active_product)
            CLIAddProduct.input_product(active_product)

    def input_product(active_product):
        '''
        The input_product method connects to the database and adds the product to and order. It then calls add_product again.
        '''
        with sqlite3.connect('bangazon.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Products
                WHERE productId = {}
                """.format(active_product))
            selected_product = cursor.fetchone()
        new_product = Product(selected_product[1], selected_product[2], selected_product[3], selected_product[4])
        input_product = ProductOnOrderManager('bangazon.db')  
        input_product.add_product_to_order(new_product)
        CLIAddProduct.add_product()  

