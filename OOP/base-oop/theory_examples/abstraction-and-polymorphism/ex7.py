# Базовый класс для вина
class Wine:
    def __init__(self, name: str, grape: str, year: int):
        self.name = name  # Название вина
        self.grape = grape  # Сорт винограда
        self.year = year  # Год производства

# Класс для красного вина, наследуется от Wine
class RedWine(Wine):
    def serve(self):
        print(f"Красное вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year} году, рекомендуем подавать комнатной температуры.")

# Класс для белого вина, наследуется от Wine
class WhiteWine(Wine):
    def serve(self):
        print(f"Белое вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year} году, рекомендуем подавать хорошо охлажденным.")

# Класс для розового вина, наследуется от Wine
class RoseWine(Wine):
    def serve(self):
        print(f"Розовое вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year} году, рекомендуем подавать слегка охлажденным.")    

# Класс винодельни, содержащий список вин
class Winery:
    def __init__(self):
        self.wines_list = []  # Список вин

    # Метод для добавления вина в коллекцию
    def add_wine(self, wine: Wine):
        self.wines_list.append(wine)

    # Метод для сервировки всех вин в коллекции
    def serve_wines(self):
        for wine in self.wines_list:
            wine.serve()

# Создание винодельни и добавление в неё вин
winery = Winery()
winery.add_wine(RedWine("Cabernet Sauvignon", "Каберне Совиньон", 2015))
winery.add_wine(WhiteWine("Chardonnay", "Шардоне", 2018))
winery.add_wine(RoseWine("Grenache", "Гренаш", 2020))

# Сервировка всех вин
winery.serve_wines()
