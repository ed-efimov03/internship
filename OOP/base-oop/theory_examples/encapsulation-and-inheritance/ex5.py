class BankAccount:
    """Класс, представляющий банковский счет.

    Этот класс хранит информацию о банковском счете.
    Также предоставляет методы для добавления суммы к балансу, вычитания суммы из баланса и добавления процентов к счету.

    Attributes:
        balance (float): Баланс
        interest_rate (float): Процентная ставка
        transactions (list): Список транзакций
    """

    def __init__(self, balance: float, interest_rate: float):
        """Инициализирует экземляр класса BankAccount

        Args:
            balance (float): Баланс
            interest_rate (float): Процентная ставка

        Raises:
            ValueError: Невалидное значение
        """

        if not((isinstance(balance, int) or isinstance(balance, float)) and 
               (isinstance(interest_rate, int) or isinstance(interest_rate, float))):
            raise ValueError("Вы ввели невалидные значения")

        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def deposit(self, amount: float):
        """Добавляет сумму к балансу и регистрирует транзакцию.

        Args:
            amount (float): Сумма, которую добовляет

        Raises:
            ValueError: Невалидное значение
        """

        if not((isinstance(amount, int) or isinstance(amount, float))):
            raise ValueError("Вы ввели невалидное значение")

        self.__balance += amount
        operation = f"Внесение наличных на счет: {amount}"
        self.__transactions.append(operation)

    def withdraw(self, amount: float):
        """Вычитает сумму из баланса и записывает транзакцию.

        Args:
            amount (float): Сумма, которую списывает.

        Raises:
            ValueError: Невалидное значение.
        """

        if not((isinstance(amount, int) or isinstance(amount, float))):
            raise ValueError("Вы ввели невалидное значение")

        if amount <= self.__balance:
            self.__balance -= amount
            operation = f"Снятие наличных: {amount}"
            self.__transactions.append(operation)
        else:
            print("Недостаточно средств на счете")

    def add_interest(self):
        """Добавляет проценты к счету на основе interest_rate и записывает транзакцию.
        """

        interest = self.__balance * self.__interest_rate
        self.__balance += interest
        operation = f"Начислены проценты по вкладу: {interest}"
        self.__transactions.append(operation)

    def history(self):
        """Печатает список всех операций по счету.
        """
        print(*self.__transactions, sep="\n")


#Проверяем работу программы
account = BankAccount(100000, 0.05)

account.deposit(15000)
account.withdraw(7500)
account.add_interest()
account.history()