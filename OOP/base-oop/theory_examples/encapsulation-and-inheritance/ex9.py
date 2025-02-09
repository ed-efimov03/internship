class Candy:
    """Базовый класс, представляющий сладость.

    Содержит информацию о названии, цене и весе.

    Attributes:
        name (str): Название сладости
        price (float): Цена
        weight (float): Вес
    """

    def __init__(self, name: str, price: float, weight: float):
        """Инициализирует экземляр класса Candy

        Args:
            name (str): Название сладости
            price (float): Цена
            weight (float): Вес

        Raises:
            ValueError: Невалидное значение
        """
        if not(isinstance(name, str) and (isinstance(price, float) or isinstance(price, int))
                and (isinstance(weight, float) or isinstance(weight, int))):
            raise ValueError("Вы ввели невалидные значения")

        self.name = name
        self.price = price
        self.weight = weight

class Chocolate(Candy):
    """Класс, представляющий шоколадную конфету.

    Наследуется от Candy и добавляет информацию о типе шоколада и проценте какао.

    Attributes:
        name (str): Название сладости
        price (float): Цена
        weight (float): Вес
        cocoa_percentage (float): Процентное содержание какао
        chocolate_type (str): Тип шоколада
    """

    def __init__(self, name: str, price: float, weight: float, cocoa_percentage: float, chocolate_type: str):
        """Инициализирует экземляр класса Chocolate

        Args:
            name (str): Название сладости
            price (float): Цена
            weight (float): Вес
            cocoa_percentage (float): Процентное содержание какао
            chocolate_type (str): Тип шоколада

        Raises:
            ValueError: Невалидное значение
        """

        if not(isinstance(name, str) and (isinstance(price, float) or isinstance(price, int))
                and (isinstance(weight, float) or isinstance(weight, int)) and (isinstance(cocoa_percentage, float) or isinstance(cocoa_percentage, int))
                and isinstance(chocolate_type, str)):
            raise ValueError("Вы ввели невалидные значения")

        super().__init__(name, price, weight)
        self.cocoa_percentage = cocoa_percentage
        self.chocolate_type = chocolate_type

class Gummy(Candy):
    """Класс, представляющий жевательный мармелад.

    Наследуется от Candy и добавляет информацию о вкусе и форме.

    Attributes:
        name (str): Название сладости
        price (float): Цена
        weight (float): Вес
        flavor (str): Вкус
        shape (str): Форма
    """

    def __init__(self, name: str, price: float, weight: float, flavor: str, shape: str):
        """Инициализирует экземляр класса Gummy

        Args:
            name (str): Название сладости
            price (float): Цена
            weight (float): Вес
            flavor (str): Вкус
            shape (str): Форма

        Raises:
            ValueError: Невалидное значение
        """

        if not(isinstance(name, str) and (isinstance(price, float) or isinstance(price, int))
                and (isinstance(weight, float) or isinstance(weight, int)) and (isinstance(flavor, str))
                and isinstance(shape, str)):
            raise ValueError("Вы ввели невалидные значения")
        
        super().__init__(name, price, weight)
        self.flavor = flavor
        self.shape = shape

class HardCandy(Candy):
    """Класс, представляющий леденец.

    Наследуется от Candy и добавляет информацию о вкусе и наличии начинки.
    
    Attributes:
        name (str): Название сладости
        price (float): Цена
        weight (float): Вес
        flavor (str): Вкус
        filled (bool): Начинка
    """

    def __init__(self, name: str, price: float, weight: float, flavor: str, filled: bool):
        """Инициализирует экземляр класса HardCandy

        Args:
            name (str): Название сладости
            price (float): Цена
            weight (float): Вес
            flavor (str): Вкус
            filled (bool): Начинка

        Raises:
            ValueError: Невалидное значение
        """

        if not(isinstance(name, str) and (isinstance(price, float) or isinstance(price, int))
                and (isinstance(weight, float) or isinstance(weight, int)) and (isinstance(flavor, str))
                and isinstance(filled, bool)):
            raise ValueError("Вы ввели невалидные значения")

        super().__init__(name, price, weight)
        self.flavor = flavor
        self.filled = filled


#Проверяем работу программы
chocolate = Chocolate(name="Швейцарские луга", price=325.50, weight=220, cocoa_percentage=40, chocolate_type="молочный")
gummy = Gummy(name="Жуй-жуй", price=76.50, weight=50, flavor="вишня", shape="медведь")
hard_candy = HardCandy(name="Crazy Фрукт", price=35.50, weight=25, flavor="манго", filled=True)

print("Шоколадные конфеты:")
print(f"Название конфет: {chocolate.name}")
print(f"Стоимость: {chocolate.price} руб")
print(f"Вес брутто: {chocolate.weight} г")
print(f"Процент содержания какао: {chocolate.cocoa_percentage}")
print(f"Тип шоколада: {chocolate.chocolate_type}")

print("\nМармелад жевательный:")
print(f"Название конфет: {gummy.name}")
print(f"Стоимость: {gummy.price} руб")
print(f"Вес брутто: {gummy.weight} г")
print(f"Вкус: {gummy.flavor}")
print(f"Форма: {gummy.shape}")

print("\nФруктовые леденцы:")
print(f"Название конфет: {hard_candy.name}")
print(f"Стоимость: {hard_candy.price} руб")
print(f"Вес брутто: {hard_candy.weight} г")
print(f"Вкус: {hard_candy.flavor}")
print(f"Начинка: {hard_candy.filled}")