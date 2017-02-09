import unittest
import sys
sys.path.append('../')
from app.ordermanager import *
from app.productmanager import *
from app.order import *
from app.product import *
from app.customer import *


class TestProductOnOrder(unittest.TestCase):
    """
    This class tests everything related to placing a product on an order.

    Method List   
    test_customer_can_create_an_order
    test_customer_can_add_product_to_an_order
    Arguments unittest.TestCase allows the unittest model to know what to test.
    Author Zoe LeBlanc, Python Ponies
    """

    @classmethod
    def setUpClass(self):
        '''Set up initial instances'''
        self.zoe = Customer('Zoe', 'Nashville', 'TN', '37205', '6158106485')
        self.orderManager = OrderManager()
        self.productManager = ProductManager()

    def test_customer_can_create_an_order(self):
        """ This method tests if a customer can successfully create an order. A customer should be able to create order after passing their name.
        """
        order_1 = Order(self.zoe.customer_name)
        self.assertIsInstance(order_1, Order)
        self.orderManager.create_order(order_1)
        self.assertTrue(self.orderManager.customer_has_active_order(order_1))
       
    def test_customer_can_add_product_to_an_order(self):
        """ This method tests if a customer can successfully add a product to an order. A customer should be able to add a product to an order by passing their name and product.
        """
        product_1 = Product("bike", 100.00, 3)
        print(product_1)
        order_1 = Order(self.zoe.customer_name)
        self.orderManager.add_product_to_order(order_1, product_1)
        self.assertIn((order_1, product_1), self.orderManager.product_on_order)

    # def test_afterCustomerCanSeeAllRemainingProducts(self):
    #     '''Test that customer can see all remaining products'''
    #     self.assertIsNotNone(self.productManager.get_all_available_products(self.zoe))

if __name__ == '__main__':
    unittest.main()