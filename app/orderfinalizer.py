import sqlite3



class OrderFinalizer():

    """
    purpose: The OrderFinalizer class contains  methods and properties related
    to the submission of an order.

    Methods: 
        - check_cart_contains_items
        - complete_order
        -check_order_is_complete
    """

    def __init__(self, db_path):
        """
        This method initializes the class with self, and the required argument specifying the database path. 
        """
        self.db_path = db_path


    def check_cart_contains_items(self):

        """
        purpose: Determine whether the cart has items by returning status of True
        if the order has products or False if not

        Author: Ike, Python Ponies
            variables: 
                - status: A flag set to False that can toggle to True
                - order: A list of products, an empty list returns False
        """ 

        # connect to database query for active user
        with sqlite3.connect(self.db_path) as databae:
            cursor = databae.cursor()
            try:
                cursor.execute('SELECT customerId FROM `Customers` WHERE active = 1'
                )

                cid = cursor.fetchone() #cid is the customerId for the active user
                cursor.execute("""
                    SELECT * FROM Orders
                    WHERE payment_complete = 0
                    AND customerId = '{}'
                    """
                .format(cid[0])
                )
                selected_order = cursor.fetchone()[0] #this is the one order from active user

                # return products_on_selected_order
                cursor.execute("""SELECT productId FROM ProductsOnOrders WHERE orderId = {}""".format(selected_order))
                products_on_selected_order = cursor.fetchall()[0][0]

                #if products are on a selected order return True
                if products_on_selected_order:
                    return True
          

            except sqlite3.OperationalError:
                return False


    def finalize_order(self, selected_payment_option_as_integer):
        """
        purpose: Complete an order by tying a payment_type to an order
        and setting payment_complete to 1 (from 0 by default)
        author: Ike, Python Ponies
        parameters:
            - order: list of products
            -payment_type: data type containing payment_type
        
        """

        # query to determine the active user
        with sqlite3.connect(self.db_path) as databae:
            cursor = databae.cursor()
            cursor.execute('SELECT customerId FROM `Customers` WHERE active = 1'
            )
            cid = cursor.fetchall()[0][0] #cid is the active user's customerId

            #query to get the payment types for the active user
            cursor.execute("""
                SELECT * FROM PaymentTypes
                WHERE customerId = '{}'
                """.format(cid)
            )
            selected_payment_type = cursor.fetchall()[0][0] 

            #query to update orders of active user to payment_complete = 1
            cursor.execute("""
                UPDATE  Orders
                SET payment_complete = 1 
                WHERE payment_complete = 0
                AND customerId = {}
                """.format(cid)
            )

            #query to set payment type on active order to selected payment type of active user
            cursor.execute("""
                UPDATE  Orders
                SET paymentTypeId = {}
                WHERE customerId = {}
                """.format(selected_payment_option_as_integer, cid)
            )

            #query to set payment complete status to 1 (paid)
            cursor.execute("""
                SELECT * FROM  Orders
                WHERE payment_complete = 1
                AND customerId = {} 
                """.format(cid)
            )

            payment_status = cursor.fetchall()[0][4] #this is the payment status (1)
            victory_message = print("""Your order is complete! Press any key to return to main menu

                *********************************************************
                **  Welcome to Bangazon! Command Line Ordering System  **
                *********************************************************
                1. Create a customer account
                2. Choose active customer
                3. Create a payment option
                4. Add product to shopping cart
                5. Complete an order
                6. List products by popularity
                7. Leave Bangazon


                """)
            return victory_message

    def order_total(self):
        """
        purpose: Total an order by adding sum of products on an order
        author: Ike, Python Ponies
        """
        #query to get sum of order
        with sqlite3.connect(self.db_path) as databae:
            cursor = databae.cursor()
            cursor.execute("""
                SELECT * FROM Customers
                WHERE active = {}
                """.format(1))
            selected_user = cursor.fetchone()
            cursor.execute("""
                SELECT * FROM Orders
                WHERE customerId = {}
                -- AND payment_complete = 0
                """.format(selected_user[0]))
            selected_order = cursor.fetchone()[0]
            cursor.execute("""
                SELECT SUM(Products.price) as revenue, Products.productId, ProductsOnOrders.orderId
                FROM ProductsOnOrders
                JOIN Products
                ON Products.productId = ProductsOnOrders.productId
                JOIN Orders
                On ProductsOnOrders.orderId = Orders.orderId
                JOIN Customers
                ON Orders.customerId = Customers.customerId
                AND Customers.active = {}
                AND Orders.payment_complete = 0
                GROUP BY ProductsOnOrders.orderId;
                """.format(selected_user[7]))
            total = cursor.fetchone()[0]
            return total



# if __name__ == '__main__':
#     new_order = OrderFinalizer()
#     # new_order.check_cart_contains_items()
#     # new_order.complete_order()
#     # new_order.order_total()


