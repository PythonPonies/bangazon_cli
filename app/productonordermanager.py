import sqlite3


class ProductOnOrderManager():
    """ The Order Manager class manages orders and products with data passed to it.

    Method List   create_order, customer_has_active_order, add_product_to_origin, get_products_on_order
    Arguments     The object argument lets the Order Manager class inherit properites of object
    Author        Zoe LeBlanc, Python Ponies
    """
    def __init__(self):
        pass

    def add_product_to_order(self, product):
        """
        Adds a new product to an order. 
        """
        with sqlite3.connect('../bangazon.db') as conn:
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
            decrease_value = selected_product[0][4]-1
            cursor.execute("""
                UPDATE Products
                SET quantity = {}
                WHERE productId = {} 
                """.format(decrease_value, selected_product[0][0]))
        cursor.close()

    def get_all_products_on_order(self):
        """
        Gets all products on order. 
        """
        with sqlite3.connect('../bangazon.db') as conn:
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

    def get_all_products_not_on_order(self):
        """
        Gets all products not on order. 
        """
        with sqlite3.connect('../bangazon.db') as conn:
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
            selected_products_on_order = cursor.fetchall()
            for product in selected_products_on_order:
                cursor.execute("""
                SELECT * FROM Products
                WHERE quantity != {} 
                """.format(0))
            remaining_products = cursor.fetchall()
            return remaining_products
