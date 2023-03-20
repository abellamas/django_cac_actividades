from person import Person
from account import Account, YoungAccount

def main():
    "Ejercicio 6"
    # person1 = Person()
    # person1.name = 'Abel'
    # person1.age = 23
    # person1.dni = 41862171
    # person1.show()

    "Ejercicio 7"
    # account = Account('Abel', 23, 41862171)
    # print(account.holder)
    # account.holder = Person('Mauricio', 23, 41862171)
    # account.show()
    # account.deposit(12)
    # account.show()
    # account.extract(0.5)
    # account.show()

    "Ejercicio 8"
    young_account = YoungAccount('Abel', 23, 41862171, 10)
    print(young_account.is_valid())
    young_account.deposit(40)
    young_account.extract(12)
    young_account.show()



if __name__ == '__main__':
    main()