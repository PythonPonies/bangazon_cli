from app.customer import *
from app.customerregistrar import *

class CLICreateCustomer():
    '''
    The CLICreateCustomer class allows a new customer to be made from the command line interface.

    Methods: create_customer

    Author: Nate Baker, Python Ponies
    '''

    def create_customer():
        '''
        The create_customer method creates a new customer from the command line interface. It takes all required inputs and then adds this customer to the database.
        '''

        # collect user inputs
        customer_name  = input("Enter customer name  > ")
        street_address = input("Enter street address > ")
        city           = input("Enter city           > ")
        state          = input("Enter state          > ")
        print                 ("(enter number only)")
        postal_code    = input("Enter postal code    > ")

        # only allow numbers when asking for postal code
        while postal_code.isdigit() == False:
            print              ("")
            print              ("ERROR")
            print              ("(enter number only)")
            postal_code = input("Enter postal code    > ")

        phone_number   = input ("Enter phone number   > ")

        # create new customer based on inputs
        new_customer = Customer(
            customer_name,
            street_address,
            city,
            state,
            postal_code,
            phone_number
        )

        # register news customer
        CustomerRegistrar.register(new_customer, 'bangazon.db')

        # currently, the newly registered customer is NOT set as active customer. This needs to be done manually.

        # provide success message
        print("")
        print("The customer " + customer_name + " registered successfully.")

        #show full menu
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
