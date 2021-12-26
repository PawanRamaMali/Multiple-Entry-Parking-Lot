import unittest
import logging
from parkingLot import parking


class TestParkingInitialization(unittest.TestCase):
    """
    Testing Parking Lot Initialization
    """

    def test_parking_no_capacity_arg(self):
        logging.info(f"Test Case 01")
        self.assertRaises(TypeError, parking.ParkingLot, entryslots=[3, 10, 7])

    def test_parking_capacity_type(self):
        logging.info(f"Test Case 02")
        self.assertRaises(TypeError, parking.ParkingLot, "10", [3, 10, 7])

    def test_parking_entry_slot_type(self):
        logging.info(f"Test Case 03")
        self.assertRaises(TypeError, parking.ParkingLot, 10, "5")
        self.assertRaises(TypeError, parking.ParkingLot, 10, ["5"])

    def test_parking_no_entry_slots_arg(self):
        logging.info(f"Test Case 04")
        self.assertRaises(TypeError, parking.ParkingLot, capacity=20)

    def test_parking_no_capacity(self):
        logging.info(f"Test Case 05")
        self.assertRaises(ValueError, parking.ParkingLot, -10, [3, 10, 7])
        self.assertRaises(ValueError, parking.ParkingLot, 0, [3, 10, 7])

    def test_parking_over_capacity(self):
        logging.info(f"Test Case 06")
        self.assertRaises(ValueError, parking.ParkingLot, 32000, [3, 10, 7])

    def test_parking_no_entry_slots(self):
        logging.info(f"Test Case 07")
        self.assertRaises(ValueError, parking.ParkingLot, 120, [])

    def test_parking_negative_entry_slot(self):
        logging.info(f"Test Case 08")
        self.assertRaises(ValueError, parking.ParkingLot, 120, -5)
        self.assertRaises(ValueError, parking.ParkingLot, 120, 0)

    def test_parking_negative_entry_slots_in_list(self):
        logging.info(f"Test Case 09")
        self.assertRaises(ValueError, parking.ParkingLot, 120, [-10, 5, 10])
        self.assertRaises(ValueError, parking.ParkingLot, 120, [0, 5, 10])

    def test_parking_exceed_entry_slots(self):
        logging.info(f"Test Case 10")
        self.assertRaises(ValueError, parking.ParkingLot, 120, [i for i in range(121)])


class TestParking(unittest.TestCase):
    """
    Testing Parking Lot Parking functionality
    """

    def test_valid_entry_slot_type(self):
        logging.info(f"Test Case 11")
        parking_lot = parking.ParkingLot(10, [5, 7])
        self.assertRaises(TypeError, parking_lot.park, "5", "Bus", "KA-01-HH-1234", "Red", "Tesla")

    def test_valid_entry_slot_value(self):
        logging.info(f"Test Case 12")
        parking_lot = parking.ParkingLot(10, [5, 7])
        self.assertRaises(ValueError, parking_lot.park, 6, "Bus", "KA-01-HH-1234", "Red", "Tesla")

    def test_valid_entry_slot_args(self):
        logging.info(f"Test Case 13")
        parking_lot = parking.ParkingLot(10, [5, 7])
        self.assertRaises(ValueError, parking_lot.park, 6, "Bus", "KA-01-HH-1234", "Red", "Tesla")

    def test_with_duplicate_registration_number(self):
        logging.info(f"Test Case 14")
        parking_lot = parking.ParkingLot(20, [1, 5, 7])
        parking_lot.park(5, "Bus", "KA-01-HH-1234", "Red", "Tesla")
        parking_lot.park(5, "Bus", "KA-01-HH-1235", "Red", "Tesla")
        self.assertRaises(ValueError, parking_lot.park, 5, "Bus", "KA-01-HH-1234", "Blue", "Honda")

    def test_with_parking_lot_full(self):
        logging.info(f"Test Case 15")
        parking_lot = parking.ParkingLot(2, [1, 2])
        parking_lot.park(1, "Bus", "KA-01-HH-1234", "Red", "Tesla")
        parking_lot.park(1, "Bus", "KA-01-HH-1235", "Red", "Tesla")
        self.assertRaises(ValueError, parking_lot.park, 1, "Bus", "KA-01-HH-1236", "Blue", "Honda")


class TestUnParking(unittest.TestCase):
    """
    Testing Un parking functionality
    """

    def test_valid_registration_number_type(self):
        logging.info(f"Test Case 16")
        parking_lot = parking.ParkingLot(10, [5, 7])
        parking_lot.park(5, "Bus", "KA-01-HH-1234", "Red", "Tesla")
        parking_lot.park(5, "Bus", "KA-01-HH-1235", "Red", "Tesla")
        self.assertRaises(TypeError, parking_lot.un_park, 1234)

    def test_registration_number_not_found(self):
        logging.info(f"Test Case 17")
        parking_lot = parking.ParkingLot(10, [5, 7])
        parking_lot.park(5, "Bus", "KA-01-HH-1234", "Red", "Tesla")
        parking_lot.park(5, "Bus", "KA-01-HH-1235", "Red", "Tesla")
        self.assertRaises(ValueError, parking_lot.un_park, "KA-01-HH-1230")


class TestParkingSearch(unittest.TestCase):
    """
    Testing Parking search functionality
    """

    def test_invalid_registration_number_type(self):
        logging.info(f"Test Case 18")
        parking_lot = parking.ParkingLot(10, [5, 7])
        parking_lot.park(5, "Bus", "KA-01-HH-1234", "Red", "Tesla")
        parking_lot.park(5, "Bus", "KA-01-HH-1235", "Red", "Tesla")
        self.assertRaises(TypeError, parking_lot.search, registration_num=5123)

    def test_registration_number_not_found(self):
        logging.info(f"Test Case 19")
        parking_lot = parking.ParkingLot(15, [5, 7, 10])
        parking_lot.park(5, "Bus", "KA-01-HH-1234", "Red", "Tesla")
        parking_lot.park(7, "Bus", "KA-01-HH-1235", "Red", "Tesla")
        self.assertRaises(ValueError, parking_lot.search, registration_num="KA-01-HH-1230")

    def test_no_search_parameter(self):
        logging.info(f"Test Case 20")
        parking_lot = parking.ParkingLot(15, [5, 7, 10])
        parking_lot.park(5, "Bus", "KA-01-HH-1234", "Red", "Tesla")
        parking_lot.park(7, "Bus", "KA-01-HH-1235", "Red", "Tesla")
        self.assertRaises(TypeError, parking_lot.search, not_defined=True)

    def test_invalid_vehicle_type_not_found(self):
        logging.info(f"Test Case 21")
        parking_lot = parking.ParkingLot(15, [5, 7, 10])
        parking_lot.park(5, "Bus", "KA-01-HH-1234", "Red", "Tesla")
        parking_lot.park(7, "Bus", "KA-01-HH-1235", "Red", "Tesla")
        self.assertRaises(TypeError, parking_lot.search, vehicle_type=456)

    def test_colour_type_not_found(self):
        logging.info(f"Test Case 22")
        parking_lot = parking.ParkingLot(15, [5, 7, 10])
        parking_lot.park(5, "Bus", "KA-01-HH-1234", "Red", "Tesla")
        parking_lot.park(7, "Bus", "KA-01-HH-1235", "Red", "Tesla")
        self.assertRaises(TypeError, parking_lot.search, colour=456)

    def test_make_type_not_found(self):
        logging.info(f"Test Case 23")
        parking_lot = parking.ParkingLot(15, [5, 7, 10])
        parking_lot.park(5, "Bus", "KA-01-HH-1234", "Red", "Tesla")
        parking_lot.park(7, "Bus", "KA-01-HH-1235", "Red", "Tesla")
        self.assertRaises(TypeError, parking_lot.search, make=456)

    def test_vehicle_type_not_found(self):
        logging.info(f"Test Case 24")
        parking_lot = parking.ParkingLot(15, [5, 7, 10])
        parking_lot.park(5, "Bus", "KA-01-HH-1234", "Red", "Tesla")
        parking_lot.park(7, "Bus", "KA-01-HH-1235", "Red", "Tesla")
        self.assertRaises(ValueError, parking_lot.search, vehicle_type="car")

    def test_vehicle_colour_not_found(self):
        logging.info(f"Test Case 25")
        parking_lot = parking.ParkingLot(15, [5, 7, 10])
        parking_lot.park(5, "Bus", "KA-01-HH-1234", "Red", "Tesla")
        parking_lot.park(7, "Bus", "KA-01-HH-1235", "Red", "Tesla")
        self.assertRaises(ValueError, parking_lot.search, colour="Orange")

    def test_vehicle_make_not_found(self):
        logging.info(f"Test Case 26")
        parking_lot = parking.ParkingLot(15, [5, 7, 10])
        parking_lot.park(5, "Bus", "KA-01-HH-1234", "Red", "Tesla")
        parking_lot.park(7, "Bus", "KA-01-HH-1235", "Red", "Tesla")
        self.assertRaises(ValueError, parking_lot.search, make="BMW")


if __name__ == '__main__':
    unittest.main()
