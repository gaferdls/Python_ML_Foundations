
# ----- Parent Class: Vehicle -----
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

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

    def describe_movement(self):
        return "This vehicle moves on wheels"


# ----- Child Class: Car (inherits from Vehicle) -----
class Car(Vehicle):
    def __init__(self, make, model, year, color, mileage, train_type):
        super().__init__(make, model, year)
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

    def describe_movement(self):
        return "The car drives smoothly on roads"


# ----- Child Class: Motorcycle (inherits from Vehicle) -----
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar, engine_size_cc):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar
        self.engine_size_cc = engine_size_cc

    def wheelie(self):
        return "Vroom! Popping a wheelie!"

    def get_vehicle_info(self):
        parent_info = super().get_vehicle_info()
        sidecar_info = "with a sidecar" if self.has_sidecar else "without a sidecar"
        return f"{parent_info} (Engine: {self.engine_size_cc}cc, {sidecar_info})"

    def describe_movement(self):
        return "The motorbike zips through traffic."

my_car = Car("Toyota", "Camry", 2022, "Silver", 25000.0, 4)
my_motorcycle = Motorcycle("Harley-Devidson", "Fat Bob", 2023, False, 1868)
an_old_truck = Vehicle("Ford", "F-100", 1970)

vehicles = [my_car, my_motorcycle, an_old_truck]

print("--- Polymorphism ---")
for vehicle in vehicles:
    print(f"\nProcessing a {vehicle.make} {vehicle.model}.")
    print(vehicle.get_vehicle_info())
    print(vehicle.start_engine())
    print(vehicle.describe_movement())
    print(vehicle.stop_engine())

