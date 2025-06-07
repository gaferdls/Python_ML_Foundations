# opp_basics.py

#Define a simple class:
class Car:
    #The __init__ method is called when a new Car object is created\
    def __init__(self, make, model, year, color, mileage,train_type):
            self.make = make
            self.model = model
            self.year = year
            self.color = color
            self.mileage = mileage
            self.train_type = train_type

    def start_engine(self):
        return "Vroom! Engine started"

    def accelerate(self, speed_increase):
        self.mileage += speed_increase
        return f"Accelerating... Current mileage: {self.mileage}"

    def brake(self):
        return "Applying brakes..."

    def honk(self):
        return "Honk! Honk!"

    def get_info(self):
        return f"{self.make} {self.model} {self.year} ({self.color}), Mileage :  {self.mileage}, {self.train_type}wd"

#Create Car objects, providing initial values for the attributes
my_car = Car("Toyota", "Camry", 2022, "Silver", 25000.0,2)
rental_car = Car("Ford", "F-150",2024, "Blue", 10000.0, 4)

#You can print them to see they are distinct objects ( their memory address )
print(my_car.get_info())
print(rental_car.start_engine())
print(my_car.accelerate(500.0))
