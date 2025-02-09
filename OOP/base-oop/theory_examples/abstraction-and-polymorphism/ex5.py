from abc import ABC, abstractmethod

class Instrument(ABC):
    """Абстрактный класс, представляющий музыкальный инструмент.
    
    Каждый инструмент должен реализовывать методы для получения имени, типа, звука и для воспроизведения.
    """

    @abstractmethod
    def get_name(self):
        """Возвращает имя инструмента."""
        pass

    @abstractmethod
    def get_type(self):
        """Возвращает тип инструмента."""
        pass

    @abstractmethod
    def get_sound(self):
        """Возвращает звук, который издает инструмент."""
        pass

    @abstractmethod
    def play(self):
        """Метод воспроизведения звука инструмента."""
        pass

class StringedInstrument(Instrument):
    """Класс для струнных инструментов.

    Реализует методы для работы со струнными инструментами, например, скрипками или виолончелями.
    """

    def __init__(self, name: str, type: str, sound: str):
        """Инициализирует струнный инструмент с его именем, типом и звуком."""
        self.name = name
        self.type = type
        self.sound = sound

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_sound(self):
        return self.sound

    def play(self):
        """Возвращает строку с воспроизведением струнного инструмента."""
        return f"Звучит струнный инструмент {self.get_name()}"

class PercussionInstrument(Instrument):
    """Класс для ударных инструментов.

    Реализует методы для работы с ударными инструментами, например, барабанами или маракасами.
    """

    def __init__(self, name: str, type: str, sound: str):
        """Инициализирует ударный инструмент с его именем, типом и звуком."""
        self.name = name
        self.type = type
        self.sound = sound

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_sound(self):
        return self.sound

    def play(self):
        """Возвращает строку с воспроизведением ударного инструмента."""
        return f"Звучит ударный инструмент {self.get_name()}"

class Orchestra:
    """Класс для управления оркестром.

    Позволяет добавлять инструменты, а также фильтровать и выводить список инструментов по их типам.
    """

    def __init__(self):
        """Инициализирует оркестр с пустым списком инструментов."""
        self.instrument_list = []

    def add_instrument(self, instrument: Instrument):
        """Добавляет инструмент в оркестр.

        Args:
            instrument (Instrument): Инструмент, который добавляется в оркестр.
        """
        self.instrument_list.append(instrument)

    def list_instruments(self):
        """Возвращает список всех инструментов в оркестре."""
        return [instrument.get_name() for instrument in self.instrument_list]
    
    def list_stringed_instruments(self):
        """Возвращает список всех струнных инструментов в оркестре."""
        return [instrument.get_name() for instrument in self.instrument_list if isinstance(instrument, StringedInstrument)]
    
    def list_percussion_instruments(self):
        """Возвращает список всех ударных инструментов в оркестре."""
        return [instrument.get_name() for instrument in self.instrument_list if isinstance(instrument, PercussionInstrument)]


# Создание экземпляров инструментов
chello = StringedInstrument("виолончель", "струнный инструмент", "Strum")
maracas = PercussionInstrument("маракасы", "ударный инструмент", "Maracas")
violin = StringedInstrument("скрипка", "струнный инструмент", "Virtuoso")
drums = PercussionInstrument("барабан", "ударный инструмент", "Beat")    

# Создание оркестра и добавление инструментов
orchestra = Orchestra()
orchestra.add_instrument(chello)
orchestra.add_instrument(maracas)
orchestra.add_instrument(violin)
orchestra.add_instrument(drums)

# Вывод информации о музыкальных инструментах
print("В оркестрe есть инструменты:", ', '.join(orchestra.list_instruments()))  
print("Струнные инструменты:", ', '.join(orchestra.list_stringed_instruments())) 
print("Ударные инструменты:", ', '.join(orchestra.list_percussion_instruments()))  

# Воспроизведение звуков инструментов
print(chello.play())    
print(drums.play())
