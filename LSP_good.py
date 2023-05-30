class Car:
    def accelerate(self):
        # Code zur Beschleunigung des Autos
        pass

    def brake(self):
        # Code zum Bremsen des Autos
        pass

class SelfDrivingCar(Car):
    def engage_auto_pilot(self):
        # Code zum Aktivieren des Autopiloten
        pass

    def accelerate(self):
        self.engage_auto_pilot()

    def brake(self):
        self.engage_auto_pilot()
