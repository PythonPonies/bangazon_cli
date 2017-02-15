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

    def __init__(self, db_path):
        """
        This method initializes the class with self, and the required argument specifying the database path. 
        """
        self.db_path = db_path


    def check_cart_contains_items(self):

        """
        purpose: Determine whether the cart has items by returning status
        Author: Ike
            variables: 
                - status: A flag set to False that can toggle to True
                - order: A list of products, an empty list returns False

        """ 

        with sqlite3.connect(self.db_path) as databae:
            cursor = databae.cursor()
            try:
                cursor.execute('SELECT customerId FROM `Customers` WHERE active = 1'
                )
                cid = cursor.fetchone()
                cursor.execute("""
                    SELECT * FROM Orders
                    WHERE payment_complete = 0
                    AND customerId = '{}'
                    """
                .format(cid[0])
                )
                selected_order = cursor.fetchone()[0] #this is the one order from active user
                cursor.execute("""SELECT productId FROM ProductsOnOrders WHERE orderId = {}""".format(selected_order))
                products_on_selected_order = cursor.fetchall()[0][0]
                if products_on_selected_order:
                    return True
                # return products_on_selected_order

            except sqlite3.OperationalError:
                return False
                # return []


    def finalize_order(self, selected_payment_option_as_integer):
        """
        purpose: Complete an order by tying a payment_type to an order
        author: Ike
        parameters:
            - order: list of products
            -payment_type: data type containing payment_type
        
        variables:
            - status: flag to ensure the order contains items (is active?)
        """

        with sqlite3.connect(self.db_path) as databae:
            cursor = databae.cursor()
            # try:


            cursor.execute('SELECT customerId FROM `Customers` WHERE active = 1'
            )
            cid = cursor.fetchall()[0][0]
            cursor.execute("""
                SELECT * FROM PaymentTypes
                WHERE customerId = '{}'
                """.format(cid)
            )
            selected_payment_type = cursor.fetchall()[0][0]
            # selected_payment_option_as_integer = int(selected_payment_option_as_integer)
            cursor.execute("""
                UPDATE  Orders
                SET payment_complete = 1 
                WHERE payment_complete = 0
                AND customerId = {}
                """.format(cid)
            )
            cursor.execute("""
                UPDATE  Orders
                SET paymentTypeId = {}
                WHERE customerId = {}
                """.format(selected_payment_option_as_integer, cid)
            )
            cursor.execute("""
                SELECT * FROM  Orders
                WHERE payment_complete = 1
                AND customerId = {} 
                """.format(cid)
            )
            payment_status = cursor.fetchall()[0][4]
            # print(payment_status)
            # print('Your order is complete! Press any key to return to main menu')
            # print("""*********************************************************
            #     **  Welcome to Bangazon! Command Line Ordering System  **
            #     *********************************************************
            #     1. Create a customer account
            #     2. Choose active customer
            #     3. Create a payment option
            #     4. Add product to shopping cart
            #     5. Complete an order
            #     7. Leave Bangazon!""")
            # return payment_status
            victory_message = print("Your order is complete! Press any key to return to main menu")
            return victory_message

    def order_total(self):
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

            # cursor.execute("""
            #     SELECT * FROM Orders
            #     WHERE customerId = {}
            #     -- AND payment_complete = 0
            #     """.format(selected_user[0]))
            # selected_order = cursor.fetchone()
            # cursor.execute("""
            #     SELECT productId FROM ProductsOnOrders
            #     WHERE orderId = {}
            #     """.format(selected_order[0]))
            # selected_products = cursor.fetchall()

            # list_of_selected_products = []
            # for item in selected_products:
            #     single_item = list(item)
            #     list_of_selected_products.extend(single_item)

            # print(list_of_selected_products)



            # except:
                # return False

        # status = True
        # self.order = order
        # self.payment_type =  payment_type
        # if status:
        #      order["payment_type"] = self.payment_type

        # return 1


    # def check_order_is_complete(self,order, payment_type):
    #     """
    #     purpose: Check that an order is complete by returning a True indicator
    #     author: Ike
    #     parameters:
    #         -order
    #         -payment_type
    #     """

# if __name__ == '__main__':
#     new_order = OrderFinalizer()
#     # new_order.check_cart_contains_items()
#     # new_order.complete_order()
#     # new_order.order_total()


