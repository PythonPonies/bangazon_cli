import sqlite3

class Customer(object):
    """ The Customer class creates a new Customer with data passed to it.

    Method List:
        - __init__: instansiates the new Customer with customer_name, city, state, postal_code, and phone_number
        - get_customer_name
        - get_street_address
        - get_city
        - get_state
        - get_postal_code
        - get_phone_number
        - get_customer_list

    Arguments     The object argument lets the Customer class inherit properites of object
    Author        Nate Baker, Python Ponies
    """
    def __init__(self, customer_name, street_address, city, state, postal_code, phone_number):
        """
        A new customer is created based on the arguments passed in: customer_name, street_address, city, state, postal_code, and phone_number. The active switch is set to false by default and turned on when an active user is selected.
        """
        self.__street_address = street_address
        self.__customer_name = customer_name
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__postal_code = postal_code
        self.__phone_number = phone_number
        self.__active = 0
        # Active is false by default so it doesn't need to be an argument. SQLite doesn't have a boolean so it takes 0 or 1

    def get_customer_name(self):
        """ get_customer_name returns the name of a customer object. Self is needed as an argument to access the customer object.
        """
        return self.__customer_name

    def get_street_address(self):
        """ get_street_address returns the street address of a customer object. Self is needed as an argument to access the customer object.
        """
        return self.__street_address

    def get_city(self):
        """ get_city returns the city of a customer object. Self is needed as an argument to access the customer object.
        """
        return self.__city

    def get_state(self):
        """ get_state returns the state of a customer object. Self is needed as an argument to access the customer object.
        """
        return self.__state

    def get_postal_code(self):
        """ get_postal_code returns the postal code of a customer object. Self is needed as an argument to access the customer object.
        """
        return self.__postal_code

    def get_phone_number(self):
        """ get_phone_number returns the phone number of a customer object. Self is needed as an argument to access the customer object.
        """
        return self.__phone_number

    def get_active(self):
        """ get_active returns the active value for a customer. This returns true or false based on if the customer is the active customer. Self is needed as an argument to access the customer object.
        """
        return self.__active

    def get_customer_list():
        """ Returns a list of tuples with each tuple being a customer from the database.
        """
        # Connect to the database
        with sqlite3.connect('../bangazon.db') as conn:
            c = conn.cursor()
            # select all customers, but only getch id and name
            c.execute("SELECT customerId, customer_name FROM Customers")
            return c.fetchall() # fetch data