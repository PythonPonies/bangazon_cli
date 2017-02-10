import sqlite3

class CustomerRegistrar():
    """ CustomerRegistrar handles registering a customer.

    Method List   register, check_if_registered
    Author        Nate Baker, Python Ponies
    """

    def register(customer):
        print("customer method runs")
        """ The registrar method takes a customer as an argument and pushed customer data up to the database.
        """

        # Connect to the database
        with sqlite3.connect('../bangazon.db') as conn:
            c = conn.cursor()

            # If the Customers table doesn't exist, create
            c.execute("""
                CREATE TABLE IF NOT EXISTS Customers (
                `customerId` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                `customer_name` TEXT NOT NULL,
                `street_address` TEXT NOT NULL,
                `city` TEXT NOT NULL,
                `state` TEXT NOT NULL,
                `postal_code` INTEGER NOT NULL,
                `phone` TEXT NOT NULL,
                `active` INTEGER NOT NULL)
                """
            );

            try:
                c.execute("""
                    INSERT INTO `Customers` VALUES (null, '{}', '{}', '{}', '{}', '{}', '{}', {})
                    """.format(customer.customer_name, customer.street_address, customer.city, customer.state, customer.postal_code, customer.phone_number, 0))
            except sqlite3.OperationalError:
                return "There was an error. Please try again."

    def check_if_registered(customer):
        return True