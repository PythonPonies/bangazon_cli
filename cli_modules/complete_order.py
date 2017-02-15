import sys
sys.path.append('../')
# from bangazon import *
from app.paymentmanager import *
from app.orderfinalizer import *
from app.productonordermanager import *

class CLICompleteOrder():
    """
        purpose: Display the command line interface and respond to user interaction
        in order to complete an order

        author: Ike, Python Ponies
        methods: 
            - complete_order: 
    """

    def complete_order():
        """
            purpose:  Prints  order total. If user confirms order by user input and
            placing a payment type on the active order, the order is
            completed and order status is returned.
        """

        #instantiate OrderFinalizer class
        final_order = OrderFinalizer('bangazon.db')

        #if items are in the order then display order total cost
        #Takes user input of 'y' to continue order submission process
        if final_order.check_cart_contains_items():
            checkout_total = final_order.order_total()
            print('Your total order is ' + str(checkout_total) +". ")
            submit_response = input('Ready to Purchase? (y/n)')

            #use of flag named signal to trigger complete_order if True;set to False by default
            signal = False

            #if response is 'yes' in a manner that we expect user to behave list payment types
            if signal == False and submit_response == "Y" or submit_response == "y" or submit_response == "yes" or  submit_response == "YES":
                signal = True
                manage_pmt = PaymentManager()
                list_of_payment_types = manage_pmt.get_payment_types('bangazon.db')
                for payment_type in list_of_payment_types:
                    print(payment_type[0],payment_type[1])

            #if the response is 'no' in a manner we expect user to behave display directions
            elif submit_response == 'n' or  submit_response == 'N' or submit_response == 'no' or  submit_response == 'NO':
                signal = False
                message = "select 'y' to complete order...Try again."
                if signal == False:
                    print(message)
                        # signal = False

            # Ask for user to select a payment option or type quit       
            if signal == True:
                selected_payment_option = input('Please choose a payment option. or Type "quit" to re-enter')

            #if user responds quit, stop the order
                if selected_payment_option == "quit" or selected_payment_option == "Quit" or selected_payment_option == 'Quit':
                    signal == False
            else:
                signal == False

            #convert user input to an integer for use in finalize_order function
            #as method argument
            if signal == True:
                selected_payment_option_as_integer = int(selected_payment_option)
                final_order.finalize_order(selected_payment_option_as_integer)

        #if there are no products on an order, print the menu
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

