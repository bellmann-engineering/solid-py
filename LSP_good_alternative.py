class Car:
    def accelerate(self):
        # Code zur Beschleunigung des Autos
        pass

    def brake(self):
        # Code zum Bremsen des Autos
        pass

class SelfDrivingCar:
    def __init__(self, car):
        self.car = car

    def engage_auto_pilot(self):
        # Code zum Aktivieren des Autopiloten
        pass

    def accelerate(self):
        self.engage_auto_pilot()

    def brake(self):
        self.engage_auto_pilot()
