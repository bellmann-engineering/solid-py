class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        pass

    def accelerate(self):
        pass

class GasolineVehicle(Vehicle):
    def start_engine(self):
        # Code zum Starten eines Benzinmotors
        pass

    def accelerate(self):
        # Code zur Beschleunigung eines Fahrzeugs mit Benzinmotor
        pass

class DieselVehicle(Vehicle):
    def start_engine(self):
        # Code zum Starten eines Dieselmotors
        pass

    def accelerate(self):
        # Code zur Beschleunigung eines Fahrzeugs mit Dieselmotor
        pass
