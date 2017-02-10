import unittest

import sys
sys.path.append('../')

from app.paymentmanager import *
from app.customer import *


class TestUserPaymentTypes(unittest.TestCase):
    """
        This class tests aspects of a user's ability to add payment types to their account.

        Methods:
            test_user_can_add_payment_type - Tests that a user will have associated payment type information.
                Arguments: Customer name, payment type, account number

        Author: Steven Holmes
    """

    @classmethod
    def setUpClass(self):
        self.john = Customer("john",             # customer name
                             "343 paper street", #street address
                             "nashville",        # city
                             "tn",               # state
                             "12345",            # postal code
                             "1234567")          # phone number

        self.payments = PaymentManager() # PaymentManager class for accessing methods related to payment + payment information.

    def test_user_can_add_payment_type(self):

        self.payments.add_payment_type(self.john, "Visa", "1234567890") # Using method on Payments class to add a payment type. Takes customer, payment type and account number as arguments.
        self.payments.get_payment_types(self.john) # Using method on Payments class to return payment information for specific customer. Takes customer as argument.

        #-------------------------------------------------------------#
        #   PK  PAYMENT_NAME     ACCOUNT_NUMBER     CUSTOMER          #
        #[( PK,   "Visa",       "1234567890",     customer_object   )]#
        #    0       1                2                  3            #
        #-------------------------------------------------------------#

        for payment in self.payments.payment_types: # Iterate over list of tuples
            self.assertEqual("Visa", payment[1]) # Check first item in tuple
            self.assertEqual("1234567890", payment[2]) # Check second item in tuple


if __name__ == "__main__":
    unittest.main()