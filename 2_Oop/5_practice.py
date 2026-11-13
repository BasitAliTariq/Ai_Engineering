

# 5_practice.py


# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:
  def __init__(self,name,english,math,computer):
    self.name=name
    self.english=english
    self.math=math
    self.computer=computer

  def average(self):
    avg=(self.english+self.math+self.computer)/3
    print("The average of",self.name," marks is",avg)


s1=Student("Basit Ali Tariq",20,30,40)
s1.average()
