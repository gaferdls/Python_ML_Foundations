
# ----- Parent Class: Vehicle -----
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False # A common attribute for all vehicles

    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            return f"The {self.make} {self.model}'s engine started."
        else:
            return f"The {self.make} {self.model}'s engine is already running."

    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            return f"The {self.make} {self.model}'s engine stopped."
        else:
            return f"The {self.make} {self.model}'s engine is already off."

    def get_vehicle_info(self):
        return f"{self.year} {self.make} {self.model}"

# ----- Child Class: Car (inherits from Vehicle) -----
class Car(Vehicle):
    def __init__(self, make, model, year, color, mileage, train_type):
        # Call the constructor of the parent class (Vehicle)
        # to initialize attributes common to all vehicles
        super().__init__(make, model, year)

        # Initializes attributes specific to a Car
        self.color = color
        self.mileage = mileage
        self.train_type = train_type

    def honk(self):
        return "Honk! Honk!"

    def accelerate(self, distance):
        self.mileage += distance
        return f"Accelerating ... Current mileage: {self.mileage}"

    def get_vehicle_info(self):
        parent_info = super().get_vehicle_info()
        return f"{parent_info} ({self.color}), {self.train_type}wd, Mileage: {self.mileage}"


# ----- Create Objects ------

my_car = Car("Toyota", "Camry", 2022, "Silver", 25000.0, 4)
rental_car = Car("Ford", "Mustang", 2022, "Blue", 10000.0, 2)

print(my_car.get_vehicle_info())
print(my_car.start_engine())
print(my_car.is_running)
print(my_car.accelerate(500.0))
print(my_car.stop_engine())

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, color, mileage, type):
        super().__init__(make, model, year)
        self.color = color
        self.mileage = mileage
        self.type = type

    def honk(self):
        return "Honk! Honk!"

    def accelerate(self, distance):
        self.mileage += distance
        return f"Accelerating ... Current mileage: {self.mileage}"

    def get_vehicle_info(self):
        parent_info = super().get_vehicle_info()
        return f"{parent_info} ({self.color}), {self.type}, {self.mileage}"


my_bike = Motorcycle("Ducati", "Diavel", 2024, "red", 1500, "sport")
print(my_bike.get_vehicle_info())
print(my_bike.honk())
print(my_bike.accelerate(500))
