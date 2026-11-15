# Property

# We use @property decorator on any method in the class to use the method as a property.

# suppose hum ne ek system banana hai jis me three subjects ke  marks ae gay or phir un ki perecentage 
# calculate kerni hai per is me twist ye hai ke ager baad me subject ke marks change ho to  uski percentge
# auto change honi chahiay  

# class Student:
#   def __init__(self,phy,chem,math):
#     self.phy=phy
#     self.chem=chem
#     self.math=math
#     self.percentage=str((self.phy+self.chem+self.math)/3)

# st1=Student(89,60,98)
# print(st1.percentage) # 82.33333333333333

# st1.phy=50
# print(st1.phy) # 50
# print(st1.percentage) # 82.33333333333333


# Now you can see that percentage is not changing this problem is solved by property decorator


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

st1 = Student(98, 97, 99)
st1=Student(89,60,98)
print(st1.percentage) # 82.33333333333333

st1.phy=50
print(st1.phy) # 50
print(st1.percentage) # 69.33333333333333%
