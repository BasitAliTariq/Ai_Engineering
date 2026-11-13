

# 4_methods.py

# Basically class is a collection of two things
# 1. Data -->attributes
# 2. Properties ---> Functions that class performs --->Methods

class Student:
  college="ABC college"  
    
  def __init__(self,name,marks): 
    self.name=name  
    self.marks=marks
    print("A new student is added in database")

  def welcome(self):
    print("Welcome",self.name)

  def get_marks(self):
    print("Your marks is",self.marks)


s1=Student("Basit Ali Tariq",80)
s1.welcome();
s1.get_marks()
