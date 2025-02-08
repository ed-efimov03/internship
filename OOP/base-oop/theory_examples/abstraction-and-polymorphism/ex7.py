class Wine:
    def __init__(self, name: str, grape: str, year: int):
        self.name = name
        self.grape = grape
        self.year = year

class RedWine(Wine):
    def serve(self):
        print(f"Красное вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year} году, рекомендуем подавать комнатной температуры.")

class WhiteWine(Wine):
    def serve(self):
        print(f"Белое вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year} году, рекомендуем подавать хорошо охлажденным.")

class RoseWine(Wine):
    def serve(self):
        print(f"Розовое вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year} году, рекомендуем подавать слегка охлажденным.")    

class Winery:
    def __init__(self):
        self.wines_list = []

    def add_wine(self, wine: Wine):
        self.wines_list.append(wine)

    def serve_wines(self):
        for wine in self.wines_list:
            wine.serve()

winery = Winery()
winery.add_wine(RedWine("Cabernet Sauvignon", "Каберне Совиньон", 2015))
winery.add_wine(WhiteWine("Chardonnay", "Шардоне", 2018))
winery.add_wine(RoseWine("Grenache", "Гренаш", 2020))

winery.serve_wines()