from vehicle import *

class Car(Vehicle):

    def __init__(self, model):
        self.model = model
        super().__init__(4)

    def get_model(self):
        return self.model
    

