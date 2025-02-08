from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_sound(self):
        pass

    @abstractmethod
    def play(self):
        pass

class StringedInstrument(Instrument):
    def __init__(self, name: str, type: str, sound: str):
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
        return f"Звучит струнный инструмент {self.get_name()}"

class PercussionInstrument(Instrument):
    def __init__(self, name: str, type: str, sound: str):
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
        return f"Звучит ударный инструмент {self.get_name()}"

class Orchestra:
    def __init__(self):
        self.instrument_list = []

    def add_instrument(self, instrument: Instrument):
        self.instrument_list.append(instrument)

    def list_instruments(self):
        return [instrument.get_name() for instrument in self.instrument_list]
    
    def list_stringed_instruments(self):
        return [instrument.get_name() for instrument in self.instrument_list if isinstance(instrument, StringedInstrument)]
    
    def list_percussion_instruments(self):
        return [instrument.get_name() for instrument in self.instrument_list if isinstance(instrument, PercussionInstrument)]

chello = StringedInstrument("виолончель", "струнный инструмент", "Strum")
maracas = PercussionInstrument("маракасы", "ударный инструмент", "Maracas")
violin = StringedInstrument("скрипка", "струнный инструмент", "Virtuoso")
drums = PercussionInstrument("барабан", "ударный инструмент", "Beat")    

orchestra = Orchestra()
orchestra.add_instrument(chello)
orchestra.add_instrument(maracas)
orchestra.add_instrument(violin)
orchestra.add_instrument(drums)

print("В оркестрe есть инструменты:", ', '.join(orchestra.list_instruments()))  
print("Струнные инструменты:", ', '.join(orchestra.list_stringed_instruments())) 
print("Ударные инструменты:", ', '.join(orchestra.list_percussion_instruments()))  

print(chello.play())    
print(drums.play())