import sqlite3

class CustomerRegistrar():
    """ CustomerRegistrar handles registering a customer.

    Method List   register, check_if_registered
    Author        Nate Baker, Python Ponies
    """

    def register(customer):
        """ The registrar method takes a customer as an argument and pushed customer data up to the database. The customer arguement is passed so we can if a specific customer has been added to the database.
        """

        # Connect to the database
        with sqlite3.connect('../bangazon.db') as conn:
            c = conn.cursor()

            # If the Customers table doesn't exist, create one
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


            # insert a new customer based on the customer object passed to this method
            c.execute("""
                SELECT * FROM Customers
                WHERE customer_name = '{}'
                AND street_address = '{}'
                AND city = '{}'
                AND state = '{}'
                AND postal_code = '{}' 
                AND phone = '{}'  
            """.format(customer.get_customer_name(), customer.get_street_address(), customer.get_city(), customer.get_state(), customer.get_postal_code(), customer.get_phone_number()))
            selected_customer = c.fetchall()
            if len(selected_customer) == 0:
                c.execute("""
                    INSERT INTO Customers VALUES (null, '{}', '{}', '{}', '{}', '{}', '{}', {})
                    """.format(customer.get_customer_name(), customer.get_street_address(), customer.get_city(), customer.get_state(), customer.get_postal_code(), customer.get_phone_number(), 0))

    def check_if_registered(customer):
        """ This method checks that the customer data we pushed up indeed was added to the database. The customer arguement is passed so we can if a specific customer has been added to the database.
        """

        # Connect to the database
        with sqlite3.connect('../bangazon.db') as conn:
            c = conn.cursor()
            c.execute("""
                SELECT * FROM Customers
                WHERE customer_name='{}'
                AND street_address='{}'
                AND city='{}'
                AND state='{}'
                AND postal_code='{}'
                AND phone='{}'
                """.format(customer.get_customer_name(), customer.get_street_address(), customer.get_city(), customer.get_state(), customer.get_postal_code(), customer.get_phone_number()))

            # db_customer returns the customer tuple that was just added in the following format:
            # (3, 'nate', '343 paper street', 'nashville', 'tn', 12345, '1234567', 0)
            db_customer = c.fetchone()

            # check if what was pushed up matches what's in the database
            if db_customer[1] == customer.get_customer_name() \
            and db_customer[2] == customer.get_street_address() \
            and db_customer[3] == customer.get_city() \
            and db_customer[4] == customer.get_state() \
            and int(db_customer[5]) == int(customer.get_postal_code()) \
            and db_customer[6] == customer.get_phone_number():
                return True # if yes, return true
            else:
                return False # if no, return false
