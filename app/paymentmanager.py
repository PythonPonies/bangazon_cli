class PaymentManager():
    """
        The Payments class contains all methods and properties related to a customer's payment information and actions.

        Methods: 
                - add_payment_type

                - get_payment_types

        Author: Steven Holmes (Python Ponies [Bangazon, LLC])
    """

    def __init__(self):
        self.payment_types = []


    def add_payment_type(self, customer, payment_name, account_number):
        """
            Adds payment type for customer account

            Arguments: 
                    customer - customer identifier to add payment type for
                    payment_name - name of payment type
                    account_number - account number of payment type
        """

        self.payment_types.append( ("pk", payment_name, account_number, customer) )

    def get_payment_types(self, customer):
        """
            Gets payment types of customer

            Arguments:
                    customer - customer to get payment types for
        """

        for payment in self.payment_types:
            if payment[3] == customer:
                return self.payment_types