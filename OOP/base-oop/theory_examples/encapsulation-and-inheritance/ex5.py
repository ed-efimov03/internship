class BankAccount:
    def __init__(self, balance, interest_rate):
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def deposit(self, amount: float):
        self.__balance += amount
        operation = f"Внесение наличных на счет: {amount}"
        self.__transactions.append(operation)

    def withdraw(self, amount: float):
        if amount <= self.__balance:
            self.__balance -= amount
            operation = f"Снятие наличных: {amount}"
            self.__transactions.append(operation)
        else:
            print("Недостаточно средств на счете")

    def add_interest(self):
        interest = self.__balance * self.__interest_rate
        self.__balance += interest
        operation = f"Начислены проценты по вкладу: {interest}"
        self.__transactions.append(operation)

    def history(self):
        print(*self.__transactions, sep="\n")

account = BankAccount(100000, 0.05)

account.deposit(15000)

account.withdraw(7500)

account.add_interest()

account.history()