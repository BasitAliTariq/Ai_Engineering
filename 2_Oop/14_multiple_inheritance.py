# Multiple Inheritance
         # base class 1------------base class 2
         #                  |
         #            derived class

# A single child class inherits from **more than one** parent class simultaneously. The child gets access to attributes and methods of all parent classes.

# Multiple Inheritance


class A:
  varA="Welcome to class A"

class B:
  varB="Welcome to class B"

class C(A, B):
  varC= "Welcome to class C"



obj=C()
print(obj.varA);
print(obj.varB);
print(obj.varC);