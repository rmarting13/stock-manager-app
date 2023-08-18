class Product:
    def __int__(self, code, description, price, brand):
        self.__code = code
        self.__description = description
        self.__brand = brand
        self.__price = price

    @property
    def code(self):
        return self.__code

    @code.setter
    def id(self, value):
        self.__code = value

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.__name = value

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
        return (f'Product {self.id()}\n'
                f'Name: {self.name}\n'
                f'Brand: {self.brand}\n'
                f'Price: {self.price}\n')
