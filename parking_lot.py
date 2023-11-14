import datetime
import math

class Vehicle:
    def __init__(self, spot_size):
        self._spot_size = spot_size

    def get_spot_size(self):
        return self._spot_size

class MotorBike(Vehicle):
    def __init__(self):
        super().__init__(1)

class Car(Vehicle):
    def __init__(self):
        super().__init__(2)

class Limo(Vehicle):
    def __init__(self):
        super().__init__(3)

class Truck(Vehicle):
    def __init__(self):
        super().__init__(4)

class Driver:
    def __init__(self, id, vehicle):
        self._id = id
        self._vehicle = vehicle
        self._payment_due = 0

    def get_vehicle(self):
        return self._vehicle

    def get_id(self):
        return self._id

    def get_charge(self, amount):
        self._payment_due += amount

class ParkingFloor:
    def __init__(self, spot_count):
        self._spots = [0] * spot_count
        self._vehicle_map = {}

    def park_vehicle(self, vehicle):
        size = vehicle.get_spot_size()
        left, right = 0, 0

        while right < len(self._spots):
            if self._spots[right] != 0:
                left = right + 1
            # found enought spots for vehicle
            if right - left + 1 == size:
                for index in range(left, right + 1):
                    self._spots[index] = 1
                self._vehicle_map[vehicle] = [left, right]
                return True
            right += 1

        return False

    def remove_vehicle(self, vehicle):
        if vehicle not in self._vehicle_map:
            return False

        start, end = self._vehicle_map[vehicle]
        for index in range(start, end + 1):
            self._spots[index] = 0
        del self._vehicle_map[vehicle]
        return True

    def get_parking_spots(self):
        return self._spots

    def get_vehicle_spots(self, vehicle):
        return self._vehicle_map.get(vehicle)

class ParkingGarage:
    def __init__(self, floor_count, spots_per_floor):
        self._parking_floors = [ParkingFloor(spots_per_floor) for _ in range(floor_count)]

    def park_vehicle(self, vehicle):
        for floor in self._parking_floors:
            if floor.park_vehicle(vehicle):
                return True
        return False

    def remove_vehicle(self, vehicle):
        for floor in self._parking_floors:
            if floor.remove_vehicle(vehicle):
                return True
        return False

class ParkingSystem:
    def __init__(self, parkingGarage, hourlyRate):
        self._parkingGarage = parkingGarage
        self._hourlyRate = hourlyRate
        self._timeParked = {}    # map driverID to time that they parked

    def park_vehicle(self, driver):
        currentHour = datetime.datetime.now().hour
        isParked = self._parkingGarage.park_vehicle(driver.get_vehicle())
        if isParked:
            self._timeParked[driver.get_id()] = currentHour
        return isParked

    def remove_vehicle(self, driver):
        if driver.get_id() not in self._timeParked:
            return False
        currentTime = datetime.datetime.now().hour
        timeParked = math.ceil(currentTime - self._timeParked[driver.get_id()])
        driver.get_charge(timeParked * self._hourlyRate)

        del self._timeParked[driver.get_id()]
        return self._parkingGarage.remove_vehicle(driver.get_vehicle())


parkingGarage = ParkingGarage(2, 5)
parkingSystem = ParkingSystem(parkingGarage, 5)

driverMotor = Driver(1, MotorBike())
driverCar = Driver(2, Car())
driverTruck_1 = Driver(8, Truck())
driverTruck_2 = Driver(6, Truck())

print(parkingSystem.park_vehicle(driverTruck_1))    # true
print(parkingSystem.park_vehicle(driverCar))        # true
print(parkingSystem.park_vehicle(driverMotor))      # true
print(parkingSystem.park_vehicle(driverTruck_2))    # false

print(parkingSystem.remove_vehicle(driverTruck_1))  # true
print(parkingSystem.remove_vehicle(driverCar))      # true
print(parkingSystem.remove_vehicle(driverTruck_2))  # false



