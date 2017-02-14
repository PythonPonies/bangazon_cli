import unittest
import sys
sys.path.append('../')
from app.ordermanager import *
from app.orderfinalizer import *
from app.productonordermanager import *
from app.customer import *
from app.paymentmanager import *
from app.order import *
from app.product import *
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

    def test_check_that_an_order_is_empty(self):
        """
        purpose: test to check if the cart is empty
        author: Ike
        methods: get_ordered_products: returns a list of products
        """
        jfk = Customer("John Kennedy", '1819 Heron Pointe Dr', "Nashville", "TN", 37214, '8889878888')
        manage_status = CustomerStatusManager()
        make_jfk_active_user = manage_status.change_status(jfk, 'bangazon.db')
        start_jfk_order = Order(jfk)
        manage_order = OrderManager()
        jfk_order = manage_order.create_order(start_jfk_order) #an order is created in the database
        manage_products_on_order = ProductOnOrderManager()
        current_order = manage_products_on_order.get_all_products_on_order() #get all products on active user's order
        finalize_order = OrderFinalizer()
        active_order_status = finalize_order.check_cart_contains_items()
        self.assertEqual(active_order_status, [])

    def test_check_that_order_can_be_completed(self):
        """
        purpose: test to check if order can be completed: active user, products on order payment type on order,
        payment complete = 1
        author: Ike
        methods: get_ordered_products: returns a list of products
        """
        with sqlite3.connect('../bangazon.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Products
                WHERE productId = {}
                """.format(4))
            selected_product = cursor.fetchone()
            cursor.close()

        rfk = Customer("Robert Kennedy", '1919 Heron Pointe Dr', "Nashville", "TN", 37214, '8888978880')
        status_manager = CustomerStatusManager()
        status_manager.change_status(rfk, 'bangazon.db')
        start_rfk_order = Order(rfk)
        manage_order = OrderManager()
        rfk_order = manage_order.create_order(start_rfk_order) #an order is created in the database
        manage_products_on_order = ProductOnOrderManager()
        gear = Product(selected_product[1],selected_product[2], selected_product[3], selected_product[4])
        manage_products_on_order.add_product_to_order(gear)
        current_order = manage_products_on_order.get_all_products_on_order() #get all products on active user's order
        finalize_order = OrderFinalizer()
        active_order_status = finalize_order.check_cart_contains_items()
        self.assertNotEqual(active_order_status, [])
        self.assertNotEqual(start_rfk_order.get_order_payment_type(),'None')



if __name__ == "__main__":
    unittest.main()







