


# 2_constructor.py


# init function or constructor

# All classes have a function called __init__(), which is always executed when the object is being initiated.



# class Student:
#   name="Basit Ali Tariq"
#   def __init__(self):
#     print("A new student is added in database")



# s1=Student()
# print(s1.name)



# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# class Student:
#   name="Basit Ali Tariq"
#   def __init__(self):
#     print(self) #<__main__.Student object at 0x7d87182ef380>
#     print("A new student is added in database")



# s1=Student()
# print(s1) # <__main__.Student object at 0x7d87182ef380>




# How to change name dynamically
# class Student:
#   def __init__(self,full_name):
#     self.name=full_name
#     print("A new student is added in database")



# s1=Student("Basit Ali Tariq")
# print(s1.name)  # Basit Ali Tariq


# s2=Student("Fahad")
# print(s2.name) #Fahad


# now student class has name and marks as well

# class Student:
#   def __init__(self,name,marks):
#     self.name=name
#     self.marks=marks
#     print("A new student is added in database")



# s1=Student("Basit Ali Tariq",80)
# print('Name :',s1.name,"Marks :",s1.marks)  # Name : Basit Ali Tariq Marks : 80

# s2=Student("Fahad",90)
# print('Name :',s2.name,"Marks :",s2.marks) #Name : Fahad Marks : 90



# Default constructor and parameterized constructor


class Student:
  def _init__(self): #default constructor
    print('This is default constructor')

  
  def __init__(self,name,marks): # parameterized constructor
    self.name=name
    self.marks=marks
    print("A new student is added in database")



s1=Student("Basit Ali Tariq",80)
print('Name :',s1.name,"Marks :",s1.marks)  # Name : Basit Ali Tariq Marks : 80

s2=Student("Fahad",90)
print('Name :',s2.name,"Marks :",s2.marks) #Name : Fahad Marks : 90













