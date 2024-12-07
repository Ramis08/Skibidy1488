class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def describe_vehicle(self):
        return f"This vehicle moves at {self.speed} km/h."


class FlyingMachine:
    def __init__(self, altitude):
        self.altitude = altitude

    def describe_flight(self):
        return f"This machine flies at an altitude of {self.altitude} meters."


class AmphibiousVehicle(Vehicle, FlyingMachine):
    def __init__(self, speed, altitude, water_speed):
        Vehicle.__init__(self, speed)
        FlyingMachine.__init__(self, altitude)
        self.water_speed = water_speed

    def describe_amphibious(self):
        return (f"On land, it moves at {self.speed} km/h; in the air, at {self.altitude} meters; "
                f"and on water, it moves at {self.water_speed} knots.")


# Пример использования
amphibious = AmphibiousVehicle(speed=100, altitude=2000, water_speed=20)
print(amphibious.describe_vehicle())
print(amphibious.describe_flight())
print(amphibious.describe_amphibious())
