from models.person import Person


class Supplier(Person):
    def __int__(self, dni, cuit, fname, lname, tel, address, company_name=None):
        super().__init__(dni, fname, lname, tel, address)
        self.__cuit = cuit
        self.__company_name = company_name

    @property
    def cuit(self):
        return self.__cuit

    @cuit.setter
    def cuit(self, value):
        self.__cuit = value

    @property
    def companyName(self):
        return self.__company_name

    @companyName.setter
    def companyName(self, value):
        self.__company_name = value

    def __str__(self):
        return (f'Supplier {self.cuit()}\n'
                f'{super()}'
                f'Company name: {self.companyName}\n')