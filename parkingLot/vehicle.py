
class ParkedVehicle:
    """
    Class for Parked Vehicle specifications
    Each vehicle is uniquely identified by its registration number
    Vehicle also has other additional properties like colour, make
    """
    def __init__(self, registration_number, vehicle_type, colour, make, spot):
        self.registration_number = registration_number
        self.vehicle_type = vehicle_type
        self.colour = colour
        self.make = make
        self.spot = spot

    def get_registration_number(self):
        """
        To return registration_number
        """
        return self.registration_number

    def get_vehicle_type(self):
        """
        To return Vehicle Type
        """
        return self.vehicle_type

    def get_colour(self):
        """
        To return colour
        """
        return self.colour

    def get_make(self):
        """
        To return make
        """
        return self.make

    def get_spot(self):
        """
        To return vehicle spot
        """
        return self.spot
