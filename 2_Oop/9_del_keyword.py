# 9_del_keyword.py

# del keywork is used to delete object properties or object itself

# del s1.name
# del s1

class Student:
  def __init__(self,name):
    self.name=name


s1=Student("Basit Ali Tariq")
# print(s1) # <__main__.Student object at 0x79990ebef1a0>
# del s1
# print(s1) # error

print(s1.name); # Basit Ali Tariq

del s1.name
print(s1.name) # error


