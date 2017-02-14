import unittest
import sys
sys.path.append('../')
from app.customer import *
from app.customerregistrar import *
# Registrar and Customer are classes of registercustomer

class TestRegisterCustomer(unittest.TestCase):
    """
    This class tests everything related to registering a user.

    Method List   test_customer_can_register
    Arguments     unittest.TestCase allows the unittest model to know what to test.
    Author        Nate Baker, Python Ponies
    """

    def test_customer_can_register(self):
        """ This method tests if a customer can successfully register. A customer should be able to register by entering the following information:

            - customer name
            - street address
            - city
            - state
            - postal code
            - phone number
        """

        nate = Customer("nate",             # customer name
                        "343 paper street", # street address
                        "nashville",        # city
                        "tn",               # state
                        "12345",            # postal code
                        "1234567")          # phone number

        # Test that nate is an instance of the Customer class
        self.assertIsInstance(nate, Customer)

        # Register the customer nate
        CustomerRegistrar.register(nate)

        # Test that it's true that the customer is registered
        self.assertTrue(CustomerRegistrar.check_if_registered(nate))

    def test_list_of_customers_returned(self):
        """
        This method tests if a list of tuples is returned when asking for a list of customers.
        """
        customers = Customer.get_customer_list('../bangazon.db')
        self.assertIsInstance(customers, list)
        self.assertIsInstance(customers[0], tuple)


if __name__ == "__main__":
    unittest.main()

