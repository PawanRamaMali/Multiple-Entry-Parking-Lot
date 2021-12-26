from enum import Enum

class Parking_Argument(Enum):
    CREATE_PARKING_LOT = 1
    EXIT = 2
    LEAVE = 3
    PARK = 4
    SLOT_NUMBER_FOR_CAR_WITH_NUMBER = 5
    SLOT_NUMBERS_FOR_DRIVER_OF_AGE = 6
    VEHICLE_REGISTRATION_NUMBER_FOR_DRIVE_OF_AGE = 7
  
# 1 = `create_parking_lot` - Used for creating the parking lot system.

# 2 = `exit` - Used for closing the system.

# 3 = `leave` - Used to empty a parking spot in the parking lot.

# 4 = `park` - Used to park a vehicle in the parking lot.

# 5 = `slot_numbers_for_driver_of_age` - Gives the slot numbers with drivers of passed age.

# 6 = `slot_number_for_car_with_number` - Gives the slot number with vehicle with passed registration number.

# 7 = `vehicle_registration_number_for_driver_of_age` - Gives the vehicle registration numbers with the given driver's age


PARKING_ARGUMENTS_LIST = {
    'create_parking_lot': Parking_Argument.CREATE_PARKING_LOT,
    'exit': Parking_Argument.EXIT,
    'leave': Parking_Argument.LEAVE,
    'park': Parking_Argument.PARK,
    'slot_numbers_for_driver_of_age': Parking_Argument.SLOT_NUMBERS_FOR_DRIVER_OF_AGE,
    'slot_number_for_car_with_number': Parking_Argument.SLOT_NUMBER_FOR_CAR_WITH_NUMBER,
    'vehicle_registration_number_for_driver_of_age': Parking_Argument.VEHICLE_REGISTRATION_NUMBER_FOR_DRIVE_OF_AGE,
    
}
