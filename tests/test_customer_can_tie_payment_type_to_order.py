import unittest
import sys
sys.path.append('../')
from app.ordermanager import * 
from app.orderfinalizer import *
from app.customer import *
from app.paymentmanager import *
from app.order import *



class TestCompleteOrder(unittest.TestCase):
	"""
		purpose:
		tests for an finalization of an order
		via tying a payment type to an order
		author: Ike
		methods: test_products_have_been_added
	"""

	@classmethod
	def setUpClass(self):
	    self.bobby = Customer("Bobby Kennedy", "Boston", "MA", "98021", "206-988-8766")
	    self.paymentmanager = PaymentManager()
	    # # self.payments.add_payment_type(self.bobby, "Visa", "1234567890") # Using method on Payments class to add a payment type. Takes customer, payment type and account number as arguments.
	    self.order = Order(self.bobby.customer_name)
	    # self.order.payment_type = self.payments.get_payment_types(self.bobby) # Using method on Payments class to return payment information for specific customer. Takes customer as argument. 
	    self.orderfinalizer = OrderFinalizer()
	    self.ordermanager = OrderManager()

	def test_check_that_an_order_is_empty(self):
		"""
		purpose: test to check if the cart is empty
		author: Ike
		methods: get_ordered_products: returns a list of products
		"""
		product = OrderManager()
		self.assertEqual(product.get_products_on_order(), [])

	def test_check_that_order_can_be_completed(self):
		"""
		purpose: test to check if the cart is empty
		author: Ike
		methods: get_ordered_products: returns a list of products
		"""
		product = OrderManager()
		product.products=['apples', 'oranges', 'ben and jerrys']
		self.order.payment_type.append(self.paymentmanager.add_payment_type(self.bobby, "VISA", "123467"))

		self.assertNotEqual(product.get_products_on_order(), [])

		self.assertIn(self.paymentmanager.add_payment_type(self.bobby, "VISA", "123467"), self.order.payment_type)


if __name__ == "__main__":
    unittest.main()







