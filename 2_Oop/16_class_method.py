# class method

# A class method is bound to the class & receives the class as an implicit first argument.

# Note - static method can't access or modify class state & generally for utility.

# class Student:
#     @classmethod #decorator
#     def college( cls ):
#         pass



# Problem 

# class Person:
#   name="Basit" #class attribute 
#   def change_name(self,name):
#     self.name=name  # object attribute


# p1=Person()
# p1.change_name("Asad")
# print(p1.name)  #Asad
# print(Person.name) #Basit

# Problem that class method solve
# I need to the change the class attribute but as you can see that change_method changes the object attribute


# For this we have three way


# 1st way

# class Person:
#   name="Basit" #class attribute 
#   def change_name(self,name):
#     Person.name=name  # object attribute


# p1=Person()
# p1.change_name("Asad")
# print(p1.name)  #Asad
# print(Person.name) #Asad



# 2nd way

# class Person:
#   name="Basit" #class attribute 
#   def change_name(self,name):
#     self.__class__.name=name  


# p1=Person()
# p1.change_name("Asad")
# print(p1.name)  #Asad
# print(Person.name) #Asad

# 3rd way class method

class Person:
  name="Basit" #class attribute 
  @classmethod
  def change_name(cls,name):
    cls.name=name  


p1=Person()
p1.change_name("Asad")
print(p1.name)  #Asad
print(Person.name) #Asad