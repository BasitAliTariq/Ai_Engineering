# Single inheritance 
      # base class ---> single child class 
      # A single child class inherits from a single parent class.


class Car:
  @staticmethod
  def start():
    print("Car started ... ")

  @staticmethod
  def stop():
    print("Car stopped ... ")


class Tayota(Car):
  def __init__(self,name):
    self.name=name


car1=Tayota("Fortuner")
car2=Tayota("Carolla")

car1.start()         # Car started ... 
print(car1.color)    # Black
print(car1.name)     # Fortuner
car1.stop()          # Car stopped ... 

car2.start()         # Car started ... 
print(car2.color)    # Black
print(car2.name)     # Carolla
car2.stop()          # Car stopped ...
