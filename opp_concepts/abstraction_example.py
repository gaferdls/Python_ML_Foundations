from abc import ABC, abstractmethod

# --- Abstract Base Class: Vehicle ---
# A vehicle itself cannot be directly instantiated; it's a concept.
class Vehicle(ABC):
    def __init__(self, make, mode, year):
        self.make = make
        self.mode = mode
        self.year = year
        self._is_running = False

    #Abstract methods - subclasses MUST implement these
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def describe_movement(self):
        pass

    def get_vehicle_info(self):
        return f"{self.year} {self.make} {self.mode}"

# --- Concrete Child Class: Car ---
# Car *must* implement all abstract methods from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, year, color, mileage, num_doors):
        super().__init__(make, model, year)
        self.color = color
        self.mileage = mileage
        self.num_doors = num_doors

    #Implementation of abstract methods form Vehicle
    def start_engine(self):
        if not self._is_running:
            self._is_running = True
            return f"The {self.make} {self.mode}'s engine rumbles to life!"
        else:
            return f"The {self.make} {self.mode}'s engine is already running."

    def stop_engine(self):
        if self._is_running:
            self._is_running = False
            return f"The {self.make} {self.mode}'s engine quietly turns off."
        else:
            return f"The {self.make} {self.mode}'s engine is already off."

    def describe_movement(self):
        return "The car drives smoothly on asphalt."

    def honk(self):
        return "Beep beep!"

    def accelerate(self, distance):
        self.mileage += distance
        return f"Accelerating... Current mileage: {self.mileage}"

    def get_car_details(self):
        parent_info = super().get_vehicle_info()
        return f"{parent_info} ({self.color}, Doors: {self.num_doors}, Mileage: {self.mileage})"

# --- Concrete Child Class: Motorcycle ---
# Motorcycle *must* implement all abstract methods form Vehicle

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar, engine_size_cc):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar
        self.engine_size_cc = engine_size_cc

    # Implementation of abstract methods from Vehicle
    def start_engine(self):
        if not self._is_running:
            self._is_running = True
            return f"The {self.make} {self.mode}'s engine roars to life!"
        else:
            return f"The {self.make} {self.mode}'s engine is already running."

    def stop_engine(self):
        if self._is_running:
            self.is_running = False
            return f"The {self.make} {self.mode}'s engine sputters and dies."
        else:
            return f"The {self.make} {self.mode}'s engine is already off."

    def describe_movement(self):
        return "The motorcycle zips agilely through traffic."

    # Motorcycle-specific method
    def wheelie(self):
        return "Vroom! Pooping a wheelie!"

    def get_motorcycle_details(self):
        parent_info = super().get_vehicle_info()
        sidecar_info = "with a sidecar" if self.has_sidecar else "without a sidecar"
        return f"{parent_info} (Engine: {self.engine_size_cc}cc, {sidecar_info})"


# --- Demonstrating Abstraction and Polymorphism

# You CANNOT instantiate an abstract class directly !
# Uncomment the  line below to see an error:
# generic_vehicle = Vehicle("Generic", "Model", 2020) # TypeError: Can't instantiate abstract class Vehicle

my_car = Car("Honda", "Civic", 2024, "Blue", 500.0, 4)
my_motorcycle = Motorcycle("Kawasaki", "Ninja", 2023, False, 600)
vehicles = [my_car, my_motorcycle] #Notice we can still put them in a list!

print("--- Abstraction & Polymorphism in Action ---")
for vehicle in vehicles:
    print( f"\nProcessing: {vehicle.get_vehicle_info()}")
    print(vehicle.start_engine()) # Each Implements differently
    print(vehicle.describe_movement()) # Each implements differently
    # Call specific methods if you know the type (or use isinstance())
    if isinstance(vehicle, Car):
        print(vehicle.honk())
    elif isinstance(vehicle, Motorcycle):
        print(vehicle.wheelie())
    print(vehicle.stop_engine())