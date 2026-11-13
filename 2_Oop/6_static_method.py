

# 6_static_method.py

# Methods that don’t use the self parameter (work at class level) are static methods



class Student:
  def __init__(self,name,english,math,computer):
    self.name=name
    self.english=english
    self.math=math
    self.computer=computer

  @staticmethod  #decorator
  def hello():
    print("Hello ! Welcome to our sytem")

  def average(self):
    avg=(self.english+self.math+self.computer)/3
    print("The average of",self.name," marks is",avg)
  


s1=Student("Basit Ali Tariq",20,30,40)
s1.hello()
s1.average()

# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it

# In simple word we can says that Decorators gets methods as input , changes its behariour and return this method


