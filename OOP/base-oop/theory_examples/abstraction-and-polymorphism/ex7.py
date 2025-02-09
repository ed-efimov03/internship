class Wine:
    """Базовый класс для вина."""
    
    def __init__(self, name: str, grape: str, year: int):
        """Инициализирует вино с заданным названием, сортом винограда и годом выпуска."""
        self.name = name
        self.grape = grape
        self.year = year

    def serve(self):
        """Метод для подачи вина, переопределяется в подклассах."""
        pass


class RedWine(Wine):
    """Класс для красного вина."""
    
    def serve(self):
        """Рекомендуемая температура подачи для красного вина."""
        print(f"Красное вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year} году, рекомендуем подавать комнатной температуры.")


class WhiteWine(Wine):
    """Класс для белого вина."""
    
    def serve(self):
        """Рекомендуемая температура подачи для белого вина."""
        print(f"Белое вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year} году, рекомендуем подавать хорошо охлажденным.")


class RoseWine(Wine):
    """Класс для розового вина."""
    
    def serve(self):
        """Рекомендуемая температура подачи для розового вина."""
        print(f"Розовое вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year} году, рекомендуем подавать слегка охлажденным.")


class Winery:
    """Класс для винодельни, хранящей список вин."""
    
    def __init__(self):
        """Инициализирует пустой список для хранения вин."""
        self.wines_list = []

    def add_wine(self, wine: Wine):
        """Добавляет вино в список вин."""
        self.wines_list.append(wine)

    def serve_wines(self):
        """Подает все вина из списка."""
        for wine in self.wines_list:
            wine.serve()


# Создание экземпляра винодельни
winery = Winery()

# Добавление различных видов вина в винодельню
winery.add_wine(RedWine("Cabernet Sauvignon", "Каберне Совиньон", 2015))
winery.add_wine(WhiteWine("Chardonnay", "Шардоне", 2018))
winery.add_wine(RoseWine("Grenache", "Гренаш", 2020))

# Подача всех вин
winery.serve_wines()
