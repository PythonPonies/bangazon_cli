import unittest
import sys
sys.path.append('../')
from app.ordermanager import *
from app.orderfinalizer import *
from app.productonordermanager import *
from app.customer import *
from app.paymentmanager import *
from app.order import *
from app.customerregistrar import *
from app.customerstatusmanager import *



class TestCompleteOrder(unittest.TestCase):
	"""
		purpose:
		tests for an finalization of an order
		via tying a payment type to an order
		author: Ike
		methods: test_products_have_been_added
	"""

	# @classmethod
	# def setUpClass(self):
	#     self.bobby = Customer("Bobby Kennedy", '343 paper street', "Boston", "MA", 98021, '2069888766')
	#     self.paymentmanager = PaymentManager()
	#     self.order = Order(self.bobby)
	#     self.orderfinalizer = OrderFinalizer()
	#     self.ordermanager = OrderManager()
	#     self.productonordermanager = ProductOnOrderManager()
	#     self.customerregistrar = CustomerRegistrar()


	def test_check_that_an_order_is_empty(self):
		"""
		purpose: test to check if the cart is empty
		author: Ike
		methods: get_ordered_products: returns a list of products
		"""
		jfk = Customer("John Kennedy", '1819 Heron Pointe Dr', "Nashville", "TN", 37214, '8889878888')
		# registration = CustomerRegistrar()
		# registration.register(jfk)
		# # self.customerregistrar.register(robert)
		# manage_status = CustomerStatusManager()
		# make_jfk_active_user = manage_status.change_status(jfk.customer_name)

		start_jfk_order = Order(jfk)
		manage_order = OrderManager()
		jfk_order = manage_order.create_order(start_jfk_order) #an order is created in the database
		manage_products_on_order = ProductOnOrderManager()
		current_order = manage_products_on_order.get_all_products_on_order() #get all products on active user's order
		print(current_order, "this is current order")
		finalize_order = OrderFinalizer()
		active_order = finalize_order.check_cart_contains_items()
		print(active_order, "this is active order")
		self.assertEqual(current_order, [])
		self.assertEqual(active_order, [])


		
		# self.customerstatusmanager.change_status(self.bobby.get_customer_name())
		# create_order = self.ordermanager.create_order(self.order)
		# order = self.productonordermanager.get_all_products_on_order()
		# product = OrderManager()
		# print(order)
		# self.assertIsNone(order)

	# def test_check_that_order_can_be_completed(self):
	# 	"""
	# 	purpose: test to check if the cart is empty
	# 	author: Ike
	# 	methods: get_ordered_products: returns a list of products
	# 	"""
	# 	product = OrderManager()
	# 	product.products = ['apples', 'oranges', 'ben and jerrys']
	# 	self.order.payment_type.append(self.paymentmanager.add_payment_type(self.bobby, "VISA", "123467"))
	# 	self.assertIsNotNone(order)
	# 	#asserting a payment type is the value for an order.
	# 	self.assertIn(self.paymentmanager.add_payment_type(self.bobby, "VISA", "123467"), self.order.payment_type)
	# 	self.assertEquals(status, 1)

	# 	order_status = ""
	# 	status = CustomerStatusManager.change_status(self, Customer1.customer_name)
	# 	self.assertEqual(order_status, 1)

if __name__ == "__main__":
    unittest.main()







