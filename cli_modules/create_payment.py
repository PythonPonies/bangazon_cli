import sys
sys.path.append('../')

from app.paymentmanager import *
from app.customerstatusmanager import *
from app.customer import *

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

class CLICreatePayment():
    """
        The CLICreatePayment class contains all methods and properties related to the command line interface actions of adding payment methods to a customer's account.

        Methods:
                - create_payment

        Author: Steven Holmes (Python Ponies [Bangazon, LLC])
    """

    def create_payment():
        """
            Creates a payment for the user via command line interface and adds it to the Bangazon database.

        """

        payment = PaymentManager()

        print("""
            *****************************************
            *      CREATE NEW PAYMENT TYPE          *
            *****************************************
            """)
        payment_name = input(bcolors.OKBLUE + """

Enter payment type (e.g. AmEx, Visa, Checking)

> """ + bcolors.ENDC)

        account_number = input(bcolors.OKBLUE + """

Enter account number

> """ + bcolors.ENDC)

        payment.add_payment_type(payment_name, account_number, 'bangazon.db')

        print(bcolors.OKBLUE + 'Successfully added ' + payment_name + ' (#' + account_number + ') payment method to your account.' + bcolors.ENDC)

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

