import sys
sys.path.append('../')
# from bangazon import *
from app.paymentmanager import *
from app.orderfinalizer import *
from app.productonordermanager import *

class CLICompleteOrder():

    def complete_order():
        if OrderFinalizer.check_cart_contains_items():
            checkout_total = OrderFinalizer.order_total()
            print('Your total order is ' + str(checkout_total) +". ")
            submit_response = input('Ready to Purchase? (y/n)')
            if submit_response == 'y' or 'Y':
                # import pdb; pdb.set_trace()  #This will be removed later per Steve
                list_of_payment_types = PaymentManager.get_payment_types('bangazon.db')
                organized_payment_types = []
                for payment_type in list_of_payment_types:
                    print(payment_type[0],payment_type[1])
                # import pdb; pdb.set_trace()
                selected_payment_option = input('Please choose a payment option. or Type "quit" to re-enter')
                if selected_payment_option == "quit" or "Quit" or 'Quit':
                    print('Please select a valid payment option')

                else:
                    OrderFinalizer.complete_order(selected_payment_option)
            elif submit_response == 'n' or 'N':
                print('Select "y" to complete order')


        else:
            print('Please add some products to your order first.  Refer to the main menu')
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




# if __name__ == '__main__':

#     sys.argv[1]
#     cli_complete = CLICompleteOrder()
#     cli_complete.complete_order()

