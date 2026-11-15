# Complete Python Object-Oriented Programming (OOP) Guide

## Table of Contents

1. [Object-Oriented Programming in Python](#1-object-oriented-programming-in-python)
2. [Procedural Programming and the Need for OOP](#2-procedural-programming-and-the-need-for-oop)
3. [Classes and Objects](#3-classes-and-objects)
4. [Constructors and `__init__()` Function](#4-constructors-and-__init__-function)
5. [Attributes (Class and Object Attributes)](#5-attributes-class-and-object-attributes)
6. [Methods](#6-methods)
7. [Static Methods](#7-static-methods)
8. [Abstraction](#8-abstraction)
9. [Encapsulation](#9-encapsulation)
10. [`del` Keyword](#10-del-keyword)
11. [Private Attributes and Methods](#11-private-attributes-and-methods)
12. [Inheritance](#12-inheritance)
13. [Types of Inheritance](#13-types-of-inheritance)
14. [`super()` Method](#14-super-method)
15. [Class Methods](#15-class-methods)
16. [Property Decorator](#16-property-decorator)
17. [Getter Decorator](#17-getter-decorator)
18. [Setter Decorator](#18-setter-decorator)
19. [Polymorphism](#19-polymorphism)
20. [Operator Overloading and Dunder Functions](#20-operator-overloading-and-dunder-functions)

---

# 1. Object-Oriented Programming in Python

## Definition

Object-Oriented Programming (OOP) is a programming approach in which we organize our code using classes and objects.

It combines data (attributes) and functions (methods) into a single unit called an object.

OOP makes programs more organized, reusable, maintainable, and easier to manage.

## Four Main Principles of OOP

1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

## Example

```python
class Student:

    def study(self):
        print("Student is studying")

    def play(self):
        print("Student is playing")


# Creating an object
student1 = Student()

# Calling methods
student1.study()
student1.play()
```

**Output:**

```text
Student is studying
Student is playing
```

**Explanation:**

- `class Student`: Creates a class.
- `study()` and `play()`: Methods of the class.
- `student1`: Object of the Student class.
- `student1.study()`: Calls the study method.

## Advantages of OOP

1. **Code Reusability:** We can reuse existing code through inheritance.
2. **Modularity:** We can divide a large program into smaller classes.
3. **Maintainability:** Code becomes easier to update and manage.
4. **Security:** Encapsulation helps control access to data.
5. **Flexibility:** Polymorphism allows the same interface to work with different objects.

---

# 2. Procedural Programming and the Need for OOP

## What is Procedural Programming?

Procedural Programming is a programming approach in which a program is divided into functions or procedures.

In this approach, we write instructions step by step and use functions to perform different tasks.

It focuses on functions rather than objects.

## Example of Procedural Programming

```python
# Data
student_name = "Basit"
student_age = 22
student_marks = 85


# Functions
def display_student():
    print("Name:", student_name)
    print("Age:", student_age)
    print("Marks:", student_marks)


def calculate_grade():
    if student_marks >= 80:
        print("Grade: A")
    else:
        print("Grade: B")


display_student()
calculate_grade()
```

**Output:**

```text
Name: Basit
Age: 22
Marks: 85
Grade: A
```

Here, data and functions are separate.

## What is the Need for OOP?

Consider a school management system containing:

- Students
- Teachers
- Courses
- Departments

If we use procedural programming, we may need to create many separate variables and functions.

As the application grows, managing the data and functions becomes difficult.

OOP solves this problem by combining related data and functions into classes.

## Same Example Using OOP

```python
class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display_student(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

    def calculate_grade(self):
        if self.marks >= 80:
            print("Grade: A")
        else:
            print("Grade: B")


student1 = Student("Basit", 22, 85)

student1.display_student()
student1.calculate_grade()
```

**Output:**

```text
Name: Basit
Age: 22
Marks: 85
Grade: A
```

## Difference Between Procedural and OOP

| Procedural Programming                          | Object-Oriented Programming                    |
| ----------------------------------------------- | ---------------------------------------------- |
| Focuses on functions                            | Focuses on objects                             |
| Data and functions are separate                 | Data and functions are combined                |
| Uses a step-by-step approach                    | Uses classes and objects                       |
| Code reuse mainly through functions             | Code reuse through inheritance and composition |
| Can become difficult to manage in large systems | Helps organize large systems                   |

**Important:** Procedural programming is useful for small scripts and simple programs. OOP becomes particularly useful when applications grow and contain multiple related entities.

---

# 3. Classes and Objects

## What is a Class?

A class is a blueprint or template used to create objects.

It defines the attributes (data) and methods (functions) that its objects will have.

**Syntax:**

```python
class ClassName:

    # Attributes
    # Methods
    pass
```

## What is an Object?

An object is an instance of a class.

We create objects using the class name followed by parentheses.

**Syntax:**

```python
object_name = ClassName()
```

## Example

```python
class Car:

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")


# Creating objects
car1 = Car()
car2 = Car()


# Calling methods
car1.start()
car2.stop()
```

**Output:**

```text
Car is starting
Car is stopping
```

Here:

- `Car` is a class.
- `car1` and `car2` are objects.
- `start()` and `stop()` are methods.

## Real-Life Example

Think about a car manufacturing company.

- Class: Car
- Objects: Honda Civic, Toyota Corolla, Suzuki Alto
- Attributes: Color, model, price
- Methods: Start, stop, accelerate

One class can create multiple objects with different data.

---

# 4. Constructors and `__init__()` Function

## What is a Constructor?

A constructor is a special mechanism used during object creation to initialize an object.

In Python, `__init__()` is commonly called the constructor, although technically it is the initializer.

The actual object creation process is handled by `__new__()`.

Its main purpose is to initialize object attributes.

## Syntax

```python
class ClassName:

    def __init__(self):
        # Initialization code
        pass
```

## Example

```python
class Student:

    def __init__(self):
        print("Constructor called")

    def study(self):
        print("Student is studying")


student1 = Student()
student1.study()
```

**Output:**

```text
Constructor called
Student is studying
```

Notice that we did not call `__init__()` manually. Python called it when we created the object.

## Types of Constructors

Python does not have multiple built-in constructor categories like some other languages. However, constructors are commonly explained using the following patterns.

### 1. Default Constructor

When we do not define `__init__()`, Python provides an inherited initializer that does not accept additional initialization arguments.

```python
class Student:

    def study(self):
        print("Student is studying")


student1 = Student()
student1.study()
```

**Output:**

```text
Student is studying
```

### 2. Non-Parameterized Constructor

A constructor that does not accept additional parameters except `self`.

```python
class Student:

    def __init__(self):
        self.name = "Basit"
        self.age = 22

    def display(self):
        print(self.name)
        print(self.age)


student1 = Student()
student1.display()
```

**Output:**

```text
Basit
22
```

### 3. Parameterized Constructor

A constructor that accepts parameters to initialize object attributes.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Basit", 22)
student2 = Student("Ahsan", 23)

student1.display()
student2.display()
```

**Output:**

```text
Name: Basit
Age: 22
Name: Ahsan
Age: 23
```

### 4. Constructor with Default Arguments

We can also provide default values for constructor parameters.

```python
class Student:

    def __init__(self, name="Unknown", age=18):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


student1 = Student()
student2 = Student("Basit", 22)

student1.display()
student2.display()
```

**Output:**

```text
Unknown 18
Basit 22
```

### 5. Alternative Constructor Using Class Method

Python does not support traditional constructor overloading.

However, we can create alternative object-creation methods using `@classmethod`.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))


student1 = Student.from_string("Basit-22")

print(student1.name)
print(student1.age)
```

**Output:**

```text
Basit
22
```

### Important: Constructor Overloading

Python does not support defining multiple `__init__()` methods with different parameter lists.

If we define `__init__()` multiple times, the last definition replaces the previous one.

We can achieve similar behavior using default arguments or `*args` and `**kwargs`.

## Difference Between `__new__()` and `__init__()`

| `__new__()`                      | `__init__()`                         |
| -------------------------------- | ------------------------------------ |
| Creates the object               | Initializes the object               |
| Called before `__init__()`       | Called after `__new__()`             |
| Returns the new object           | Usually returns `None`               |
| Used in advanced object creation | Used in normal object initialization |

---

# 5. Attributes (Class and Object Attributes)

## What are Attributes?

Attributes are variables associated with a class or an object.

There are two main types:

1. Class Attributes
2. Instance (Object) Attributes

## 1. Class Attributes

Class attributes are variables defined inside a class but outside its methods.

They are shared by all instances unless an instance has its own attribute with the same name.

**Example:**

```python
class Student:

    university = "University of Education"

    def __init__(self, name):
        self.name = name


student1 = Student("Basit")
student2 = Student("Ahsan")

print(student1.university)
print(student2.university)
```

**Output:**

```text
University of Education
University of Education
```

Both objects access the same class attribute.

## 2. Instance Attributes

Instance attributes belong to individual objects.

They are usually created using `self` inside the constructor.

**Example:**

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Basit", 22)
student2 = Student("Ahsan", 23)

print(student1.name)
print(student2.name)

print(student1.age)
print(student2.age)
```

**Output:**

```text
Basit
Ahsan
22
23
```

Each object has its own name and age.

## Difference Between Class and Instance Attributes

| Class Attributes               | Instance Attributes                 |
| ------------------------------ | ----------------------------------- |
| Defined inside the class       | Usually defined inside `__init__()` |
| Shared through the class       | Belong to individual objects        |
| Accessed using class or object | Accessed using object               |
| Common across instances        | Can have different values           |

## Important Example: Modifying Class Attributes

```python
class Student:

    university = "UE"

    def __init__(self, name):
        self.name = name


student1 = Student("Basit")
student2 = Student("Ahsan")

Student.university = "PU"

print(student1.university)
print(student2.university)
```

**Output:**

```text
PU
PU
```

Changing the class attribute through the class changes the shared value.

However, if we assign `student1.university = "FAST"`, we create an instance attribute that shadows the class attribute for that object.

---

# 6. Methods

## What are Methods?

Methods are functions defined inside a class.

They are used to perform operations related to the class and its objects.

There are three commonly discussed types of methods:

1. Instance Methods
2. Class Methods
3. Static Methods

## 1. Instance Methods

Instance methods operate on individual objects.

They take `self` as their first parameter.

`self` represents the current object.

**Example:**

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)


student1 = Student("Basit")
student1.display()
```

**Output:**

```text
Student Name: Basit
```

Here, `self.name` accesses the attribute of the current object.

## Why Do We Use `self`?

Suppose we create two objects:

```python
student1 = Student("Basit")
student2 = Student("Ahsan")
```

When we call:

```python
student1.display()
```

Python internally passes `student1` as the first argument.

Conceptually:

```python
Student.display(student1)
```

Similarly:

```python
Student.display(student2)
```

`self` is a convention, not a reserved keyword. However, using `self` is the standard Python practice.

---

# 7. Static Methods

## What is a Static Method?

A static method is a method that belongs to a class but does not require access to instance attributes or class attributes.

It is defined using the `@staticmethod` decorator.

It does not receive `self` or `cls` automatically.

## Syntax

```python
class ClassName:

    @staticmethod
    def method_name():
        pass
```

## Example

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print(Calculator.add(10, 20))
print(Calculator.multiply(5, 4))
```

**Output:**

```text
30
20
```

We can call static methods directly using the class name.

## Why Use Static Methods?

Use static methods when a function is logically related to a class but does not need object or class data.

For example, a calculator class can contain mathematical operations.

---

# 8. Abstraction

## Definition

Abstraction is an OOP principle that hides unnecessary implementation details and exposes only the essential functionality to the user.

It focuses on what an object does rather than how it does it.

## Real-Life Example

Consider an ATM machine.

When you withdraw money:

- You enter your PIN.
- You select the withdrawal option.
- You enter the amount.
- The ATM gives you money.

You do not need to know the internal banking operations, database queries, or transaction processing.

This is abstraction.

## Abstraction in Python

Python provides the `abc` module to implement formal abstract classes and methods.

Important components:

- `ABC`: Abstract Base Class.
- `@abstractmethod`: Defines an abstract method.

## Example

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

**Output:**

```text
Dog barks
Cat meows
```

## Important Points

1. An abstract class is a blueprint for other classes.
2. An abstract method must be implemented by a concrete subclass before its objects can be created.
3. We cannot instantiate an abstract class that still has unimplemented abstract methods.
4. Abstraction helps define a common interface.

---

# 9. Encapsulation

## Definition

Encapsulation is an OOP principle in which data and methods are combined inside a class.

It also helps control how an object's internal data is accessed or modified.

## Real-Life Example

Consider a bank account.

A user should not directly change the account balance without following the required rules.

Instead, we provide methods such as:

- Deposit
- Withdraw
- Check Balance

## Example

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance


account = BankAccount(10000)

account.deposit(2000)
account.withdraw(3000)

print(account.get_balance())
```

**Output:**

```text
9000
```

Here:

- `__balance` is a name-mangled attribute.
- `deposit()` controls how money is added.
- `withdraw()` controls how money is removed.
- `get_balance()` provides access to the balance.

**Important:** Python does not provide strict private access control. Encapsulation is implemented using naming conventions and controlled interfaces.

---

# 10. `del` Keyword

## Definition

The `del` keyword is used to delete references to variables, object attributes, or items from collections.

In OOP, it can be used to delete object attributes or references to objects.

## 1. Deleting a Variable

```python
name = "Basit"

print(name)

del name

# print(name)  # NameError
```

**Output:**

```text
Basit
```

The final line is commented out because accessing the deleted variable would raise a `NameError`.

## 2. Deleting an Object Attribute

```python
class Student:

    def __init__(self, name):
        self.name = name
        self.age = 22


student1 = Student("Basit")

print(student1.name)

del student1.name

# print(student1.name)  # AttributeError
```

**Output:**

```text
Basit
```

After deleting the attribute, accessing it raises an `AttributeError`.

## 3. Deleting an Object Reference

```python
class Student:

    def __init__(self, name):
        self.name = name


student1 = Student("Basit")

del student1
```

Here, we delete the variable `student1`.

**Important:** `del student1` does not necessarily destroy the object immediately. If another reference points to the same object, the object continues to exist.

## Difference Between `del` and `__del__()`

| `del`                                           | `__del__()`                                 |
| ----------------------------------------------- | ------------------------------------------- |
| Python keyword                                  | Special method                              |
| Deletes a reference or attribute                | Finalizer called during object finalization |
| Used explicitly by programmers                  | Usually called automatically                |
| Does not guarantee immediate object destruction | Execution timing is not guaranteed          |

---

# 11. Private Attributes and Methods

## What are Private Attributes?

Private attributes are attributes that are intended to be accessed only within the class.

In Python, we use double underscores (`__`) before an attribute name to trigger name mangling.

## Example

```python
class Student:

    def __init__(self):
        self.__name = "Basit"
        self.__age = 22

    def display(self):
        print(self.__name)
        print(self.__age)


student1 = Student()

student1.display()
```

**Output:**

```text
Basit
22
```

Trying to access these attributes directly:

```python
# print(student1.__name)
```

Raises:

```text
AttributeError
```

## What is Name Mangling?

Python internally changes the name of a double-underscore attribute.

For example:

```python
self.__name
```

Becomes approximately:

```python
self._Student__name
```

We can technically access it using the mangled name:

```python
print(student1._Student__name)
```

**Output:**

```text
Basit
```

This shows that Python's private attributes are not truly inaccessible. Name mangling mainly prevents accidental access and naming conflicts.

## What are Private Methods?

Private methods are methods that are intended to be used inside the class.

They also use double underscores.

**Example:**

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def __check_balance(self):
        print("Current Balance:", self.__balance)

    def display(self):
        self.__check_balance()


account = BankAccount(5000)

account.display()
```

**Output:**

```text
Current Balance: 5000
```

## Types of Attribute Naming in Python

| Syntax   | Meaning                                 |
| -------- | --------------------------------------- |
| `name`   | Public attribute                        |
| `_name`  | Protected-style attribute (convention)  |
| `__name` | Private-style attribute (name mangling) |

**Important:** Python does not enforce Java-style protected or private access modifiers.

---

# 12. Inheritance

## Definition

Inheritance is an OOP principle in which one class acquires the attributes and methods of another class.

It allows us to reuse existing code and create relationships between classes.

## Important Terms

1. Parent Class: The class whose properties are inherited.
2. Child Class: The class that inherits from another class.
3. Base Class: Another name for parent class.
4. Derived Class: Another name for child class.

## Syntax

```python
class Parent:

    def method1(self):
        print("Parent method")


class Child(Parent):

    def method2(self):
        print("Child method")
```

## Example

```python
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()
```

**Output:**

```text
Animal is eating
Dog is barking
```

The `Dog` class inherits the `eat()` method from `Animal`.

## Why Do We Use Inheritance?

1. Code Reusability
2. Reduces Code Duplication
3. Easier Maintenance
4. Supports Method Overriding
5. Helps create hierarchical relationships

---

# 13. Types of Inheritance

Python supports five commonly discussed types of inheritance.

## 1. Single Inheritance

One child class inherits from one parent class.

**Structure:**

Parent → Child

**Example:**

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


dog = Dog()

dog.eat()
dog.bark()
```

**Output:**

```text
Eating
Barking
```

## 2. Multiple Inheritance

One child class inherits from two or more parent classes.

**Structure:**

Parent1 + Parent2 → Child

**Example:**

```python
class Father:

    def father_property(self):
        print("Father's property")


class Mother:

    def mother_property(self):
        print("Mother's property")


class Child(Father, Mother):

    def child_property(self):
        print("Child's property")


child = Child()

child.father_property()
child.mother_property()
child.child_property()
```

**Output:**

```text
Father's property
Mother's property
Child's property
```

## 3. Multilevel Inheritance

A class inherits from a child class, creating multiple levels of inheritance.

**Structure:**

Grandparent → Parent → Child

**Example:**

```python
class Grandparent:

    def house(self):
        print("Grandparent's house")


class Parent(Grandparent):

    def car(self):
        print("Parent's car")


class Child(Parent):

    def bike(self):
        print("Child's bike")


child = Child()

child.house()
child.car()
child.bike()
```

**Output:**

```text
Grandparent's house
Parent's car
Child's bike
```

## 4. Hierarchical Inheritance

Multiple child classes inherit from one parent class.

**Structure:**

Parent → Child1

Parent → Child2

**Example:**

```python
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


class Cat(Animal):

    def meow(self):
        print("Cat is meowing")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()
```

**Output:**

```text
Animal is eating
Dog is barking
Animal is eating
Cat is meowing
```

## 5. Hybrid Inheritance

Hybrid inheritance is a combination of two or more types of inheritance.

**Example:**

```python
class A:

    def method_a(self):
        print("Class A")


class B(A):

    def method_b(self):
        print("Class B")


class C(A):

    def method_c(self):
        print("Class C")


class D(B, C):

    def method_d(self):
        print("Class D")


obj = D()

obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()
```

**Output:**

```text
Class A
Class B
Class C
Class D
```

## Summary of Inheritance Types

| Type         | Explanation                        |
| ------------ | ---------------------------------- |
| Single       | One parent, one child              |
| Multiple     | One child, multiple parents        |
| Multilevel   | Inheritance across multiple levels |
| Hierarchical | Multiple children, one parent      |
| Hybrid       | Combination of inheritance types   |

---

# 14. `super()` Method

## Definition

`super()` is a built-in Python function that provides access to methods of the next class in the Method Resolution Order (MRO).

It is commonly used to call a parent class's constructor or methods from a child class.

## Example 1: Calling Parent Constructor

```python
class Parent:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Child(Parent):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        super().display()
        print("Age:", self.age)


child = Child("Basit", 22)

child.show()
```

**Output:**

```text
Name: Basit
Age: 22
```

**Explanation:**

- `super().__init__(name)` calls the next class's constructor in the MRO.
- `super().display()` calls the next class's `display()` method.
- `self.age = age` initializes the child-specific attribute.

## Example 2: Method Overriding with `super()`

```python
class Parent:

    def show(self):
        print("Parent method")


class Child(Parent):

    def show(self):
        super().show()
        print("Child method")


obj = Child()

obj.show()
```

**Output:**

```text
Parent method
Child method
```

## Important Points

1. `super()` avoids directly naming the parent class.
2. It is useful in multiple inheritance.
3. It follows the Method Resolution Order (MRO).
4. It can call parent or next-in-line class methods.

---

# 15. Class Methods

## Definition

A class method is a method that works with class-level data rather than individual object data.

It is defined using the `@classmethod` decorator.

A class method takes `cls` as its first parameter.

`cls` represents the current class.

## Syntax

```python
class ClassName:

    @classmethod
    def method_name(cls):
        pass
```

## Example

```python
class Student:

    university = "UE"

    @classmethod
    def change_university(cls, new_name):
        cls.university = new_name


print(Student.university)

Student.change_university("Punjab University")

print(Student.university)
```

**Output:**

```text
UE
Punjab University
```

## Why Use Class Methods?

Class methods are useful when we need to:

1. Access class attributes.
2. Modify class-level data.
3. Create alternative constructors.
4. Implement operations related to the class rather than an individual object.

## Difference Between Instance, Class, and Static Methods

| Feature            | Instance Method   | Class Method      | Static Method      |
| ------------------ | ----------------- | ----------------- | ------------------ |
| Decorator          | None              | `@classmethod`    | `@staticmethod`    |
| First parameter    | `self`            | `cls`             | None automatically |
| Access object data | Yes               | Not through `cls` | No automatically   |
| Access class data  | Yes               | Yes               | No automatically   |
| Main purpose       | Object operations | Class operations  | Utility operations |

---

# 16. Property Decorator

## Definition

The `@property` decorator allows us to access a method like an attribute.

It is commonly used to implement controlled access to object attributes.

It allows us to use getter and setter functionality without changing how we access the attribute.

## Example

```python
class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


student = Student("Basit")

print(student.name)
```

**Output:**

```text
Basit
```

Notice that we accessed `name` without parentheses.

Normally, we call a method like this:

```python
student.name()
```

But with `@property`, we access it like an attribute:

```python
student.name
```

## Why Use the Property Decorator?

1. Provides controlled access to attributes.
2. Helps implement encapsulation.
3. Allows validation before changing values.
4. Makes methods behave like attributes.
5. Helps change internal implementation without changing the public interface.

---

# 17. Getter Decorator

## Definition

A getter is a method used to retrieve or read the value of an attribute.

In Python, we commonly implement getters using the `@property` decorator.

## Example

```python
class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


student = Student("Basit")

# Getter
print(student.name)
```

**Output:**

```text
Basit
```

Here:

- `@property` defines the getter.
- `name()` is the underlying method name.
- `student.name` retrieves the value.

**Important:** A getter does not necessarily mean that the attribute is private. It provides a controlled way to read a value.

---

# 18. Setter Decorator

## Definition

A setter is a method used to update or modify the value of an attribute.

In Python, we implement setters using the `@attribute_name.setter` decorator.

## Example

```python
class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if new_name:
            self._name = new_name
        else:
            print("Name cannot be empty")


student = Student("Basit")

print(student.name)

student.name = "Ali"

print(student.name)
```

**Output:**

```text
Basit
Ali
```

## Complete Getter and Setter Example

```python
class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    # Getter
    @property
    def balance(self):
        return self._balance

    # Setter
    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Balance cannot be negative")


account = BankAccount(10000)

# Getting value
print(account.balance)

# Setting value
account.balance = 15000

print(account.balance)

# Invalid value
account.balance = -500
```

**Output:**

```text
10000
15000
Balance cannot be negative
```

## Difference Between Getter and Setter

| Getter                      | Setter                   |
| --------------------------- | ------------------------ |
| Reads an attribute          | Modifies an attribute    |
| Uses `@property`            | Uses `@attribute.setter` |
| Returns a value             | Usually updates a value  |
| Does not require assignment | Uses assignment syntax   |

---

# 19. Polymorphism

## Definition

Polymorphism is an OOP principle in which the same interface, method, or operation can behave differently depending on the object or data type.

The word polymorphism means "many forms".

## Real-Life Example

Consider the `speak()` action.

- Dog speaks by barking.
- Cat speaks by meowing.
- Cow speaks by mooing.

The action is the same, but its behavior is different.

## Example 1: Polymorphism Through Method Overriding

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

**Output:**

```text
Dog barks
Cat meows
```

Both classes have a method named `sound()`, but the implementation is different.

## Example 2: Polymorphism Through a Common Interface

```python
class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


class Cow:

    def sound(self):
        print("Cow moos")


def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()
cow = Cow()

make_sound(dog)
make_sound(cat)
make_sound(cow)
```

**Output:**

```text
Dog barks
Cat meows
Cow moos
```

The same function works with different objects.

This is an example of duck typing in Python.

## Example 3: Polymorphism Through Built-in Functions

```python
print(len("Python"))
print(len([10, 20, 30]))
print(len({"name": "Basit", "age": 22}))
```

**Output:**

```text
6
3
2
```

The same `len()` function works with strings, lists, and dictionaries.

## Types of Polymorphism Commonly Discussed

1. **Method Overriding:** A child class provides its own implementation of an inherited method.
2. **Operator Overloading:** An operator behaves differently for different objects.
3. **Duck Typing:** Objects are used based on their supported behavior rather than their specific class.

**Important:** Python does not support traditional method overloading by defining multiple methods with the same name and different parameter lists. Default arguments and `*args` can be used to achieve similar behavior.

---

# 20. Operator Overloading and Dunder Functions

## What is Operator Overloading?

Operator overloading allows us to define how operators behave when they are used with objects of our own classes.

For example:

- `+` adds numbers.
- `-` subtracts numbers.
- `*` multiplies numbers.
- `==` compares values.

We can customize these operations for our own objects.

## What are Dunder Functions?

Dunder stands for Double Underscore.

Dunder methods are special methods whose names start and end with double underscores.

Examples:

- `__init__()`
- `__str__()`
- `__add__()`
- `__sub__()`
- `__mul__()`
- `__eq__()`
- `__len__()`

They are also called magic methods or special methods.

## 1. `__init__()`

Initializes an object.

```python
class Student:

    def __init__(self, name):
        self.name = name


student = Student("Basit")
```

## 2. `__str__()`

Defines the human-readable string representation of an object.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student Name: {self.name}"


student = Student("Basit")

print(student)
```

**Output:**

```text
Student Name: Basit
```

## 3. `__add__()`

Defines the behavior of the `+` operator.

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


num1 = Number(10)
num2 = Number(20)

print(num1 + num2)
```

**Output:**

```text
30
```

Internally, this:

```python
num1 + num2
```

Works like:

```python
num1.__add__(num2)
```

## 4. `__sub__()`

Defines the behavior of the `-` operator.

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value


num1 = Number(50)
num2 = Number(20)

print(num1 - num2)
```

**Output:**

```text
30
```

## 5. `__mul__()`

Defines the behavior of the `*` operator.

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return self.value * other.value


num1 = Number(10)
num2 = Number(5)

print(num1 * num2)
```

**Output:**

```text
50
```

## 6. `__eq__()`

Defines the behavior of the `==` operator.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


student1 = Student("Basit")
student2 = Student("Basit")

print(student1 == student2)
```

**Output:**

```text
True
```

Without implementing `__eq__()`, objects normally use identity-based equality.

## Important Dunder Functions

| Dunder Method    | Operator / Purpose                |
| ---------------- | --------------------------------- |
| `__init__()`     | Initialize an object              |
| `__new__()`      | Create an object                  |
| `__str__()`      | String representation             |
| `__repr__()`     | Developer-oriented representation |
| `__add__()`      | `+`                               |
| `__sub__()`      | `-`                               |
| `__mul__()`      | `*`                               |
| `__truediv__()`  | `/`                               |
| `__floordiv__()` | `//`                              |
| `__mod__()`      | `%`                               |
| `__pow__()`      | `**`                              |
| `__eq__()`       | `==`                              |
| `__ne__()`       | `!=`                              |
| `__lt__()`       | `<`                               |
| `__gt__()`       | `>`                               |
| `__le__()`       | `<=`                              |
| `__ge__()`       | `>=`                              |
| `__len__()`      | `len()`                           |
| `__getitem__()`  | `obj[index]`                      |
| `__setitem__()`  | `obj[index] = value`              |
| `__call__()`     | `obj()`                           |
| `__del__()`      | Finalization hook                 |

## Complete Operator Overloading Example

```python
class Calculator:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __str__(self):
        return str(self.value)


num1 = Calculator(20)
num2 = Calculator(10)

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
```

**Output:**

```text
Addition: 30
Subtraction: 10
Multiplication: 200
```

Here, we have customized the behavior of mathematical operators for our own class.

---

# Final Revision: Four Main Pillars of OOP

The four pillars are the most important concepts in Object-Oriented Programming.

## 1. Encapsulation

Combining data and methods into a class and controlling access to internal data.

**Example:** Bank Account.

## 2. Abstraction

Hiding implementation details and showing only essential functionality.

**Example:** ATM machine.

## 3. Inheritance

Allowing one class to acquire attributes and methods from another class.

**Example:** Dog inherits from Animal.

## 4. Polymorphism

Allowing the same interface or operation to behave differently for different objects.

**Example:** Different animals have different `sound()` implementations.

---

# Important Python OOP Syntax Cheat Sheet

| Concept                   | Syntax                 |
| ------------------------- | ---------------------- |
| Class                     | `class Student:`       |
| Object                    | `student = Student()`  |
| Constructor               | `def __init__(self):`  |
| Instance Attribute        | `self.name = "Basit"`  |
| Class Attribute           | `university = "UE"`    |
| Instance Method           | `def display(self):`   |
| Static Method             | `@staticmethod`        |
| Class Method              | `@classmethod`         |
| Abstract Class            | `class A(ABC):`        |
| Abstract Method           | `@abstractmethod`      |
| Inheritance               | `class Child(Parent):` |
| Super Method              | `super()`              |
| Private Attribute         | `self.__name`          |
| Protected-style Attribute | `self._name`           |
| Property                  | `@property`            |
| Setter                    | `@name.setter`         |
| Delete Attribute          | `del object.attribute` |
| Addition Overloading      | `__add__()`            |
| String Representation     | `__str__()`            |

---

# Recommended Learning Order

Follow this order when practicing Python OOP:

1. Classes and Objects
2. Constructors
3. Attributes
4. Instance Methods
5. Class Methods
6. Static Methods
7. Procedural vs OOP
8. Encapsulation
9. Private Attributes and Methods
10. Getter, Setter, and Property
11. Abstraction
12. Inheritance
13. Types of Inheritance
14. `super()`
15. Polymorphism
16. Operator Overloading
17. Dunder Methods
18. `del` Keyword

**Final Advice:** Do not just memorize the definitions. Write each code example yourself, run it, and change the values to understand how Python behaves.

This will give you a strong foundation in Python OOP for backend development, Django/FastAPI, and AI application development.
