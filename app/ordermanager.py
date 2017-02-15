import sqlite3


class OrderManager():
    """ The Order Manager class manages orders and products with data passed to it.

    Method List   
     - create_order, customer_has_active_order, add_product_to_origin, get_products_on_order
    Arguments     
    - The object argument lets the Order Manager class inherit properites of object
    Author        Zoe LeBlanc & Ike, Python Ponies
    """
    def __init__(self, db_path):
        """
        This method initializes the class with self, and the required argument specifying the database path. 
        """
        self.db_path = db_path

    def create_order(self, order):
        """
        A new order is created based on the arguments passed in: order. 
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS `Orders`
                (
                    orderId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    date_created TEXT NOT NULL,
                    payment_complete INTEGER NOT NULL,
                    customerId INTEGER NOT NULL,
                    paymentTypeId INTEGER NOT NULL,
                    FOREIGN KEY(customerId) REFERENCES Customers (customerId),
                    FOREIGN KEY(paymentTypeId) REFERENCES PaymentTypes (paymentTypeId)
                )
            """)
            cursor.execute("""
                SELECT * FROM Customers
                WHERE active = {}
                """.format(1))
            selected_user = cursor.fetchall()
            cursor.execute(""" 
                SELECT * FROM Orders
                WHERE customerId = {}
                AND payment_complete = {}
                """.format(selected_user[0][0], 0))
            selected_order = cursor.fetchall()
            if len(selected_order) == 0: 
                cursor.execute("""
                    INSERT INTO Orders VALUES 
                    (null, '{}', '{}', '{}', {}) 
                    """.format(order.get_order_date_created(), selected_user[0][0], None, order.get_order_payment_complete(), 0))
                selected_order = cursor.fetchall()
        cursor.close()

    def customer_has_active_order(self):
        """
        Checks if customer has an active order. 
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Customers
                WHERE active = {}
                """.format(1))
            selected_user = cursor.fetchall()
            cursor.execute("""
                SELECT * FROM Orders 
                WHERE CustomerId = '{}'
                AND payment_complete = {} 
                """.format(selected_user[0][0], 0))
            selected_order = cursor.fetchall() 
            return selected_order
        cursor.close()

    def add_product_to_order(self, product):
        """
        Adds a new product to an order. 
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS `ProductsOnOrders`
                (
                    productsOnOrderId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    productId INTEGER NOT NULL,
                    orderId INTEGER NOT NULL,
                    FOREIGN KEY(productId) REFERENCES Products (productId),
                    FOREIGN KEY(orderId) REFERENCES Orders (orderId)
                )
            """)
            cursor.execute("""
                SELECT * FROM Customers
                WHERE active = {}
                """.format(1))
            selected_user = cursor.fetchall()
            cursor.execute("""
                SELECT * FROM Orders
                WHERE customerId = '{}'
                AND payment_complete = {} 
                """.format(selected_user[0][0], 0))
            selected_order = cursor.fetchall()
            cursor.execute("""
                SELECT * FROM Products
                WHERE title = '{}'
                AND description = '{}'
                AND price = {}
                AND quantity = {} 
                """.format(product.get_product_title(), product.get_product_description(), product.get_product_price(), product.get_product_quantity()))
            selected_product = cursor.fetchall()
            cursor.execute("""
                INSERT INTO ProductsOnOrders 
                VALUES (null, {}, {}) """.format(selected_product[0][0], selected_order[0][0]))
        cursor.close()

    def get_all_products_on_order(self):
        """
        Gets all products on order. 
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Customers
                WHERE active = {}
                """.format(1))
            selected_user = cursor.fetchall()
            cursor.execute("""
                SELECT * FROM Orders
                WHERE customerId = '{}'
                AND payment_complete = {} 
                """.format(selected_user[0][0], 0))
            selected_order = cursor.fetchall()
            cursor.execute("""
                SELECT * FROM ProductsOnOrders
                WHERE orderId = '{}' 
                """.format(selected_order[0][0]))
            selected_product = cursor.fetchall()
        return selected_product


    def get_all_orders_by_customer(self):
        """
        Gets all products on order. 
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Customers
                WHERE active = {}
                """.format(1))
            selected_user = cursor.fetchall()
            cursor.execute("""
                SELECT * FROM Orders
                WHERE customerId = '{}' 
                """.format(selected_user[0][0]))
            selected_order = cursor.fetchall()
        return selected_order


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


