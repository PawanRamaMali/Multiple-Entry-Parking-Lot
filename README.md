# Parking-Lot-Demo

Design a parking lot that can hold up to `N` cars at any given point in time. 

## Problem Description

This code represents a basic design of parking lot. It creates parking lot with given number of slots. 
The cars entering the parking lot will always get the first empty slot in the parking lot. This slots becomes available when the customer leaves the parking lot. 
The interaction with the code is with file-based input system i.e. it should accept a filename as an input. 


## Code Dependencies

Python 3 is required to run this code.

## Setup

Follow these steps -

1. Clone the repository. `git clone https://github.com/PawanRamaMali/Parking-Lot-Demo` 

2. Run `python Run_Parking.py -f input.txt` using terminal.

## Directory Structure

```
Parking-Lot_Demo
|
|── Run_Parking.py
|── Parking_Argument.py
|── Vehicle.py
|── input.txt
└── README.md
    
```
## Description of commands in the Input file

##### 1 `create_parking_lot <N>` - To create parking lot with N parking slots .

##### 2 `exit` - To exit the parking lot system.

##### 3 `leave <n>` - To empty a parking spot in the parking lot passed slot number.

##### 4 `park <Vehicle_Number> driver_age <Age>` - To park a vehicle in the parking lot with passed Vehicle Number and Driver's Age.

##### 5 `slot_numbers_for_driver_of_age` - Gives the slot numbers with drivers of passed age argument.

##### 6 `slot_number_for_car_with_number <Vehicle_Number>` - Gives the slot number with vehicle with passed registration number.

##### 7 `vehicle_registration_number_for_driver_of_age <Age>` - Gives the vehicle registration numbers with the given driver's age


### Sample 1 Input 

```
Create_parking_lot 6
Park KA-01-HH-1234 driver_age 21
Park PB-01-HH-1234 driver_age 21
Slot_numbers_for_driver_of_age 21
Park PB-01-TG-2341 driver_age 40
Slot_number_for_car_with_number PB-01-HH-1234
Leave 2
Park HR-29-TG-3098 driver_age 39
Vehicle_registration_number_for_driver_of_age 18
```

### Sample 1 Output

```
 Created parking of 6 slots
 Car with vehicle registration number "KA-01-HH-1234" has been parked at slot number 1
 Car with vehicle registration number "PB-01-HH-1234" has been parked at slot number 2
 1, 2
 Car with vehicle registration number "PB-01-TG-2341" has been parked at slot number 3
 2
 Slot number 2 vacated, the car with vehicle registration number PB-01-HH-1234 has left the space, the driver of the car was of age 21
 Car with vehicle registration number "HR-29-TG-3098" has been parked at slot number 2
 
```
