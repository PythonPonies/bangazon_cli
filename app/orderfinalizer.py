import sqlite3



class OrderFinalizer():

    """
    purpose: The OrderFinalizer class contains  methods and properties related
    to the ordering of products from creation to submission.

    Methods: 
        - check_cart_contains_items
        - complete_order
        -check_order_is_complete
    """

    def check_cart_contains_items(self):

        """
        purpose: Determine whether the cart has items by returning status
        Author: Ike
            variables: 
                - status: A flag set to False that can toggle to True
                - order: A list of products, an empty list returns False

        """ 
        with sqlite3.connect("../bangazon.db") as databae:
            cursor = databae.cursor()
            try:
                cursor.execute('SELECT customerId FROM `Customers` WHERE active = 1'
                )
                cid = cursor.fetchone()
                print(cid, "this is currentid")
                cursor.execute("""
                    SELECT * FROM Orders
                    WHERE payment_complete = 0
                    AND customerId = '{}'
                    """
                .format(cid))
                selected_order = cursor.fetchall() #this is the one order from active user
                cursor.execute("SELECT productId FROM ProductsOnOrders WHERE orderId = '{}'")#.format(selected_order[0])
                products_on_selected_order = cursor.fetchall()
                print(products_on_selected_order, "products on selected order")
                return products_on_selected_order

            except sqlite3.OperationalError:
                return False


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

        with sqlite3.connect("../bangazon.db") as databae:
            cursor = databae.cursor()
            cursor.execute('SELECT customerId FROM `Customers` WHERE active = 1')
            cid = cursor.fetchall()
            print(cid)
