# Multiple Entry Parking Lot 

Design a multiple entry parking lot and implement the solution in an object-oriented programming language 

## Problem Description

###      Multiple Entry Parking Lot: Design parking lot system with below features
* Contains 'n' parking slots in a linear manner with some of these slots designated as entries. Both 'n' & 'entrySlots' are provided during the parking lot initialisation.
* Once initialised, the parking lot can hold 'n' different vehicles at any given time with one vehicle in each slot.
* Currently, there are different types of vehicles like a Truck, Car, Bus which comes to the Parking Lot. Each slot in the Parking Lot can accommodate any type of vehicle. 
* Each vehicle is uniquely identified by its registration number however it has other additional properties like colour, make..etc. 
* Once the system is initialised with input size 'n' & 'entrySlots', it should support a series of the following operations in an interactive mode (commands on command line/commands through input file).

###     Operations:
* park (entrySlot, vehicleType, registrationNo, colour, make) - should assign the nearest free slot from the entry. When there are multiple slots with the same distance, parking in any of them is accepted.
* unpark (registrationNo)
* status - should print the parkingLot status showing all the occupied slots (and the vehicle information) and free slots.
* search [vehicleType] [registrationNos] [colour] [make] - Only one of search parameters is mandatory. registrationNos could be a list. Should search for the slots with the vehicles which satisfies the search.
* Example: Let's say there is a parking lot with 100 slots and slots 1,10,20...100 designated as entry slots.
       * Now when a vehicle comes in through slot-10, it needs to be parked at 10.
       * Another vehicle comes in through slot-10, it can be parked either at 9 or 11 (any slot is fine).
       * Third vehicles coming in through slot-10 need to be parked at 9 or 11 depending on the above.
       * Let's say another vehicle comes in through slot-10 after a long time (by which slots 1-80 are all filled out), this vehicle needs to be parked at 81. 
       * So on..


## Code Dependencies

Python 3

## Directory Structure

```
MultipleEntryParkingLot
|
|── main.py
|── /parkingLot
|── ── vehicle.py
|── ── functions.py
|── ── parking.py
|── ── __init__.py

```
## To run the Unit Test Cases  

```
python test_parking_lot.py

```

## To run the Code in Linux 

```
python main.py
```

# Methodology Used
* Bottom Up Design using Object Oriented Programming

