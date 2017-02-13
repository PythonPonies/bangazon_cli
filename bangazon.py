import sys
from cli_modules import *

class CommandLineInterface():
    """ CommandLineInterface handles command line arguments to access functionality from the Bangazon app.

    Method List   PrintFullMenu, PrintStartMenu
    Author        Nate Baker and Steven Holmes, Python Ponies
    """

    def PrintFullMenu():
        """ The PrintFullMenu method prints all menu options available to the customer.
        """
        print("""
            *********************************************************
            **  Welcome to Bangazon! Command Line Ordering System  **
            *********************************************************
            1. Create a customer account
            2. Choose active customer
            3. Create a payment option
            4. Add product to shopping cart
            5. Complete an order
            7. Leave Bangazon!
        """
        )

    def PrintStartMenu():
        """ The PrintStartMenu method prints only options to a customer assuming they are just entering the interface and we want them to log in, register, or get out.
        """
        print("""
            *********************************************************
            **  Welcome to Bangazon! Command Line Ordering System  **
            *********************************************************
            1. Create a customer account
            2. Choose active customer
            7. Leave Bangazon!
        """
        )

# If the customer accesses this file via the command line...
if __name__ == "__main__":
    # and types the following commands, do the following...
    if sys.argv[1] == "menu":
        CommandLineInterface.PrintStartMenu()
    elif sys.argv[1] == "1":
        # 1. Create a customer account
        create_customer.CLICreateCustomer.create_customer()
        # file in cli_modules > class > method
    elif sys.argv[1] == "2":
        # 2. Choose active customer
        choose_active_customer.CLIChooseActiveCustomer.choose_active_customer()
    elif sys.argv[1] == "3":
        # 3. Create a payment option
        create_payment.CLICreatePayment.create_payment()
    elif sys.argv[1] == "4":
        # 4. Add product to shopping cart
        add_product.CLIAddProduct.add_product()
    elif sys.argv[1] == "5":
        # 5. Complete an order
        complete_order.CLICompleteOrder.complete_order()
    # elif sys.argv[1] == "6":
    # placeholder for printing all products
    elif sys.argv[1] == "7":
        # 7. Leave Bangazon!
        leave_bangazon.CLILeaveBangazon.leave_bangazon()
    # and if not, handle the default action
    else:
        print("you typed something else")
