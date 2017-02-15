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
            if submit_response == "Y" or "y" or "yes" or "YES":
                list_of_payment_types = PaymentManager.get_payment_types('bangazon.db')
                for payment_type in list_of_payment_types:
                    print(payment_type[0],payment_type[1])
            
            selected_payment_option = input('Please choose a payment option. or Type "quit" to re-enter')
            print(selected_payment_option, "this is the selected payment_option...")

            signal = True
            if selected_payment_option == "quit" or "Quit" or 'Quit':
                signal == False



            elif submit_response == 'n' or 'N':
                print('Select "y" to complete order')
                signal == False

            else:
                signal == True

            if signal == True:
                selected_payment_option_as_integer = int(selected_payment_option)
                print(selected_payment_option_as_integer, "this is int selected pmt option")
                OrderFinalizer.finalize_order(selected_payment_option_as_integer)


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

