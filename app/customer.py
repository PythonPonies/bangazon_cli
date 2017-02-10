class Customer(object):
    """ The Customer class creates a new Customer with data passed to it.

    Method List:
        - __init__: instansiates the new Customer with customer_name, city, state, postal_code, and phone_number
        - get_customer_name:
        - get_city:
        - get_state:
        - get_postal_code:
        - get_phone_number

    Arguments     The object argument lets the Customer class inherit properites of object
    Author        Nate Baker, Python Ponies
    """
    def __init__(self, customer_name, street_address, city, state, postal_code, phone_number):
        """
        A new customer is created based on the arguments passed in: customer_name, city, state, postal_code, and phone_number. The active switch is set to false by default and turned on when an active user is selected.
        """
        self.customer_name = customer_name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.phone_number = phone_number
        self.active = 0
        # Active is false by default so it doesn't need to be an argument. SQLite doesn't have a boolean so it takes 0 or 1

    def get_customer_name(self):
        return self.customer_name

    def get_street_address(self):
        return self.street_address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_postal_code(self):
        return self.postal_code

    def get_phone_number(self):
        return self.phone_number

    def get_active(self):
        return self.active