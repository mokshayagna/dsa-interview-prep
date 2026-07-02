# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         print(f"{self.name} bark")

# dog1 = Dog("snoopy",3)
# dog1.bark()


"""Task 1 — Create a simple class
Create a Car class with attributes brand and color.
Create 2 objects and print their details.
    """
# class car:
#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color = color
    
# car1 = car("BMW","black")
# car2 = car("AUDI","RED")

# print(car1.brand)
# print(car1.color)
# print(car2.brand)
# print(car2.color)

"""
Task 2 — Add a method
Add a method drive() to the Car class that prints:
"BMW is driving!"
    """

# class car:
#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color = color
#     def drive(self):
#         print(f"{self.brand},is driving")

# car1 = car("BMW","black")
# car2 = car("AUDI","RED")

# car1.drive()

"""
    Task 3 — Create a Student class
Create a Student class with name, age, and marks.

Add a method is_passed() that prints Pass if marks >= 50, else Fail.
    """

# class student:
#     def __init__(self,name,age,marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
    
#     def pass_fail(self):
#         if self.marks > 30:
#             print(f"{self.name} passed the exam")
#         else:
#             print(f"{self.name} failed the exam")

# student1 = student("Moksha",23,55)
# student2 = student("xyz",22,23)

# student1.pass_fail()
# student2.pass_fail()


"""
Create a Bank class with a class attribute bank_name = "SBI".
Every object should share the same bank name, but have their own account_holder and balance.
    """

# class Bank:
#     def __init__(self,name,balance):
#         self.branch = "SBI"
#         self.name = name
#         self.balance = balance
#     def statement(self):
#         print(f"candidate {self.name} has {self.balance} balance in {self.branch} account")
    
# a = Bank("moksha",2345)
# b = Bank("xyz",34)

# a.statement()

"""
Task 5 — Add a method to update data
In the Bank class, add methods:

deposit(amount) — adds money to balance
withdraw(amount) — deducts money from balance
show_balance() — prints current balance

    """
# class Bank:
#     def __init__(self,name,balance,amount):
#         self.branch = "SBI"
#         self.name = name
#         self.balance = balance
#         self.amount = amount
#         self.final_amount = None
#     def deposit(self):
#         self.final_amount = self.balance + self.amount
#         print(f"Final ammount after deposit is {self.final_amount}")
#     def withdraw(self):
#         self.final_amount = self.balance - self.amount
#         print(f"Final amount after withdraw {self.final_amount}")
#     def show_balance(self):
#         print(f"balance:{self.final_amount}")
# a = Bank("moksha",23,5)

# a.deposit()
# a.withdraw()
# a.show_balance()
