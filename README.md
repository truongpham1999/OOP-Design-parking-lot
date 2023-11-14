# OOP-Design-parking-lot
Parking lots for vehicles to park in. Vehicles can be of different sizes, e.g. motorbikes, cars, limos, trucks, etc.

- Multiple levels in the parking lot
- Possible vehicle types: car, limo, semi-truck
- We will have a payment system with a single entrance and exit
- Drivers will be assigned a parking spot after paying

## Vehicles and Parking Spots
- Vehicles can be of different sizes (motorbike = 1, car = 2, limo = 3, truck = 4)
- Each parking spot will have a size of 1
- A vehicle must fully take up each spot assigned to it (no fractional spots)
- Vehicles will automatically be assigned the next available parking spot on the lowest floor

## Payment System
- Drivers will pay for parking and be assigned the next available spot on the lowest floor
- Drivers can pay for a variable number of hours and they are charged after they remove their vehicle based on an hourly rate
- We can assume vehicles can be parked for a variable number of hours
- If there is no capacity, the system should not assign a spot and should notify the driver
