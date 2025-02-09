class Employee:
    """Класс, представляющий сотрудника.

    Этот класс хранит информацию о сотруднике.
    Также предоставляет методы для установки бонуса и получения информации о сторуднике.

    Attributes:
        name (str): Имя сотрудника
        age (int): Возраст сотрудника
        salary (float): Зарплата сотрудника
        bonus (float): Бонус
    """

    def __init__(self, name: str, age: int, salary: float):
        """Инициализирует экземляр класса Employee

        Args:
            name (str): Имя сотрудника
            age (int): Возраст сотрудника
            salary (float): Зарплата сотрудника

        Raises:
            ValueError: Невалидное значение
        """

        if not(isinstance(name, str) and isinstance(age, int) and (isinstance(salary, int) or isinstance(salary, float))):
            raise ValueError("Вы ввели невалидные значения")
        
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = 0

    def set_bonus(self, bonus: float):
        """Устанавливает бонус

        Args:
            bonus (float): Бонус

        Raises:
            ValueError: Невалидное значение
        """

        if not(isinstance(bonus, float) or isinstance(bonus, int)):
            raise ValueError("Вы ввели невалидные значения")
        
        self.__bonus = bonus

    def get_name(self) -> str:
        """Возвращает имя сотрудника

        Returns:
            str: Имя сотрудника
        """
        return self.__name
    
    def get_age(self) -> int:
        """Возвращает возраст сотрудника

        Returns:
            str: Возраст сотрудника
        """

        return self.__age
    
    def get_salary(self) -> float:
        """Возвращает зарплату сотрудника

        Returns:
            str: Зарплату сотрудника
        """

        return self.__salary
    
    def get_bonus(self) -> float:
        """Возвращает бонус сотрудника

        Returns:
            str: Бонус сотрудника
        """

        return self.__bonus
    
    def get_total_salary(self) -> float:
        """Возвращает общую зп сотрудника

        Returns:
            str: Общая зп сотрудника
        """

        return self.__salary + self.__bonus


#Проверяем работу программы
employee = Employee("Марина Арефьева", 30, 90000)

employee.set_bonus(15000)

print("Имя:", employee.get_name())
print("Возраст:", employee.get_age())
print("Зарплата:", employee.get_salary())
print("Бонус:", employee.get_bonus())
print("Итого начислено:", employee.get_total_salary())