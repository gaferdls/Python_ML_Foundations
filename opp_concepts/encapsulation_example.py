class Car:
    def __init__(self, make, model, year, color, initial_mileage=0.0):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        # Treat mileage as a "protected" attribute (convention)
        # It means: please don't modify this directly from outside
        self._mileage = initial_mileage
        # A truly "private" attribute (name mangled)
        self.__engine_status = "off"

    # Public method to get mileage (the controlled interface)
    def get_mileage(self):
        return self._mileage

    # Public method to drive, which updates mileage (the controlled operation)
    def drive(self, distance):
        if distance > 0:
            self._mileage += distance
            print(f"Drove {distance} miles. Current mileage: {self._mileage}")
        else:
            print("Distance must be positive.")

    # Public method to start engine (controls the private state)
    def start_engine(self):
        if self.__engine_status == "off":
            self.__engine_status = "on"
            print("Engine started!")
        else:
            print("Engine is already on.")

    # Public method to stop engine (controls the private state)
    def stop_engine(self):
        if self.__engine_status == "on":
            self.__engine_status = "off"
            print("Engine stopped.")
        else:
            print("Engine is already off.")

    # Public method to get engine status (controlled access to private state)
    def get_engine_status(self):
        return self.__engine_status

    def get_info(self):
        return f"{self.year} {self.make} {self.model} ({self.color}), Mileage: {self._mileage}, Engine: {self.__engine_status}"

# --- Demonstrating Encapsulation ---
my_car = Car("Tesla", "Model Y", 2023, "White", 100.0)

print(my_car.get_info())

# Try to modify mileage directly (it works, but it's bad practice due to '_')
my_car._mileage = -500 # This is allowed but violates the "protected" convention
print(f"Direct access to protected mileage: {my_car._mileage}") # Output: -500.0 (data integrity compromised!)
my_car.drive(50) # Now mileage goes to -450.0 - clearly wrong!

print("\n--- Correct Encapsulated Usage ---")
# Reset car for correct demo
my_car = Car("Tesla", "Model Y", 2023, "White", 100.0)
print(f"Initial Mileage: {my_car.get_mileage()}") # Access via public method

my_car.drive(200) # Correct way to update mileage
my_car.drive(-10) # Fails correctly because of internal check
print(f"Current Mileage: {my_car.get_mileage()}")

# Try to access a private attribute directly (will fail)
#print(my_car.__engine_status) # Uncomment this line to see an AttributeError!

# Accessing and controlling private state through public methods
print(f"Engine status: {my_car.get_engine_status()}")
my_car.start_engine()
my_car.start_engine() # Try starting again
print(f"Engine status: {my_car.get_engine_status()}")
my_car.stop_engine()
print(f"Engine status: {my_car.get_engine_status()}")