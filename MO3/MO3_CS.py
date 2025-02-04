# Graftin Gubocki
# MO3_CS.py
# Program collects user input for different vehicle properties and creates an automobile object using the users inputs

# Vehicle class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Automobile class, inheriting from Vehicle
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        Vehicle.__init__(self, "car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Collect users car details
print("Enter your cars information:")
year = input("Year: ")
make = input("Make: ")
model = input("Model: ")
doors = input("Number of doors (2 or 4): ")
roof = input("Type of roof (standard or sun roof): ")

# Create an Automobile object using the users input
car = Automobile(year, make, model, doors, roof)

# Print the cars info
print("\nCar Information:")
print("Vehicle type:", car.vehicle_type)
print("Year:", car.year)
print("Make:", car.make)
print("Model:", car.model)
print("Number of doors:", car.doors)
print("Type of roof:", car.roof)
