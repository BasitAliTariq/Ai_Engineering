# Multi level inheritance
    #  grand parent class ---> parent class ---> child class
    # A class is derived from another derived class, forming a    "chain" or multi-generational hierarchy

# Multilevel Inheritance

class Car:
  @staticmethod
  def start():
    print("Car started ... ")

  @staticmethod
  def stop():
    print("Car stopped ... ")


class TayotaCar(Car):
  def __init__(self,brand):
    self.brand=brand


class Fortuner(TayotaCar):
  def __init__(self,type):
    self.type=type


car1=Fortuner("disel")
car1.start();

