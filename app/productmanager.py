import sqlite3

class ProductManager():
    
    def create_product(self, product):
        """Method creates a product"""
        with sqlite3.connect('../bangazon.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS `Products`
                    (
                        productId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT NOT NULL,
                        price INTEGER NOT NULL,
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
        with sqlite3.connect('../bangazon.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Products
                """)
            selected_product = cursor.fetchall()
        return selected_product

    def get_one_product(self, product):
        """Gets one products in the database"""
        with sqlite3.connect('../bangazon.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Products
                WHERE title = '{}'
                AND description = '{}'
                AND price = {}
                """.format(product.get_product_title(), product.get_product_description(), product.get_product_price()))
            selected_product = cursor.fetchone()
        return selected_product



