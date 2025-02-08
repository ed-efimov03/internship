# Импортируем необходимые модули: ABC (Abstract Base Class) и abstractmethod для создания абстрактных классов и методов
from abc import ABC, abstractmethod

# Абстрактный класс, представляющий общий интерфейс для музыкальных инструментов
class Instrument(ABC):
    # Абстрактный метод для получения названия инструмента
    @abstractmethod
    def get_name(self):
        pass

    # Абстрактный метод для получения типа инструмента
    @abstractmethod
    def get_type(self):
        pass

    # Абстрактный метод для получения звука инструмента
    @abstractmethod
    def get_sound(self):
        pass

    # Абстрактный метод для игры на инструменте
    @abstractmethod
    def play(self):
        pass

# Класс струнных инструментов, наследуется от Instrument
class StringedInstrument(Instrument):
    def __init__(self, name: str, type: str, sound: str):
        self.name = name  # Название инструмента
        self.type = type  # Тип инструмента
        self.sound = sound  # Звук инструмента

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_sound(self):
        return self.sound

    def play(self):
        return f"Звучит струнный инструмент {self.get_name()}"

# Класс ударных инструментов, наследуется от Instrument
class PercussionInstrument(Instrument):
    def __init__(self, name: str, type: str, sound: str):
        self.name = name  # Название инструмента
        self.type = type  # Тип инструмента
        self.sound = sound  # Звук инструмента

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_sound(self):
        return self.sound

    def play(self):
        return f"Звучит ударный инструмент {self.get_name()}"

# Класс Оркестр, содержащий коллекцию инструментов
class Orchestra:
    def __init__(self):
        self.instrument_list = []  # Список инструментов в оркестре

    # Метод для добавления инструмента в оркестр
    def add_instrument(self, instrument: Instrument):
        self.instrument_list.append(instrument)

    # Метод для получения списка всех инструментов
    def list_instruments(self):
        return [instrument.get_name() for instrument in self.instrument_list]
    
    # Метод для получения списка только струнных инструментов
    def list_stringed_instruments(self):
        return [instrument.get_name() for instrument in self.instrument_list if isinstance(instrument, StringedInstrument)]
    
    # Метод для получения списка только ударных инструментов
    def list_percussion_instruments(self):
        return [instrument.get_name() for instrument in self.instrument_list if isinstance(instrument, PercussionInstrument)]

# Создание экземпляров различных инструментов
chello = StringedInstrument("виолончель", "струнный инструмент", "Strum")
maracas = PercussionInstrument("маракасы", "ударный инструмент", "Maracas")
violin = StringedInstrument("скрипка", "струнный инструмент", "Virtuoso")
drums = PercussionInstrument("барабан", "ударный инструмент", "Beat")    

# Создание оркестра и добавление в него инструментов
orchestra = Orchestra()
orchestra.add_instrument(chello)
orchestra.add_instrument(maracas)
orchestra.add_instrument(violin)
orchestra.add_instrument(drums)

# Вывод информации о составе оркестра
print("В оркестрe есть инструменты:", ', '.join(orchestra.list_instruments()))  
print("Струнные инструменты:", ', '.join(orchestra.list_stringed_instruments())) 
print("Ударные инструменты:", ', '.join(orchestra.list_percussion_instruments()))  

# Демонстрация игры на инструментах
print(chello.play())    
print(drums.play())
