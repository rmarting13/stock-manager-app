class Product:
    def __init__(self, code=None, description=None, price=None, brand=None):
        self.__code = code
        self.__description = description
        self.__brand = brand
        self.__price = price

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def __str__(self):
        return (f'Product:\n'
                f'Name: {self.description}\n'
                f'Brand: {self.brand}\n'
                f'Price: {self.price}\n')
