class Parked_Vehicle:
    """
    Class for Parked Vehicle specifications
    """
    def __init__(self, registration_number, driver_age):
        self.driver_age = driver_age
        self.registration_number = registration_number


class Car(Parked_Vehicle):
    """
    Class for Parked Vehicle with function to initialize & return Car Object
    """
    def __init__(self, registration_number, driver_age):
        Parked_Vehicle.__init__(self, registration_number, driver_age)

    def getType(self):
        """
        To return Car Object
        """
        return "Car"
