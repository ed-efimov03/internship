class Recipe:
    """Класс, представляющий рецепт блюда.

    Этот класс позволяет хранить информацию о блюде и его ингредиентах.
    Также предоставляет методы для вывода списка ингредиентов и имитации процесса приготовления.

    Attributes:
        dish (str): Название блюда
        ingredients (list): Список ингредиентов, необходимых для приготовления блюда
    """

    def __init__(self, dish: str, ingredients: list):
        """Инициализирует экземляр класса Recipe

        Args:
            dish (str): _description_
            ingredients (list): _description_

        Raises:
            ValueError: Невалидное значение.
        """

        if not(isinstance(dish, str) and isinstance(ingredients, list)):
            raise ValueError("Вы ввели невалидные значения")
        
        self.dish = dish  
        self.ingredients = ingredients 

    def print_ingredients(self):
        """Выводит список ингредиентов для блюда
        """

        print(f"Ингредиенты для {self.dish}:") 
        for ing in self.ingredients: 
            print(f"- {ing}") 

    def cook(self):
        """Имитирует процесс приготовления блюда
        """

        print(f"Сегодня мы готовим {self.dish}.") 
        print(f"Выполняем инструкцию по приготовлению блюда {self.dish}...")  
        print(f"Блюдо {self.dish} готово!") 


#Проверяем работу программы
spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
spaghetti.print_ingredients()
spaghetti.cook()  

cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
cake.print_ingredients()
cake.cook()
