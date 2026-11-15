# Super method

# Super method is used tyo accesss the methods of paret class

class Car:

  def __init__(self,type):
    self.type=type


  @staticmethod
  def start():
    print("Car started ... ")

  @staticmethod
  def stop():
    print("Car stopped ... ")


class Tayota(Car):
  def __init__(self,name,type):
    super().__init__(type) 
    self.name=name
    super().start()


car1=Tayota("Fortuner","Disel")
print(car1.type)
print(car1.name)