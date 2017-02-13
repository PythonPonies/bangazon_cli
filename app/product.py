class Product:
    """ The Product class creates a new product with data passed to it.

    Method List   __init__ instansiates the new Product with product_name, price, quantity
    Arguments     The object argument lets the Customer class inherit properites of object
    Author        Zoe LeBlanc, Python Ponies
    """
    def __init__(self, title, description, price, quantity):
        """
        A new product is created based on the arguments passed in: title, price, quantity. 
        """
        self.__title = title
        self.__description = description
        self.__price = price
        self.__quantity = quantity

    def get_product_title(self):
        """ get_product_title returns the name of a product object. Self is needed as an argument to access the product object.
        """
        return self.__title

    def get_product_description(self):
        """ get_product_description returns the description of a product object. Self is needed as an argument to access the product object.
        """
        return self.__description

    def get_product_price(self):
        """ get_product_price returns the price of a product object. Self is needed as an argument to access the product object.
        """
        return self.__price

    def get_product_quantity(self):
        """ get_product_quantity returns the quantity of a product object. Self is needed as an argument to access the product object.
        """
        return self.__quantity
