class Order:
    """ The Order class creates a new order with data passed to it.

    Method List   __init__, get_order_date_created, get_order_customer, get_order_payment_type, get_order_status
    Arguments     Requires user object
    Author        Zoe LeBlanc, Python Ponies
    """
    def __init__(self, user):
        
        self.__date_created = "2017-02-08"
        self.__customer = user
        self.payment_type = []
        self.__payment_complete = False
        self.__active = True

    def get_order_date_created(self):
        return self.__date_created

    def get_order_customer(self):
        return self.__customer

    def get_order_payment_type(self):
        return self.payment_type

    def get_order_payment_complete(self):
        return self.__payment_complete

    def get_order_status(self):
        return self.__active

# if __name__ == '__main__':
    
