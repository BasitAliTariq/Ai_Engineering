
# 8_encapsulation.py

# Encapsulation

# Wrapping data and functions into a single unit (object).

#  Encapsulation (Bundling & Protecting Data)Encapsulation means wrapping data (variables/attributes) and the functions (methods) that operate on that data into a single unit—a class. It also involves restricting direct access to sensitive internal data so it cannot be accidentally corrupted from outside the class.  



# Real-World Analogy: A medical capsule. It wraps different medicinal powders together into one neat unit, protecting the contents inside until they are used properly.
  
# Code Example: A bank account bundles the balance data with deposit() and withdraw() methods. By making __balance private, external code cannot arbitrarily set acc.__balance = -5000; it must go through controlled methods that validate the transaction.


# class BankAccount:
#     def __init__(self, owner, initial_balance):
#         self.owner = owner
#         self.__balance = initial_balance  # Private attribute (double underscore)

#     # Controlled method to modify data safely
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited ${amount}. New balance: ${self.__balance}")
#         else:
#             print("Invalid deposit amount.")

#     def get_balance(self):
#         return self.__balance

# acc = BankAccount("Ali", 1000)
# acc.deposit(500)          # Works safely via method
# # print(acc.__balance)    # Raises AttributeError: cannot access directly




class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)