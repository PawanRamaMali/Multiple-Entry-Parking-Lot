# Load Prerequisite libraries
import argparse
from collections import defaultdict
import logging
import os
import sys

# Import functions from Parking_Argument.py & Vehicle.py
from Parking_Argument import *
import Vehicle

# Set Log configuration with Standard Output
FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=FORMAT)


class ParkingLot:
    EMPTY_SLOT = -1

    def __init__(self):
        """
        Constructor defaults set to Zero 
        """
        self._capacity = 0
        self.slotId = 0
        self.numOfOccupiedSlots = 0

    def create_Parking_Lot(self, capacity):
        """
        Function to initialize and validate the capacity value and 
        accordingly build parking lot with given capacity. 
        Args:
            capacity ([Integer]): Capacity is the maximum numbers of parking lots

        Returns:
            [Integer]: returns the maximum numbers of parking lots
        """
        if capacity <= 0:
            logging.error('Value of Parking Slots must be greater than zero')
            return None
        elif capacity > 1000:
            logging.error('Parking Slots exceed the maximum allowed capacity of 1000')
        else:
            self.slots = [ParkingLot.EMPTY_SLOT] * capacity
            self._capacity = capacity
            self.ageSlotMap = defaultdict(list)
            return self._capacity

    def _get_Empty_Slot(self):
        """
        Function to find the first empty parking lot.

        Returns:
            [Integer]: Parking Slot Id
        """
        for index in range(len(self.slots)):
            if self.slots[index] == ParkingLot.EMPTY_SLOT:
                return index

    def _isDuplicate(self, registration_number):
        """
        Function to find duplicate registration numbers 

        Args:
            registration_number ([String]): Registration Number of the vehicle
        """
        vehicle_found = [
            slot for slot in self.slots
            if slot != ParkingLot.EMPTY_SLOT
            and slot.registration_number == registration_number
        ]
        isDuplicate = True if len(vehicle_found) > 0 else False
        if isDuplicate:
            logging.info(
                f'Registration Number "{registration_number}" already exists, Kindly re-check.'
            )
        return isDuplicate

    def park(self, registration_number, driver_age):
        """
        Function to park the vehicle into the first empty parking lot found.

        Args:
            registration_number ([String]): Registration Number of the vehicle
            driver_age ([Integer]): Driver's age

        Returns:
            [Intger]: Returns -1 in case of no parking lot else the number allocated parking lot
        """
        if self.numOfOccupiedSlots < self._capacity and not self._isDuplicate(registration_number):
            slotId = self._get_Empty_Slot()
            self.slots[slotId] = Vehicle.Car(registration_number, driver_age)
            self.ageSlotMap[driver_age].append(slotId)
            self.slotId = self.slotId + 1
            self.numOfOccupiedSlots = self.numOfOccupiedSlots + 1
            return slotId + 1
        else:
            return -1

    def leave(self, slotId):
        """
        Function to clear slot of a parking lot. 

        Args:
            slotId ([Integer]): Parking Slot number to be emptied

        Returns:
            [Vehicle]: Returns None if the parking slot is already empty else vehicle
        """
        if self.numOfOccupiedSlots > 0 and self.slots[slotId - 1] != -1:
            vehicle = self.slots[slotId - 1]
            self.ageSlotMap[vehicle.driver_age].remove(slotId - 1)
            self.slots[slotId - 1] = -1
            self.numOfOccupiedSlots = self.numOfOccupiedSlots - 1
            return vehicle
        return None

    def get_Slot_From_Registration_Number(self, registration_number):
        """
        Function to get the slot number if the vehicle with the registration number 
        if Vehicle exists in the parking lot else -1.

        Args:
            registration_number ([String]): Registration Number of the vehicle

        Returns:
            [Integer]: Slot Id if Vehicle is found else -1
        """

        for index in range(len(self.slots)):
            slot = self.slots[index]
            if slot.registration_number == registration_number:
                return index + 1
        return -1

    def get_Slots_From_Drivers_Age(self, driver_age):
        """
        Function to get the slot numbers with the driver's age

        Args:
            driver_age ([Integer]): Driver's age

        Returns:
            [Integer]: Number of slots
        """
        return [str(slot + 1) for slot in self.ageSlotMap[driver_age]]

    def run_Parking_Lot(self, commandLine):
        """
        Function for running the parking lot. 
        Identify the user command and act accordingly.
        Args:
            commandLine ([String]): Parking Lot Command
        """
        
        # Split the line to identify commands
        command = commandLine.split(' ')[0].lower()

        # Error Message if command not found 
        if command not in PARKING_ARGUMENTS_LIST:
            logging.error('[Sorry] Unable to identify command : '+ str(command))
        
        elif PARKING_ARGUMENTS_LIST[command] == Parking_Argument.CREATE_PARKING_LOT:
            numOfSlots = int(commandLine.split(' ')[1])
            capacity = self.create_Parking_Lot(numOfSlots)
            if capacity:
                logging.info('Created parking of ' + str(capacity) + ' slots')
            else:
                logging.info('[Sorry] Unable to create a parking lot for capacity '+ str(capacity))
                sys.exit(-1)

        elif PARKING_ARGUMENTS_LIST[command] == Parking_Argument.PARK:
            registration_number = commandLine.split(' ')[1]
            driver_age = int(commandLine.split(' ')[3])
            allocated_parking_spot = self.park(registration_number, driver_age)
            if allocated_parking_spot == ParkingLot.EMPTY_SLOT:
                logging.info("Parking lot has reached maximum capacity ! ")
            else:
                logging.info('Car with vehicle registration number "{0}" has been parked at slot number {1}'.format(
                    registration_number, allocated_parking_spot
                ))

        elif PARKING_ARGUMENTS_LIST[command] == Parking_Argument.LEAVE:
            vacated_slot_id = int(commandLine.split(' ')[1])
            vehicle = self.leave(vacated_slot_id)
            if vehicle:
                logging.info('Slot number {0} vacated, the car with vehicle registration number {1} has left the space, the driver of the car was of age {2}'.format(
                    vacated_slot_id, vehicle.registration_number, vehicle.driver_age))

        elif PARKING_ARGUMENTS_LIST[command] == Parking_Argument.SLOT_NUMBERS_FOR_DRIVER_OF_AGE:
            driver_age = int(commandLine.split(' ')[1])
            slotIds = self.get_Slots_From_Drivers_Age(driver_age)
            logging.info(', '.join(slotIds))

        elif PARKING_ARGUMENTS_LIST[command] == Parking_Argument.SLOT_NUMBER_FOR_CAR_WITH_NUMBER:
            registration_number = commandLine.split(' ')[1]
            slotId = self.get_Slot_From_Registration_Number(registration_number)
            logging.info(slotId)

        elif PARKING_ARGUMENTS_LIST[command] == Parking_Argument.VEHICLE_REGISTRATION_NUMBER_FOR_DRIVE_OF_AGE:
            driver_age = int(commandLine.split(' ')[1])
            slotIds = [
                int(index) - 1 for index in self.get_Slots_From_Drivers_Age(driver_age)]
            slots = [self.slots[index]
                     for index in range(len(self.slots)) if index in slotIds]
            vehicle_numbers = [vehicle.registration_number for vehicle in slots]
            logging.info(', '.join(vehicle_numbers))
        
        else:
            exit(0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', required=True,
                        dest='input_file', help="Input File")
    args = parser.parse_args()

    if args.input_file:
        parkinglot = ParkingLot()
        logging.debug('Reading Input File.')
        with open(args.input_file) as f:
            # TODO: add validations in file to ensure the correctness of the commands
            for line in f:
                line = line.rstrip('\n')
                parkinglot.run_Parking_Lot(line)
    else:
        logging.error('Please pass an input file. example, python Run_Parking.py -f INPUT_FILE')


if __name__ == '__main__':
    main()
