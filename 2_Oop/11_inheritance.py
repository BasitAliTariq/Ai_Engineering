
# 10_inheritance.py

# Inheritance  

# When one class(child/derived) derives the properties & methods of another class(parent/base).   

# class Car:
#     ....

# class ToyotaCar( Car ):
#     ....


class Car:
  color="Black"
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



# Types of Inheritance 
# Single inheritance 
      # base class ---> single child class 
      # A single child class inherits from a single parent class.
# Multi level inheritance
    #  grand parent class ---> parent class ---> child class
    # A class is derived from another derived class, forming a    "chain" or multi-generational hierarchy

# Multiple Inheritance
         # base class 1------------base class 2
         #                  |
         #            derived class

# A single child class inherits from **more than one** parent class simultaneously. The child gets access to attributes and methods of all parent classes.




















