class Car:
    def accelerate(self):
        # Code zur Beschleunigung des Autos
        pass

    def brake(self):
        # Code zum Bremsen des Autos
        pass

class SelfDrivingCar(Car):
    def accelerate(self):
        raise NotImplementedError("Self-driving cars cannot be manually accelerated")

    def brake(self):
        raise NotImplementedError("Self-driving cars cannot be manually braked")

    def engage_auto_pilot(self):
        # Code zum Aktivieren des Autopiloten
        pass
