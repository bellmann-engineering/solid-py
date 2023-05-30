class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    
    def start_engine(self):
        if self.fuel_type == "gasoline":
            # Code zum Starten eines Benzinmotors
            pass
        elif self.fuel_type == "diesel":
            # Code zum Starten eines Dieselmotors
            pass
    
    def accelerate(self):
        if self.fuel_type == "gasoline":
            # Code zur Beschleunigung eines Fahrzeugs mit Benzinmotor
            pass
        elif self.fuel_type == "diesel":
            # Code zur Beschleunigung eines Fahrzeugs mit Dieselmotor
            pass
