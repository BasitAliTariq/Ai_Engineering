# Polymorphism : Operator Overloading

# When the same operator is allowed to have different meaning according to the context.

# Operators & Dunder functions

# a + b   #addition        a.__add__(b)
# a - b   #subtraction     a.__sub__(b)
# a * b   #multiplication  a.__mul____(b)
# a / b   #division        a.__truediv____(b)
# a % b   #addition        a.__mod____(b)


# print(5+7) #12

# print("Basit"+" Ali") # Basit Ali

# print([1,3,4]+[6,7,8]) # [1, 3, 4, 6, 7, 8]


# Complex number class

class Complex:
  def __init__(self,real,imaginary):
    self.real=real
    self.imaginary=imaginary

  def show_Number(self):
    print(self.real,"i +",self.imaginary,"j")

  def __add__(self, num2):
    newReal = self.real + num2.real
    newImg = self.imaginary + num2.imaginary
    return Complex(newReal, newImg)


num1=Complex(3,5)
num1.show_Number()

num2=Complex(4,7)
num2.show_Number()

num3=num1+num2
num3.show_Number()

