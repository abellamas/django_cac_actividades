class Person:
    """
    A class used to represent a Person

    ...

    Attributes
    ----------
    name : str
        name of the person, by default is None
    age : int
        age of the person, by default is None
    dni : int
        dni of the person, by default is None

    Methods
    -------
    show()
        Print the name, age and dni of the person
    is_adult()
        Return and boolean if the person is greater than 18 years old
    """
    def __init__(self, name:str = None, age:int = None, dni:int = None):
        self.__name = name
        self.__age = age
        self.__dni = dni

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name:str):
        if type(new_name) == str:
            self.__name = new_name
        else:
            raise TypeError('name must be a str')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age:int):
        if type(new_age) == int:
            if 0 <= new_age < 120:
                self.__age = new_age
            else:
                raise ValueError('Incorrect age, this must be an integer between 0 and 120')
        else:
            raise TypeError('age must be an integer')
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, new_dni:int):
        if type(new_dni) == int:
            if 999999 < new_dni < 100000000:
                self.__dni = new_dni
            else:
                raise ValueError('Dni must be an integer between 999999 and 100000000')
        else:
            raise TypeError('dni must be an integer')

    def show(self):
        print(f'name: {self.__name} \n age: {self.__age} \n dni: {self.__dni}')

    def is_adult(self):
        if self.__age >= 18:
            return True
        else:
            return False
