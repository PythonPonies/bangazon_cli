from app.customer import *
from app.customerstatusmanager import *

class CLIChooseActiveCustomer():
    ''' Methods: two methods to a) show the list of customers in the database so a user can choose and b) change selected 
        user's status to active
        Arguments: the second method takes an argument of the customer_id of the selected customer, which is passed via the 
        user's input
        Author: L.Sales, Python Ponies
    '''
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