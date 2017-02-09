class Customer(object):
    """ The Customer class creates a new Customer with data passed to it.

    Method List   __init__ instansiates the new Customer with customer_name,
                  city, state, postal_code, and phone_number
    Arguments     The object argument lets the Customer class inherit properites of object
    Author        Nate Baker, Python Ponies
    """
    def __init__(self, customer_name, city, state, postal_code, phone_number):
        """
        A new customer is created based on the arguments passed in: customer_name, city, state, postal_code, and phone_number. The active switch is set to false by default and turned on when an active user is selected.
        """
        self.customer_name = customer_name
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.phone_number = phone_number
        self.active = False
