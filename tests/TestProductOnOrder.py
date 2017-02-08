import unittest
import sys
sys.path.append('../')
from app.ordermanager import *
from app.productmanager import *
from app.order import *
from app.product import *


class TestProductOnOrder(unittest.TestCase):
    '''Test to validate products and orders are joined'''

    @classmethod
    def setUpClass(self):
        '''Set up initial instances'''
        self.zoe = 'Zoe'
        self.orderManager = OrderManager()
        self.productManager = ProductManager()

    def test_customerCanCreateAnOrder(self):
        '''Test that customer can create an initial order'''
        order_1 = Order(self.zoe)
        self.assertIsInstance(order_1, Order)
        self.orderManager.create_order(order_1)
        self.assertTrue(self.orderManager.customer_has_active_order(order_1))
       
    def test_customerCanAddProductToAnOrder(self):
        '''Test that customer can add a product to an order'''
        product_1 = Product("bike", 100.00, 3)
        print(product_1)
        order_1 = Order(self.zoe)
        self.orderManager.add_product_to_order(order_1, product_1)
        self.assertIn((order_1, product_1), self.orderManager.product_on_order)

    # def test_afterCustomerCanSeeAllRemainingProducts(self):
    #     '''Test that customer can see all remaining products'''
    #     self.assertIsNotNone(self.productManager.get_all_available_products(self.zoe))

if __name__ == '__main__':
    unittest.main()