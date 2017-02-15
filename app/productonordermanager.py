import sqlite3


class ProductOnOrderManager():
    """ The Product On Order Manager class manages orders and products with data passed to it.

    Method List   
    - create_order, customer_has_active_order, add_product_to_origin, get_products_on_order
    Arguments     
    - The object argument lets the Product On Order Manager class inherit properites of object
    Author        Zoe LeBlanc, Python Ponies
    """
    def __init__(self, db_path):
        """
        This method initializes the class with self, and the required argument specifying the database path. 
        """
        self.db_path = db_path

    def add_product_to_order(self, product):
        """
        This method adds a new product to the active order and checks if the product has quantity remaining. If not in stock, the method returns a message to the user about the product. 
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
            selected_user = cursor.fetchone()
            cursor.execute("""
                SELECT * FROM Orders
                WHERE customerId = {}
                AND payment_complete = {} 
                """.format(selected_user[0], 0))
            selected_order = cursor.fetchone()
            cursor.execute("""
                SELECT * FROM Products
                WHERE title = '{}'
                AND description = '{}'
                AND price = {}
                AND quantity = {} 
                """.format(product.get_product_title(), product.get_product_description(), product.get_product_price(), product.get_product_quantity()))
            selected_product = cursor.fetchone()
            if selected_product[4] > 0:
                cursor.execute("""
                INSERT INTO ProductsOnOrders 
                VALUES (null, {}, {}) """.format(selected_product[0], selected_order[0]))
                decrease_value = selected_product[4]-1
                cursor.execute("""
                    UPDATE Products
                    SET quantity = {}
                    WHERE productId = {} 
                    """.format(decrease_value, selected_product[0]))
            else: 
                print("Product {} is not in stock".format(selected_product[1]))
        cursor.close()

    def get_all_products_on_order(self):
        """
        This method returns all products on the active order. 
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
        cursor.close()

    def get_all_products_not_on_order(self):
        """
        This method returns all products not currently on the active order. 
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
            selected_products_on_order = cursor.fetchall()
            for product in selected_products_on_order:
                cursor.execute("""
                SELECT * FROM Products
                WHERE quantity != {} 
                """.format(0))
            remaining_products = cursor.fetchall()
            return remaining_products
        cursor.close()

    def get_products_by_order_popularity(self):
        """This method returns all products by order popularity and ONLY for completed orders. The result is table returned including product names, number of orders, number of customers who ordered the product, and revenue for each product. The final row is calculates totals for the final three columns. If we want ALL orders, remove the AND o.payment_complete line from both queries"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM (
                SELECT p.title as Name, 
                COUNT(*) as ProductOrders, 
                COUNT(DISTINCT o.customerId) as CustomerOrders,
                SUM(p.price) as Revenue
                FROM ProductsOnOrders po
                INNER JOIN Products p
                ON po.productId = p.productId
                INNER JOIN Orders o
                ON po.orderId = o.orderId
                -- AND o.payment_complete = 1 #Uncomment this line to limit products by complete orders
                GROUP BY po.productId 
                ORDER BY (ProductOrders) DESC
                ) 
                UNION ALL
                SELECT 'Totals' as Name, 
                COUNT(*) as ProductOrders, 
                SUM(DISTINCT o.customerId) as CustomerOrders, 
                SUM(p.price) as Revenue
                FROM ProductsOnOrders po
                INNER JOIN Products p
                ON po.productId = p.productId
                INNER JOIN Orders o
                ON po.orderId = o.orderId
                -- AND o.payment_complete = 1 #Uncomment this line to limit products by complete orders
                """)
            selected_products = cursor.fetchall()
            return selected_products
        cursor.close()
           
    def remove_all_products_from_order(self):
        """This method removes all products from active order"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Customers
                WHERE active = {}
                """.format(1))
            selected_user = cursor.fetchone()
            cursor.execute("""
                SELECT * FROM Orders
                WHERE customerId = '{}'
                AND payment_complete = {} 
                """.format(selected_user[0], 0))
            selected_order = cursor.fetchone()
            cursor.execute("""
                SELECT * FROM ProductsOnOrders
                WHERE orderId = '{}' 
                """.format(selected_order[0]))
            selected_products_on_order = cursor.fetchall()
            for product in selected_products_on_order:
                cursor.execute("""
                DELETE FROM ProductsOnOrders
                WHERE productId = {}
                AND orderId = {} 
                """.format(product[1], selected_order[0]))
            cursor.close()
