# Exceptions are the errors detected at the program of execution

# print(1/0)


x=input("Enter number1: ")
y=input("Enter number2: ")
z='none'
try:
  z=int(x)/int(y)
except Exception as e:
  print("Exception occur",e)
print("Division is: ", z)