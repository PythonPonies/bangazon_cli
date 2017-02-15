import sqlite3

class ProductManager():
    """ The Product Manager class manages products with data passed to it.

    Method List   
    - create_product, get_all_products, get_one_product
    Author        Zoe LeBlanc, Python Ponies
    """
    def __init__(self, db_path):
        """
        This method initializes the class with self, and the required argument specifying the database path. 
        """
        self.db_path = db_path

    def create_product(self, product):
        """Method creates a product"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS `Products`
                    (
                        productId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT NOT NULL,
                        price DECIMAL(18,2) NOT NULL,
                        quantity INTEGER NOT NULL
                    )
                """)
            cursor.execute("""
                INSERT INTO Products 
                VALUES (null, '{}', '{}', '{}', {}) 
                """.format(product.get_product_title(), product.get_product_description(), product.get_product_price(), product.get_product_quantity()))
        cursor.close()

    def get_all_products(self):
        """Gets all products in the database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Products
                """)
            selected_product = cursor.fetchall()
        return selected_product

    def get_one_product(self, product):
        """Gets one products in the database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Products
                WHERE title = '{}'
                AND description = '{}'
                AND price = {}
                """.format(product.get_product_title(), product.get_product_description(), product.get_product_price()))
            selected_product = cursor.fetchone()
        return selected_product



