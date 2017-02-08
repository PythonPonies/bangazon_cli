class Product:

    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_product_name(self):
        return self.__name

    def get_product_price(self):
        return self.__price

    def get_product_quantity(self):
        return self.__quantity

# if __name__ == '__main__':