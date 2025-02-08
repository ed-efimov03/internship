class Recipe:
    def __init__(self, dish: str, ingredients: list):
        self.dish = dish  
        self.ingredients = ingredients 

    def print_ingredients(self):
        print(f"Ингредиенты для {self.dish}:") 
        for ing in self.ingredients: 
            print(f"- {ing}") 

    def cook(self):
        print(f"Сегодня мы готовим {self.dish}.") 
        print(f"Выполняем инструкцию по приготовлению блюда {self.dish}...")  
        print(f"Блюдо {self.dish} готово!") 


spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])


spaghetti.print_ingredients()


spaghetti.cook()  


cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])


cake.print_ingredients()


cake.cook()
