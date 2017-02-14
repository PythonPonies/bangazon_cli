from app.customer import *
from app.customerregistrar import *

class CLICreateCustomer(object):

    def create_customer():

        # collect user inputs
        customer_name  = input(" Enter customer name > ")
        street_address = input("Enter street address > ")
        city           = input("          Enter city > ")
        state          = input("         Enter state > ")
        postal_code    = input("   Enter postal code > ")
        phone_number   = input("  Enter phone number > ")

        new_customer = Customer(
            customer_name,
            street_address,
            city,
            state,
            postal_code,
            phone_number
        )

        CustomerRegistrar.register(new_customer, 'bangazon.db')

        print("The customer " + customer_name + " registered successfully")

        #show correct menu
