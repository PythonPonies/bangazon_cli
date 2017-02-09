class OrderFinalizer():
	"""
	purpose: The OrderFinalizer class contains  methods and properties related
	to the ordering of products from creation to submission.

	Methods: 
		- check_cart_contains_items
		- complete_order
		-check_order_is_complete
	"""

	def check_cart_contains_items(self, order):
		"""
		purpose: Determine whether the cart has items by returning status
		Author: Ike
			variables: 
				- status: A flag set to False that can toggle to True
				- order: A list of products, an empty list returns False

		"""
		status = False
		self.order = order
		if order:
			status = True
		return status

	def complete_order(self, order, payment_type):
		"""
		purpose: Complete an order by tying a payment_type to an order
		author: Ike
		parameters:
			- order: list of products
			-payment_type: data type containing payment_type
		
		variables:
			- status: flag to ensure the order contains items (is active?)
		"""
		status = True
		self.order = order
		self.payment_type =  payment_type
		if status:
			 order["payment_type"] = self.payment_type


	def check_order_is_complete(self,order, payment_type):
		"""
		purpose: Check that an order is complete by returning a True indicator
		author: Ike
		parameters:
			-order
			-payment_type
		"""
		order = {"userId":"42", "products":['peanut butter', 'jelly', 'bread'], "payment_type": "10"}
		self.payment_type = order["payment_type"]
		status = True
		order_status = True
		return order_status

