from person import Person

class Account():
    """
        A class representing a bank account

        ...

        Attributes
        ----------
        holder : Person
            the holder is an instance of a Person class, this is required.

        Methods
        -------
        deposit(amount:float or int)
            allow deposit money in the bank account, if the amount is negative the deposit nothing is done

        extract(amount:float or int)
            allow extract money of the bank account, the amount required must be less than the amount available in the account.

    """

    def __init__(self, name: str, age: int, dni: int):
        self._holder = Person(name, age, dni)
        self.__amount = 0.0

    @property
    def holder(self):
        return f'Holder data\n name\t age\t dni\t \n {self._holder.name}\t {self._holder.age}\t {self._holder.dni}'

    @holder.setter
    def holder(self, person):
        if type(person) == Person:
            self._holder = person
        else:
            raise TypeError('the holder must be a person object')

    def deposit(self, amount: float or int):
        if type(amount) == int or type(amount) == float:
            if amount > 0:
                self.__amount += amount
        else:
            raise TypeError('the amount must be a float')

    def extract(self, amount: float or int):
        if type(amount) == int or type(amount) == float:
            if amount <= self.__amount:
                self.__amount = self.__amount - amount
            else:
                raise ValueError('the requested amount is not available')
        else:
            raise TypeError('the amount must be a float')

    def show(self):
        print(f'Account data\n name\t age\t dni\t amount\n'
              f'{self._holder.name}\t {self._holder.age}\t {self._holder.dni}\t {self.__amount}')


class YoungAccount(Account):
    """
        A new class of account, called Young Account to holders between 18 and 25 years old.

        Attributes
        ----------
        holder : Person(name, age, dni)
            the holder is an instance of a Person class, this is required.

        Methods
        -------
        deposit(amount:float or int)
            allow deposit money in the bank account, if the amount is negative the deposit nothing is done

        is_valid()
            if the holder have between 18 and 25 return True.

        extract(amount:float or int)
            allow extract money of the bank account if the user is valid, the amount required must be less than
            the amount available in the account.

    """
    def __init__(self, name, age, dni, bonus):
        super().__init__(name, age, dni)
        self.__bonus = bonus

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus):
        self.__bonus = bonus

    def is_valid(self):

        # print(self._holder.age)
        return True if 18 < self._holder.age < 25 else False

    def extract(self, amount):
        if self.is_valid() == True:
            super().extract(amount)
        else:
            print('No se puede extraer')

    def show(self):
        print(f'Young account, {self.bonus} % bonus')
        super().show()

