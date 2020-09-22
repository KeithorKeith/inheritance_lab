from vehicle import *

class Motorbike(Vehicle):

    def __init__(self):
        super().__init__(2)

    def start(self):
        vehicle_start = Vehicle.start(self)
        return f"{vehicle_start} (I'm a motorbike), HELL YEAH!"