import sys
sys.path.append('../')
# from bangazon import *
from app.paymentmanager import *
from app.orderfinalizer import *
from app.productonordermanager import *

class CLICompleteOrder():
    def complete_order():
        final_order = OrderFinalizer('bangazon.db')
        if final_order.check_cart_contains_items():
            checkout_total = final_order.order_total()
            print('Your total order is ' + str(checkout_total) +". ")
            submit_response = input('Ready to Purchase? (y/n)')

            # import pdb; pdb.set_trace()
            signal = False

            if signal == False and submit_response == "Y" or submit_response == "y" or submit_response == "yes" or  submit_response == "YES":
                signal = True
                print(signal, "what's signal?")
                manage_pmt = PaymentManager()
                list_of_payment_types = manage_pmt.get_payment_types('bangazon.db')
                for payment_type in list_of_payment_types:
                    print(payment_type[0],payment_type[1])

            elif submit_response == 'n' or 'N' or 'no' or 'NO':
                print(signal, "sig wthin response of no")
                signal = False
                message = "select 'y' to complete order...Try again."
                print(signal, "what's signal within submit no here...")
                if signal == False:
                    print(message)
                        # signal = False

            print(signal, "before slected payment_option choose pmt optoin or quit")
            if signal == True:
                selected_payment_option = input('Please choose a payment option. or Type "quit" to re-enter')

                if selected_payment_option == "quit" or "Quit" or 'Quit':
                    signal == False
            else:
                signal == False

            if signal == True:
                selected_payment_option_as_integer = int(selected_payment_option)
                print(selected_payment_option_as_integer, "this is int selected pmt option")
                final_order.finalize_order(selected_payment_option_as_integer)


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

