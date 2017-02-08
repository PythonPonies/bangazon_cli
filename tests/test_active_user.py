import unittest
import sys 
sys.path.append('../')
from app.customer import *
from app.customerstatusmanager import *

class TestUserIsActive(unittest.TestCase):
	'''	Methods: test_customer_is_active: method will test if active status returns true, which indicates user is current user.
		Arguments: Customer and CustomerStatusManager
		Author: L.Sales, Python Ponies
	'''
	#Test to determine if user is active
	def test_customer_is_active(self):
		#establish an instance of a user
		Customer1 = Customer('Paul Breckenridge', 'Somerville', 'MA', "23567", '265-345-9867')
		#assert that the property of 'active' on user is true
		CustomerStatusManager.change_status(Customer1)
		self.assertTrue(Customer1.active)

if __name__ == '__main__':
    unittest.main()  