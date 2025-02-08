# Класс Candy представляет общие характеристики конфет
class Candy:
    # Инициализация конфеты с названием, ценой и весом
    def __init__(self, name: str, price: float, weight: float):
        self.name = name  # Название конфеты
        self.price = price  # Цена конфеты
        self.weight = weight  # Вес конфеты

# Класс Chocolate наследует от Candy и представляет шоколадные конфеты
class Chocolate(Candy):
    # Инициализация шоколадных конфет с добавлением процента какао и типа шоколада
    def __init__(self, name: str, price: float, weight: float, cocoa_percentage: float, chocolate_type: str):
        super().__init__(name, price, weight)  # Вызов конструктора родительского класса
        self.cocoa_percentage = cocoa_percentage  # Процент содержания какао в шоколаде
        self.chocolate_type = chocolate_type  # Тип шоколада (молочный, тёмный и т. д.)

# Класс Gummy наследует от Candy и представляет жевательные мармелады
class Gummy(Candy):
    # Инициализация жевательных мармеладок с добавлением вкуса и формы
    def __init__(self, name: str, price: float, weight: float, flavor: str, shape: str):
        super().__init__(name, price, weight)  # Вызов конструктора родительского класса
        self.flavor = flavor  # Вкус мармелада
        self.shape = shape  # Форма мармелада (например, медведь, круглый и т. д.)

# Класс HardCandy наследует от Candy и представляет фруктовые леденцы
class HardCandy(Candy):
    # Инициализация леденцов с добавлением вкуса и информации о начинке
    def __init__(self, name: str, price: float, weight: float, flavor: str, filled: str):
        super().__init__(name, price, weight)  # Вызов конструктора родительского класса
        self.flavor = flavor  # Вкус леденца
        self.filled = filled  # Указывает, есть ли начинка в леденце (True или False)

# Создаем объект шоколадных конфет
chocolate = Chocolate(name="Швейцарские луга", price=325.50, weight=220, cocoa_percentage=40, chocolate_type="молочный")

# Создаем объект жевательных мармеладок
gummy = Gummy(name="Жуй-жуй", price=76.50, weight=50, flavor="вишня", shape="медведь")

# Создаем объект фруктовых леденцов
hard_candy = HardCandy(name="Crazy Фрукт", price=35.50, weight=25, flavor="манго", filled=True)

# Выводим информацию о шоколадных конфетах
print("Шоколадные конфеты:")
print(f"Название конфет: {chocolate.name}")  # Выводим название шоколада
print(f"Стоимость: {chocolate.price} руб")  # Выводим цену шоколада
print(f"Вес брутто: {chocolate.weight} г")  # Выводим вес шоколада
print(f"Процент содержания какао: {chocolate.cocoa_percentage}")  # Выводим процент какао
print(f"Тип шоколада: {chocolate.chocolate_type}")  # Выводим тип шоколада

# Выводим информацию о жевательных мармеладках
print("\nМармелад жевательный:")
print(f"Название конфет: {gummy.name}")  # Выводим название мармелада
print(f"Стоимость: {gummy.price} руб")  # Выводим цену мармелада
print(f"Вес брутто: {gummy.weight} г")  # Выводим вес мармелада
print(f"Вкус: {gummy.flavor}")  # Выводим вкус мармелада
print(f"Форма: {gummy.shape}")  # Выводим форму мармелада

# Выводим информацию о фруктовых леденцах
print("\nФруктовые леденцы:")
print(f"Название конфет: {hard_candy.name}")  # Выводим название леденца
print(f"Стоимость: {hard_candy.price} руб")  # Выводим цену леденца
print(f"Вес брутто: {hard_candy.weight} г")  # Выводим вес леденца
print(f"Вкус: {hard_candy.flavor}")  # Выводим вкус леденца
print(f"Начинка: {hard_candy.filled}")  # Выводим, есть ли начинка у леденца
