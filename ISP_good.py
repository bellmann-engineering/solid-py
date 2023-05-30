from abc import ABC, abstractmethod

class Startable(ABC):
    @abstractmethod
    def start(self):
        pass

class Acceleratable(ABC):
    @abstractmethod
    def accelerate(self):
        pass

class Brakable(ABC):
    @abstractmethod
    def brake(self):
        pass

class Car(Startable, Acceleratable, Brakable):
    def start(self):
        # Code zum Starten des Autos
        pass

    def accelerate(self):
        # Code zum Beschleunigen des Autos
        pass

    def brake(self):
        # Code zum Bremsen des Autos
        pass

class Bicycle(Acceleratable, Brakable):
    def accelerate(self):
        # Code zum Treten und Beschleunigen des Fahrrads
        pass

    def brake(self):
        # Code zum Bremsen des Fahrrads
        pass
