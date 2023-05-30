from abc import ABC, abstractmethod

class Drivable(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

class Car(Drivable):
    def start(self):
        # Code zum Starten des Autos
        pass

    def accelerate(self):
        # Code zum Beschleunigen des Autos
        pass

    def brake(self):
        # Code zum Bremsen des Autos
        pass

class Bicycle(Drivable):
    def start(self):
        # Nicht relevant für ein Fahrrad, führt zu einer leeren Implementierung
        pass

    def accelerate(self):
        pass

    def brake(self):
        pass
