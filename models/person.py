class Person:
    def __init__(self, dni, fname, lname, address, tel):
        self._dni = dni
        self._first_name = fname
        self._last_name = lname
        self._tel = tel
        self._address = address

    @property
    def dni(self):
        return self._dni

    @id.setter
    def dni(self, value):
        self._dni = value

    @property
    def firstName(self):
        return self._first_name

    @firstName.setter
    def firsName(self, value):
        self._first_name = value

    @property
    def lastName(self):
        return self._last_name

    @lastName.setter
    def lastName(self, value):
        self._last_name = value


    @property
    def tel(self):
        return self._tel

    @tel.setter
    def tel(self, value):
        self._tel = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    def __str__(self):
        return (f'Person:'
                f'DNI: {self.dni}'
                f'First Name: {self.firstName}'
                f'Last Name: {self.lastName}'
                f'Telephone: {self.tel}'
                f'Address: {self.address}')

