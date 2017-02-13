import datetime
class Order:
    """ The Order class creates a new order with data passed to it.

    Method List   __init__, get_order_date_created, get_order_customer, get_order_payment_type, get_order_status
    Arguments     Requires user object
    Author        Zoe LeBlanc, Python Ponies
    """
    def __init__(self, user):
        """
        A new order is created based on the arguments passed in: user. 
        """
        self.__date_created = datetime.datetime.now()
        self.__customer = user
        self.payment_type = []
        self.__payment_complete = 0

    def get_order_date_created(self):
        """ get_order_date_created returns the date created of an order object. Self is needed as an argument to access the order object.
        """
        return self.__date_created

    def get_order_customer(self):
        """ get_order_customer returns the customer of an order object. Self is needed as an argument to access the order object.
        """
        return self.__customer

    def get_order_payment_type(self):
        """ get_order_payment_type returns the payment type of an order object. Self is needed as an argument to access the order object.
        """
        return self.payment_type

    def get_order_payment_complete(self):
        """ get_order_payment_complete returns the payment_complete of an order object. Self is needed as an argument to access the order object.
        """
        return self.__payment_complete


    
