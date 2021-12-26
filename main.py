from parkingLot import parking


def main():
    """
    Create and Test Parking Lot
    """
    parking_lot = parking.ParkingLot(20, [3, 10, 7])

    parking_lot.park(10, "Bus", "KA-01-HH-1234", "Red", "Tesla")
    parking_lot.park(10, "Bus", "KA-01-HH-1235", "Red", "Tesla")
    parking_lot.park(10, "Bus", "KA-01-HH-1236", "Red", "Tesla")
    parking_lot.un_park("KA-01-HH-1235")
    parking_lot.park(10, "Bus", "KA-01-HH-1235", "Red", "Tesla")
    parking_lot.status()


if __name__ == '__main__':
    main()
