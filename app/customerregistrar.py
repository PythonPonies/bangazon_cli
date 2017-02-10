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
        connection = sqlite3.connect('../bangazon.db')

        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `Customers` VALUES (null, '{}', '{}', '{}', '{}', '{}', {})".format(customer.customer_name, customer.city, customer.state, customer.postal_code, customer.phone_number, customer.active)
                cursor.execute(sql)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

            # with connection.cursor() as cursor:
            #     # Read a single record
            #     sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            #     cursor.execute(sql, ('webmaster@python.org',))
            #     result = cursor.fetchone()
            #     print(result)
        finally:
            connection.close()

    def check_if_registered(customer):
        return True