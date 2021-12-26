# Load Prerequisite libraries
import logging
import sys
from parkingLot import vehicle
from parkingLot import functions
import time

# Set Log configuration with Standard Output
FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=FORMAT)


class ParkingLot:
    LOT_AVAILABLE = True

    def __init__(self, capacity=None, entry_slots=None):
        """
        Function to initialize and validate the capacity value and
        accordingly build parking lot with given capacity.
        Args:
            capacity ([Integer]): Capacity is the maximum numbers of parking lots available
            entry_slots([Integer or List]) : List of entry slots in parking lot

        Returns:
            [Integer]: returns the maximum numbers of parking lots
        """
        self._capacity = 0
        self._entry_slots = []
        self._available_slots = []
        self._occupied_slots = []
        self._timed_slots = {}
        self._vehicle_details = []

        if capacity is None:
            raise TypeError('Missing Parking Lot capacity "n" argument ')
        elif type(capacity) is not int:
            raise TypeError('Parking Lot capacity "n" should be integer ')
        if entry_slots is None:
            raise TypeError('Missing Entry slots [] argument ')

        if type(entry_slots) is not list:
            if type(entry_slots) is not int:
                raise TypeError('Entry Lot value should be integer ')
            elif entry_slots <= 0:
                raise ValueError('Value of Entry Slots must be greater than zero')
            self._entry_slots = [entry_slots]
        else:
            self._entry_slots = entry_slots

        if capacity <= 0:
            raise ValueError('Value of Parking Slots Capacity must be greater than zero')

        elif capacity > 30000:
            raise ValueError('Value of Parking Slots exceed the maximum capacity of 30000')

        if len(self._entry_slots) > capacity:
            raise ValueError('Entry Slots cannot be more than Parking Slots capacity')
        elif len(self._entry_slots) == 0:
            raise ValueError('Parking Slots cannot have 0 entry slots !')

        for entry in self._entry_slots:
            if type(entry) is not int:
                raise TypeError('Entry Lot value should be integer ')
            if entry <= 0:
                raise ValueError('Entry Slots cannot have negative or zero values !')

        self._capacity = capacity

        # Setting all slots as available
        self._available_slots = list(range(1, self._capacity + 1))
        logging.info(f"Parking Lot initialized with {self._capacity} capacity")
        logging.info(f"Entry slots are {self._entry_slots} ")

    def park(self, entry_slot, vehicle_type, registration_num, colour, make):
        """
        Function to park the vehicle into the nearest first empty parking lot found.

        Args:
            entry_slot ([Integer])
            vehicle_type ([String])
            registration_num ([String])
            colour ([String)
            make ([String])

        Returns:
            [Integer]: Returns -1 in case of no parking lot else the number allocated parking lot
        """
        if type(entry_slot) is not int:
            raise TypeError('Entry slot value should be integer ')
        elif entry_slot not in self._entry_slots:
            raise ValueError('Entry slot is not valid ')

        if len(self._occupied_slots) == self._capacity:
            ParkingLot.LOT_AVAILABLE = False
            raise ValueError('Parking Lot is full  !')
        elif ParkingLot.LOT_AVAILABLE:
            lot = self.__get_empty_slot(entry_slot, vehicle_type, registration_num, colour, make)
            if lot == -1:
                # Duplicate registration numbers
                raise ValueError('Duplicate registration numbers found !')
            elif lot == 0:
                # No more slots available
                ParkingLot.LOT_AVAILABLE = False
                return -1
            else:
                return lot
        else:
            return -1

    def un_park(self, registration_num):
        """
        Function to un park the vehicle from the parking lot
        Args:
            registration_num ([String])
        Returns:
            [Integer]: Returns -1 in case registration number is not found
        """
        if type(registration_num) is not str:
            logging.error(f'Registration number {registration_num} type invalid : Cannot Un park !')
            raise TypeError(f'Registration number with {type(registration_num)} type invalid')
        else:
            location = self._get_spot_from_registration_num(registration_num)
            if location == -1:
                logging.error(f'Registration number {registration_num} not found : Cannot Un park !')
                raise ValueError(f'Registration number with {registration_num}  not found')

            elif not ParkingLot.LOT_AVAILABLE:
                self._occupied_slots.remove(location)
                logging.info(f"Un parked {registration_num} from slot {location}")
                self._vehicle_details.remove(location)
                self._available_slots.append(location)
                upark_time = time.time()
                park_time = self._timed_slots[location]
                park_fees = get_price(upark_time-park_time)
                del self._timed_slots[location]
                self._available_slots.sort()
                ParkingLot.LOT_AVAILABLE = True
                return location
            else:
                self._occupied_slots.remove(location)
                for car in self._vehicle_details:
                    if car.get_registration_number() == registration_num:
                        spot = car.get_spot()
                        self._vehicle_details.remove(car)
                        self._available_slots.append(spot)
                        self._available_slots.sort()
                        break

                logging.info(f"Un parked {registration_num} from slot {location}")
                return location

    def search(self, registration_num=None, vehicle_type=None, colour=None, make=None):
        """
        One of search parameters is mandatory and registration_num could be a list.
        Should    search    for the slots with the vehicles which satisfies the search.

        Args:
             registration_num = None
             vehicle_type = None
             colour = None
             make = None

        Returns:
            [Integer]: Returns -1 in case of no parking lot found else the number allocated parking lot
        """
        if registration_num is not None:
            search_argument = "registration_num"
        elif vehicle_type is not None:
            search_argument = "vehicle_type"
        elif colour is not None:
            search_argument = "colour"
        elif make is not None:
            search_argument = "make"
        else:
            search_argument = None

        if search_argument == "registration_num":
            if type(registration_num) is not str:
                logging.error(f'Argument type invalid : Cannot proceed with Search !')
                raise TypeError(f'registration_num type invalid : Expected str !')
            else:
                return self._search_with_registration_num(registration_num)

        elif search_argument == "vehicle_type":
            if type(vehicle_type) is not str:
                logging.error(f'Argument type invalid : Cannot proceed with Search !')
                raise TypeError(f'vehicle_type type invalid : Expected str !')
            else:
                return self._search_with_vehicle_type(vehicle_type)

        elif search_argument == "colour":
            if type(colour) is not str:
                logging.error(f'Argument type invalid : Cannot proceed with Search !')
                raise TypeError(f'colour type invalid : Expected str !')
            else:
                return self._search_with_colour(colour)

        elif search_argument == "make":
            if type(make) is not str:
                logging.error(f'Argument type invalid : Cannot proceed with Search !')
                raise TypeError(f'make type invalid : Expected str !')
            else:
                return self._search_with_make(make)

        else:
            logging.error(f'At least one valid search parameter is mandatory !')
            raise TypeError("Missing key search argument")

    def status(self):
        """
        Function to print the parkingLot status
        Showing all the occupied slots, vehicle information and free slots.

        Returns:
            [List]: Returns -1 in case of no parking lot occupied else the list of parked vehicles
        """
        total_cars = len(self._occupied_slots)
        logging.info(f"> Total Vehicles in Parking Lot : {total_cars}")
        if total_cars > 0:
            for car in self._vehicle_details:
                logging.info(f"Vehicle: {car.get_registration_number()}, Type: {car.get_vehicle_type()}, "
                             f"Colour: {car.get_colour()}, Make {car.get_make()}  ")

            return total_cars
        else:
            return None

    def __get_empty_slot(self, entry_slot, vehicle_type, registration_num, colour, make):
        """
        Function to find the first empty parking lot.

        Returns:
            [Integer]: Parking Slot Id
        """
        if self.__is_duplicate(registration_number=registration_num):
            logging.error(f"Cannot park with duplicate registration numbers for {registration_num}")
            return -1
        if len(self._available_slots) == 0:
            logging.error(f"Parking lot is full, Cannot park more vehicles including {registration_num}")
            return 0
        spot = functions.find_nearest_lot(self._available_slots, len(self._available_slots), entry_slot)
        self._vehicle_details.append(vehicle.ParkedVehicle(registration_num, vehicle_type, colour, make, spot))
        self._available_slots.remove(spot)
        self._occupied_slots.append(spot)
        self._timed_slots[spot] = time.time()
        self._occupied_slots.sort()
        logging.info(f"Vehicle {registration_num} is parked at {spot}")
        return spot

    # Current slot 8 3 1 7 12
    #       9
    #    8     13
    #  3   12
    # 1  7
    #
    def get_distance(self, slot1, slot2):
        """
        returns distance between slots

        """




    def __is_duplicate(self, registration_number):
        """
        Function to find duplicate registration numbers
        :param registration_number:
        :return: True if duplicate found
        """
        for car in self._vehicle_details:
            if car.get_registration_number() == registration_number:
                logging.info(f"Another Vehicle with {registration_number} parked at {car.get_spot()} Lot")
                return True

        return False

    def _get_spot_from_registration_num(self, registration_number):
        """
        Search for vehicle with given registration number
        :param registration_number:
        :return: location of parked vehicle
        """

        for car in self._vehicle_details:
            if car.get_registration_number() == registration_number:
                return car.get_spot()

        return -1


    def _search_with_registration_num(self, registration_number):
        """
        Search for vehicle with given registration number
        :param registration_number:
        :return: location of parked vehicle
        """
        found = False
        if type(registration_number) is str:
            for car in self._vehicle_details:
                if car.get_registration_number() == registration_number:
                    logging.info(f"Vehicle {car.get_registration_number()} parked at Lot {car.get_spot()} , \
                     Type: {car.get_vehicle_type()}, Colour : {car.get_colour()} , Make : {car.get_make()}")
                    found = True
                    return car.get_spot()

        elif type(registration_number) is list:
            for number in registration_number:
                for car in self._vehicle_details:
                    if car.get_registration_number() == number:
                        logging.info(f"Vehicle {car.get_registration_number()} parked at Lot {car.get_spot()} , \
                        Type: {car.get_vehicle_type()}, Colour : {car.get_colour()} , Make : {car.get_make()}")
                        found = True

        if not found:
            raise ValueError(f" Vehicle not found {registration_number}")

    def _search_with_vehicle_type(self, vehicle_type):
        """
        Search for vehicle with given vehicle_type
        :param vehicle_type:
        :return: location of parked vehicle
        """
        cars = []
        found = False
        for car in self._vehicle_details:
            if car.get_vehicle_type() == vehicle_type:
                # logging.info(f"* Found Vehicle {vehicle_type} parked at {car.get_spot()} Lot")
                cars.append(car.get_registration_number())
                found = True

        self._search_with_registration_num(registration_number=cars)

        if not found:
            raise ValueError(f" Vehicle not found for {vehicle_type}")

    def _search_with_colour(self, colour):
        """
        Search for vehicle with given colour
        :param colour
        :return: location of parked vehicle
        """
        cars = []
        found = False
        for car in self._vehicle_details:
            if car.get_colour() == colour:
                # logging.info(f"* Found Vehicle {colour} parked at {car.get_spot()} Lot")
                cars.append(car.get_registration_number())
                found = True

        self._search_with_registration_num(registration_number=cars)
        if not found:
            raise ValueError(f" Vehicle not found for {colour}")

    def _search_with_make(self, make):
        """
        Search for vehicle with given make
        :param make:
        :return: location of parked vehicle
        """
        cars = []
        found = False
        for car in self._vehicle_details:
            if car.get_make() == make:
                # logging.info(f"* Found Vehicle {make} parked at {car.get_spot()} Lot")
                cars.append(car.get_registration_number())
                found = True

        self._search_with_registration_num(registration_number=cars)

        if not found:
            raise ValueError(f" Vehicle not found {vehicle_type}")