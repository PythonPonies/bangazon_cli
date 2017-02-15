import sys
sys.path.append('../')

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

class CLIProductPopularity():
    '''
    The CLIProductPopularity class allows a customer to see all products listed by popularity from the command line interface.

    Methods: add_product

    Author: Zoe LeBlanc, Python Ponies
    '''
    def list_product():
        '''
        The list_product method lists all the products by popularity to a customer command line interface.
        '''
        all_products = ProductOnOrderManager('bangazon.db').get_products_by_order_popularity()
        table_products = bcolors.OKBLUE + "{:18s}{:^11s} {:^11s}{:>15s}\n".format("Products", "Orders", "Customers", "Revenue") + bcolors.ENDC
        table_products += bcolors.HEADER + "*" * 55 + "\n" + bcolors.ENDC
        for product in all_products:
            table_products += "{:18s}{:^11d}{:^11d}{:>15d}\n".format(product[0], int(product[1]), int(product[2]), int(product[3]))
        print(table_products)
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