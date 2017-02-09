class Product:
    """ The Product class creates a new product with data passed to it.

    Method List   __init__ instansiates the new Product with product_name, price, quantity
    Arguments     The object argument lets the Customer class inherit properites of object
    Author        Zoe LeBlanc, Python Ponies
    """
    def __init__(self, name, price, quantity):
        """
        A new product is created based on the arguments passed in: name, price, quantity. 
        """
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_product_name(self):
        return self.__name

    def get_product_price(self):
        return self.__price

    def get_product_quantity(self):
        return self.__quantity
