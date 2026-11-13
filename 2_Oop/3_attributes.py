
# 3_attributes.py

# Supose hum pjir wohi senerio letay hai ke hamy ek college ke liay  system design kerna hai jis me studets ka data ho ga

# attribute: varibales in side class

# object / Instance attribute : Esa attribute jo her object ke different us ko hum object attribute me rakhtay hai jesay is senerio her student ka name different ho ga 


# Class  attribute

#  Esa attribute jis ki value her object ke liay same ho is ko hum class attribute me rakhtay hai like is senerio me her student ka college name same ho ga


# see below demo code


class Student:
  college="ABC college"  # class attribute
    
  def __init__(self,name,marks): 
    self.name=name   # object attribute
    self.marks=marks
    print("A new student is added in database")


s1=Student("Basit Ali Tariq",80)
print('Name :',s1.name,"Marks :",s1.marks)  # Name : Basit Ali Tariq Marks : 80

s2=Student("Fahad",90)
print('Name :',s2.name,"Marks :",s2.marks) #Name : Fahad Marks : 90


print(s1.college) # ABC college

print(s2.college) # ABC college

# Note : Hum class attributes ko class name se bi likh saktay hai

print(Student.college) # ABC college
