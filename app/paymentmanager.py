import sqlite3

class PaymentManager():
    """
        The Payments class contains all methods and properties related to a customer's payment information and actions.

        Methods:
                - add_payment_type

                - get_payment_types

        Author: Steven Holmes (Python Ponies [Bangazon, LLC])
    """

    def add_payment_type(self, payment_name, account_number, db_path):
        """
            Adds payment type to active customer accout

            Arguments:
                    payment_name - payment type name (eg. Visa)
                    account_number - account number of payment type
                    db_path - the absolute path to the database file
        """

        with sqlite3.connect(db_path) as bangazon:
            c = bangazon.cursor()

            c.execute("SELECT customerId FROM Customers WHERE active = 1")
            customer = c.fetchall()

            c.execute("""
                CREATE TABLE IF NOT EXISTS `PaymentTypes`
                    (
                        paymentTypeId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        payment_name TEXT NOT NULL,
                        account_number INTEGER NOT NULL,
                        customerId INTEGER NOT NULL
                        -- FOREIGN KEY(`customerId`) REFERENCES `Customers`(`customerId`)
                    )
            """)

            c.execute("""
                        INSERT INTO PaymentTypes VALUES (null, '{}', {}, {})
                        """.format(
                                    payment_name,
                                    account_number,
                                    customer[0][0]))

    def get_payment_types(self, db_path):
        """
            Returns all payment types of active customer

            Arguments:
                    db_path - the absolute path to the database file
        """

        with sqlite3.connect(db_path) as bangazon:
            c = bangazon.cursor()

            c.execute("SELECT customerId FROM Customers WHERE active = 1")
            customer = c.fetchall()

            c.execute("""
                        SELECT *
                        FROM PaymentTypes
                        WHERE customerId = {}
                """.format(
                            customer[0][0]))
            customer_payment_types = c.fetchall()

        return customer_payment_types
