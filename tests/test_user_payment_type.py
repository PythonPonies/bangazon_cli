import unittest

import sys
sys.path.append('../')

from app.paymentmanager import *
from app.customerstatusmanager import *
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


        self.payments = PaymentManager() # PaymentManager class for accessing methods related to payment + payment information.
        self.active_customer = CustomerStatusManager() # CustomerManager class for accessing methods related to active customer

    def test_user_can_add_payment_type(self):
        with sqlite3.connect('../bangazon.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Customers
                WHERE customer_name = '{}'
                """.format("John Doe"))
            selected_customer = cursor.fetchone()
        john = Customer(selected_customer[1], selected_customer[2], selected_customer[3], selected_customer[4], selected_customer[5], selected_customer[6])
        self.active_customer.change_status(john, 'bangazon.db')
        self.payments.add_payment_type('AmEx', 1010101010, '../bangazon.db')


        #------------------------------------------------------------------#
        # this is how PaymentType table data is structured when returned   #
        #                                                                  #
        #   PK        PAYMENT_NAME     ACCOUNT_NUMBER     CUSTOMER         #
        #[( PK,         "Visa",       "1234567890",     customer_object )] #
        #    0             1                2                  3           #
        #------------------------------------------------------------------#


    def test_user_can_get_own_payment_types(self):

        user_payment_types = self.payments.get_payment_types('../bangazon.db')

        self.assertEqual(user_payment_types[1][1], 'AmEx')
        self.assertEqual(user_payment_types[1][2], 1010101010)


if __name__ == "__main__":
    unittest.main()