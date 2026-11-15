# 10_private_attribute.py

# Private(like) attributes & methods   

# Conceptual Implementations in Python

# Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.


# Problematic code

# class Account:
#   def __init__(self,acc_no,acc_pass):
#     self.acc_no=acc_no
#     self.acc_pass=acc_pass

# acc1=Account(1233,'basit')
# print(acc1.acc_no) # 1233
# print(acc1.acc_pass) # basit

# Now problem is here account number and account apssword are sensitive information they cannot be accessed outside the class

# Solution

# kisi bi attribute ya function ko private banany ke  hum us ke peechay double underscore __ lagatay hai

class Account:
  def __init__(self,acc_no,acc_pass):
    self.__acc_no=acc_no
    self.__acc_pass=acc_pass

  def dispaly_password(self):
    return self.__acc_pass
   

acc1=Account(1233,'basit')
print(acc1.dispaly_password()) 