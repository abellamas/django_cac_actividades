from person import Person

class Account():
    """
        A class representing a bank account

        ...

        Attributes
        ----------
        holder : Person
            the holder is a Person object with the name, age and dni. This is required attribute

        Methods
        -------
        deposit(amount:float or int)
            allow deposit money in the bank account, if the amount is negative the deposit nothing is done

        extract(amount:float or int)
            allow extract money of the bank account, the amount required must be less than the amount available in the account.

    """

    def __init__(self, name: str, age: int, dni: int):
        self.__holder = Person(name, age, dni)
        self.__amount = 0.0

    @property
    def holder(self):
        return f'Holder data\n name\t age\t dni\t \n {self.__holder.name}\t {self.__holder.age}\t {self.__holder.dni}'

    @holder.setter
    def holder(self, person):
        if type(person) == Person:
            self.__holder = person
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
              f'{self.__holder.name}\t {self.__holder.age}\t {self.__holder.dni}\t {self.__amount}')
