class BankAccount:
    # Инициализация банковского счета с балансом, процентной ставкой и списком операций
    def __init__(self, balance, interest_rate):
        self.__balance = balance  # Баланс счета
        self.__interest_rate = interest_rate  # Процентная ставка по вкладу
        self.__transactions = []  # Список операций по счету

    # Метод для внесения средств на счет
    def deposit(self, amount: float):
        self.__balance += amount  # Увеличиваем баланс на сумму депозита
        operation = f"Внесение наличных на счет: {amount}"  # Записываем операцию
        self.__transactions.append(operation)  # Добавляем операцию в историю

    # Метод для снятия средств с счета
    def withdraw(self, amount: float):
        if amount <= self.__balance:  # Проверяем, достаточно ли средств на счете
            self.__balance -= amount  # Уменьшаем баланс на сумму снятия
            operation = f"Снятие наличных: {amount}"  # Записываем операцию
            self.__transactions.append(operation)  # Добавляем операцию в историю
        else:
            print("Недостаточно средств на счете")  # Сообщение о недостаточности средств

    # Метод для начисления процентов по вкладу
    def add_interest(self):
        interest = self.__balance * self.__interest_rate  # Вычисляем проценты
        self.__balance += interest  # Добавляем проценты к балансу
        operation = f"Начислены проценты по вкладу: {interest}"  # Записываем операцию
        self.__transactions.append(operation)  # Добавляем операцию в историю

    # Метод для вывода истории всех операций
    def history(self):
        print(*self.__transactions, sep="\n")  # Выводим все операции по счету

# создаем объект счета с балансом 100000 и процентом по вкладу 0.05
account = BankAccount(100000, 0.05)

# вносим 15 тысяч на счет
account.deposit(15000)

# снимаем 7500 рублей
account.withdraw(7500)

# начисляем проценты по вкладу
account.add_interest()

# печатаем историю операций
account.history()
