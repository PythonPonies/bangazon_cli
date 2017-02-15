# import sys
# sys.path.append('../')
# from bangazon import *
from app.customer import *
from app.customerstatusmanager import *

class CLIChooseActiveCustomer():

    def show_customers_list():
        customers_list = ''
        customers = Customer.get_customer_list('bangazon.db')
        for customer in customers:
            customers_list = "{}:{}".format(customer[0], customer[1])
            print(customers_list)
        active_customer = input("Select a user: ")
        active_customer = int(active_customer)
        CLIChooseActiveCustomer.choose_active_customer(active_customer)

    def choose_active_customer(active_customer):
        new_user = CustomerStatusManager()
        new_user.change_status(active_customer, 'bangazon.db')
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