import unittest
import sys
sys.path.append('../')
from app.ordermanager import * 
from app.completeorder import *
from app.customer import *
from app.paymentmanager import *



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
	    self.bobby = Customer("Bobby", "Kennedy", "Boston", "MA", "98021")
	    self.paymentmanager = PaymentManager()
	    self.order = {"userId":"42", "products":['peanut butter', 'jelly', 'bread']}
	    self.payment_type = {"Visa": "12345678"}
	    self.order_empty = []
	    self.orderfinalizer = OrderFinalizer()

	def test_check_that_an_order_is_empty(self):
		"""
		purpose: test to check if the cart is empty
		author: Ike
		methods: get_ordered_products: returns a list of products
		"""
		status = self.orderfinalizer.check_cart_contains_items(self.order_empty)
		#we will set status to False in check_cart_contains_items by default
		self.assertFalse(status)

	def test_valid_order_can_be_completed(self):
		"""
		purpose: test to validate an active order can be completed
		author: Ike
		methods: complete order
		--parameters: 
		"""
		status = self.orderfinalizer.check_cart_contains_items(self.order["products"])
		self.assertTrue(status)
		# if status:
		self.orderfinalizer.complete_order(self.order, self.payment_type)
		order_status = self.orderfinalizer.check_order_is_complete(self.order, self.payment_type)
		self.assertTrue(order_status)


if __name__ == "__main__":
    unittest.main()







