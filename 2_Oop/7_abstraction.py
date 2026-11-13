
# 7_abstraction.py

# Abstraction

# Hiding the implementation details of a class and only showing the essential features to the user.


# Abstraction (Hiding Complexity)Abstraction means hiding complex internal implementation details and exposing only the essential, high-level interface to the user.It focuses on what an object does rather than how it does it.  
  
  # Real-World Analogy: Driving a car. You only interact with the steering wheel, pedals, and gearshift. You don't need to understand internal combustion, fuel injection, or hydraulic brake pressure to drive.

  # Code Example: When you call car.start(), the complex sequence of checking sensors, igniting fuel, and engaging the starter motor is hidden behind a single, clean method.



class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    # High-level interface exposed to the user
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started...")

# The user only calls start(), completely unaware of clutch/accelerator mechanics
my_car = Car()
my_car.start()


