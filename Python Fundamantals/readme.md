# Python Programming – Complete Beginner's Guide

## Table of Contents

1. Variables
2. Arithmetic Operators
3. Strings
4. Lists
5. Conditional Statements
6. Loops
7. Functions
8. Dictionaries
9. Tuples
10. Modules in Python
11. Working with JSON
12. File Handling
13. `if __name__ == "__main__"`
14. Exception Handling

---

# 1. Variables

## 1.1 What is a Variable?

A variable is a named storage location used to store data in a program.

In Python, we do not need to declare the data type of a variable. Python automatically determines its type based on the assigned value.

### Example

```python
name = "Basit"
age = 22
height = 5.9
is_student = True

print(name)
print(age)
print(height)
print(is_student)
```

**Output:**

```text
Basit
22
5.9
True
```

### Checking the Data Type

We can use the built-in `type()` function to check the data type of a variable.

```python
name = "Basit"
age = 22
height = 5.9

print(type(name))
print(type(age))
print(type(height))
```

**Output:**

```text
<class 'str'>
<class 'int'>
<class 'float'>
```

## 1.2 Rules for Naming Variables

Python follows these rules when naming variables:

1. A variable name must start with a letter or underscore (`_`).
2. A variable name cannot start with a number.
3. A variable name can contain letters, numbers, and underscores.
4. Variable names are case-sensitive.
5. Python keywords cannot be used as variable names.
6. Spaces are not allowed in variable names.

### Valid Variable Names

```python
name = "Basit"
age = 22
student_name = "Ali"
_name = "Test"
age2 = 25
```

### Invalid Variable Names

```python
2age = 22          # Cannot start with a number
student name = ""  # Spaces are not allowed
class = "BSCS"     # class is a Python keyword
```

### Important: Case Sensitivity

```python
name = "Basit"
Name = "Ali"

print(name)
print(Name)
```

**Output:**

```text
Basit
Ali
```

Python treats `name` and `Name` as two different variables.

---

# 2. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

## 2.1 Two Types of Numbers in Python

Python mainly uses two numeric types for ordinary arithmetic:

**1. Integer (`int`)**

An integer is a whole number without a decimal point.

```python
age = 22
number = -10
quantity = 100

print(type(age))
```

Output:

```text
<class 'int'>
```

**2. Float (`float`)**

A float is a number that contains a decimal point.

```python
price = 99.50
height = 5.9
temperature = -2.5

print(type(price))
```

Output:

```text
<class 'float'>
```

## 2.2 Arithmetic Operators

| Operator | Name           | Example   | Result   |
| -------- | -------------- | --------- | -------- |
| `+`      | Addition       | `10 + 5`  | 15       |
| `-`      | Subtraction    | `10 - 5`  | 5        |
| `*`      | Multiplication | `10 * 5`  | 50       |
| `/`      | Division       | `10 / 3`  | 3.333... |
| `%`      | Modulus        | `10 % 3`  | 1        |
| `//`     | Floor Division | `10 // 3` | 3        |
| `**`     | Exponentiation | `2 ** 3`  | 8        |

### Code Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)
```

**Output:**

```text
13
7
30
3.3333333333333335
1
3
1000
```

## 2.3 Understanding Important Operators

**Modulus (`%`)**

Returns the remainder after division.

```python
print(10 % 3)  # 1
print(15 % 4)  # 3
```

It is commonly used to check whether a number is even or odd.

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Floor Division (`//`)**

Returns the quotient rounded down to the nearest integer.

```python
print(10 // 3)   # 3
print(15 // 4)   # 3
print(-10 // 3)  # -4
```

Remember: Floor division rounds towards negative infinity, not simply towards zero.

**Exponentiation (`**`)\*\*

Used to calculate powers.

```python
print(2 ** 3)  # 8
print(5 ** 2)  # 25
```

## 2.4 The `round()` Function

The `round()` function is used to round a number to a specified number of decimal places.

**Syntax:**

```python
round(number, digits)
```

The second argument is optional.

### Examples

```python
number = 10.56789

print(round(number))
print(round(number, 2))
print(round(number, 3))
```

**Output:**

```text
11
10.57
10.568
```

Python uses round-half-to-even for exact halfway cases, so:

```python
print(round(2.5))  # 2
print(round(3.5))  # 4
```

## 2.5 Operator Precedence: BODMAS or PEMDAS?

Python follows operator precedence rules similar to BODMAS/PEMDAS.

The order of execution is generally:

1. Parentheses `()`
2. Exponentiation `**`
3. Unary operators (`+`, `-`)
4. Multiplication, Division, Floor Division and Modulus (`*`, `/`, `//`, `%`)
5. Addition and Subtraction (`+`, `-`)

Operators with the same precedence are generally evaluated from left to right, except exponentiation, which groups from right to left.

### Example 1

```python
result = 10 + 5 * 2

print(result)
```

**Output:**

```text
20
```

Multiplication is performed first:

```text
10 + 10 = 20
```

### Example 2: Using Parentheses

```python
result = (10 + 5) * 2

print(result)
```

**Output:**

```text
30
```

Parentheses are evaluated first.

### Example 3: Exponentiation

```python
print(2 ** 3 ** 2)
```

**Output:**

```text
512
```

Python evaluates exponentiation from right to left:

```text
2 ** (3 ** 2)
2 ** 9
512
```

---

# 3. Strings

## 3.1 What is a String?

A string is a sequence of characters enclosed in single quotes, double quotes, or triple quotes.

Strings are used to store text.

### Examples

```python
name = "Basit"
city = 'Lahore'
message = "Welcome to Python"

print(name)
print(city)
print(message)
```

## 3.2 Single and Double Quotes

Python supports both single and double quotes.

```python
name = 'Basit'
city = "Lahore"

print(name)
print(city)
```

We can also use one type of quotation mark inside the other.

```python
message = "It's a beautiful day"

print(message)
```

```python
message = 'He said, "Hello!"'

print(message)
```

If we want to use the same quotation mark inside a string, we can escape it using a backslash (`\`).

```python
message = 'It\'s a beautiful day'

print(message)
```

## 3.3 Printing a Whole String

```python
message = "Hello Python"

print(message)
```

Output:

```text
Hello Python
```

## 3.4 Accessing Individual Characters

Python strings use zero-based indexing.

This means the first character has index `0`.

```python
name = "Python"

print(name[0])
print(name[1])
print(name[2])
```

Output:

```text
P
y
t
```

String indexing:

| Character      | P   | y   | t   | h   | o   | n   |
| -------------- | --- | --- | --- | --- | --- | --- |
| Positive index | 0   | 1   | 2   | 3   | 4   | 5   |
| Negative index | -6  | -5  | -4  | -3  | -2  | -1  |

### Negative Indexing

Negative indexing starts from the end of the string.

```python
language = "Python"

print(language[-1])
print(language[-2])
print(language[-3])
```

Output:

```text
n
o
h
```

## 3.5 Accessing Substrings (Slicing)

Slicing allows us to extract a portion of a string.

**Syntax:**

```python
string[start:end:step]
```

- `start`: Starting index (included).
- `end`: Ending index (excluded).
- `step`: Number of positions to move each time.

### Case 1: Extract a Range

```python
name = "Python"

print(name[0:3])
```

Output:

```text
Pyt
```

Index 3 is excluded.

### Case 2: Starting from Index 0

```python
name = "Python"

print(name[:4])
```

Output:

```text
Pyth
```

### Case 3: Going Until the End

```python
name = "Python"

print(name[2:])
```

Output:

```text
thon
```

### Case 4: Copying the Whole String

```python
name = "Python"

print(name[:])
```

Output:

```text
Python
```

### Case 5: Using Negative Indexing

```python
name = "Python"

print(name[-4:-1])
```

Output:

```text
tho
```

### Case 6: Using Step

```python
name = "Python"

print(name[::2])
```

Output:

```text
Pto
```

### Case 7: Reversing a String

```python
name = "Python"

print(name[::-1])
```

Output:

```text
nohtyP
```

## 3.6 Strings Are Immutable

Immutable means that an object cannot be modified after it has been created.

In Python, strings are immutable.

### Example

```python
name = "Python"

name[0] = "J"  # Error
```

This produces a `TypeError`.

We cannot directly change a character in an existing string.

However, we can create a new string.

```python
name = "Python"

name = "J" + name[1:]

print(name)
```

Output:

```text
Jython
```

## 3.7 String Concatenation

Concatenation means joining two or more strings together.

We use the `+` operator.

```python
first_name = "Basit"
last_name = "Ali"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Basit Ali
```

We can also use the `*` operator to repeat a string.

```python
print("Hello " * 3)
```

Output:

```text
Hello Hello Hello
```

### Using f-strings

An f-string allows us to insert variables directly inside a string.

```python
name = "Basit"
age = 22

message = f"My name is {name} and I am {age} years old."

print(message)
```

Output:

```text
My name is Basit and I am 22 years old.
```

## 3.8 Multiline Strings

We can create a multiline string using triple single quotes or triple double quotes.

```python
message = """Hello,
Welcome to Python.
We are learning strings."""

print(message)
```

Output:

```text
Hello,
Welcome to Python.
We are learning strings.
```

## 3.9 Common String Functions and Methods

| Method         | Purpose                        | Example                      |
| -------------- | ------------------------------ | ---------------------------- |
| `len()`        | Returns string length          | `len("Python")`              |
| `upper()`      | Converts to uppercase          | `"hello".upper()`            |
| `lower()`      | Converts to lowercase          | `"HELLO".lower()`            |
| `capitalize()` | Capitalizes first character    | `"hello world".capitalize()` |
| `title()`      | Capitalizes each word          | `"hello world".title()`      |
| `strip()`      | Removes surrounding whitespace | `" hello ".strip()`          |
| `replace()`    | Replaces a substring           | `"Hello".replace("H", "J")`  |
| `find()`       | Finds the first occurrence     | `"Python".find("t")`         |
| `count()`      | Counts occurrences             | `"banana".count("a")`        |
| `startswith()` | Checks starting characters     | `"Python".startswith("Py")`  |
| `endswith()`   | Checks ending characters       | `"Python".endswith("on")`    |
| `split()`      | Splits string into a list      | `"a,b".split(",")`           |
| `join()`       | Joins strings from an iterable | `"-".join(["a", "b"])`       |

### Example

```python
message = "  hello python  "

print(message.upper())
print(message.lower())
print(message.strip())
print(message.replace("python", "world"))
print(len(message))
```

Remember: String methods generally return a new string. They do not modify the original string.

---

# 4. Lists

## 4.1 Why Do We Need Lists?

Suppose we want to store five student names.

Without a list:

```python
student1 = "Ali"
student2 = "Ahmed"
student3 = "Basit"
student4 = "Hassan"
student5 = "Usman"
```

This approach becomes difficult when we have hundreds or thousands of students.

Instead, we can store all names inside a single list.

## 4.2 What is a List?

A list is an ordered and mutable collection of items.

- Ordered: Items maintain their positions.
- Mutable: We can change, add, or remove items.
- Allows duplicate values.
- Can store different data types.

### Creating a List

```python
students = ["Ali", "Ahmed", "Basit", "Hassan"]

numbers = [10, 20, 30, 40]

mixed = ["Basit", 22, 5.9, True]
```

## 4.3 Printing a Whole List

```python
students = ["Ali", "Ahmed", "Basit"]

print(students)
```

Output:

```text
['Ali', 'Ahmed', 'Basit']
```

## 4.4 Accessing Items in a List

Lists use zero-based indexing.

```python
students = ["Ali", "Ahmed", "Basit", "Hassan"]

print(students[0])
print(students[1])
print(students[2])
```

Output:

```text
Ali
Ahmed
Basit
```

## 4.5 Changing an Item in a List

Lists are mutable, so we can change their values.

```python
students = ["Ali", "Ahmed", "Basit"]

students[1] = "Usman"

print(students)
```

Output:

```text
['Ali', 'Usman', 'Basit']
```

## 4.6 Accessing a Range of Items

We can use slicing to access multiple items.

**Syntax:**

```python
list[start:end:step]
```

### Example 1

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

### Example 2: Starting from Beginning

```python
print(numbers[:3])
```

Output:

```text
[10, 20, 30]
```

### Example 3: Going Until the End

```python
print(numbers[2:])
```

Output:

```text
[30, 40, 50]
```

## 4.7 Negative Indexing

Negative indexing starts from the last item.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[-1])
print(numbers[-2])
```

Output:

```text
50
40
```

## 4.8 Built-in List Methods

Python provides several built-in list methods.

| Method      | Purpose                                   |
| ----------- | ----------------------------------------- |
| `append()`  | Adds an item at the end                   |
| `insert()`  | Adds an item at a specific index          |
| `extend()`  | Adds multiple items from another iterable |
| `remove()`  | Removes the first matching item           |
| `pop()`     | Removes and returns an item               |
| `clear()`   | Removes all items                         |
| `index()`   | Returns the index of an item              |
| `count()`   | Counts occurrences of an item             |
| `sort()`    | Sorts the list                            |
| `reverse()` | Reverses the list                         |
| `copy()`    | Creates a shallow copy of the list        |

### append()

Adds one item at the end.

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

### insert()

Adds an item at a specific index.

```python
numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)
```

Output:

```text
[10, 15, 20, 30]
```

### extend()

Adds multiple items from another iterable.

```python
numbers = [10, 20]

numbers.extend([30, 40])

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

### remove()

Removes the first matching value.

```python
numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)
```

Output:

```text
[10, 30, 20]
```

### pop()

Removes and returns an item.

```python
numbers = [10, 20, 30]

removed = numbers.pop()

print(removed)
print(numbers)
```

Output:

```text
30
[10, 20]
```

We can also provide an index:

```python
numbers = [10, 20, 30]

numbers.pop(1)

print(numbers)
```

Output:

```text
[10, 30]
```

### clear()

```python
numbers = [10, 20, 30]

numbers.clear()

print(numbers)
```

Output:

```text
[]
```

### index()

```python
numbers = [10, 20, 30]

print(numbers.index(20))
```

Output:

```text
1
```

### count()

```python
numbers = [10, 20, 20, 30]

print(numbers.count(20))
```

Output:

```text
2
```

### sort()

```python
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

For descending order:

```python
numbers.sort(reverse=True)

print(numbers)
```

Output:

```text
[40, 30, 20, 10]
```

### reverse()

```python
numbers = [10, 20, 30]

numbers.reverse()

print(numbers)
```

Output:

```text
[30, 20, 10]
```

### copy()

```python
numbers = [10, 20, 30]

new_numbers = numbers.copy()

print(new_numbers)
```

## 4.9 Joining Two Lists

We can join two lists using the `+` operator.

```python
list1 = [10, 20, 30]
list2 = [40, 50, 60]

result = list1 + list2

print(result)
```

Output:

```text
[10, 20, 30, 40, 50, 60]
```

We can also use `extend()`.

```python
list1 = [10, 20, 30]
list2 = [40, 50, 60]

list1.extend(list2)

print(list1)
```

## 4.10 The `in` Operator

The `in` operator checks whether an item exists in a list.

It returns `True` or `False`.

```python
students = ["Ali", "Ahmed", "Basit"]

print("Basit" in students)
print("Usman" in students)
```

Output:

```text
True
False
```

We can also use it with conditional statements.

```python
students = ["Ali", "Ahmed", "Basit"]

if "Basit" in students:
    print("Student found")
else:
    print("Student not found")
```

---

# 5. Conditional Statements

Conditional statements allow a program to make decisions based on conditions.

For example, we can check whether a student has passed or failed an examination.

## 5.1 Relational (Comparison) Operators

Relational operators compare two values and return either `True` or `False`.

| Operator | Meaning                  | Example    |
| -------- | ------------------------ | ---------- |
| `==`     | Equal to                 | `10 == 10` |
| `!=`     | Not equal to             | `10 != 5`  |
| `>`      | Greater than             | `10 > 5`   |
| `<`      | Less than                | `5 < 10`   |
| `>=`     | Greater than or equal to | `10 >= 10` |
| `<=`     | Less than or equal to    | `5 <= 10`  |

### Example

```python
a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
```

Output:

```text
False
True
True
False
```

## 5.2 Logical Operators

Logical operators are used to combine multiple conditions.

Python provides three main logical operators.

| Operator | Meaning                                |
| -------- | -------------------------------------- |
| `and`    | True if both conditions are True       |
| `or`     | True if at least one condition is True |
| `not`    | Reverses the result                    |

### AND Operator

Both conditions must be True.

```python
age = 22
has_id = True

if age >= 18 and has_id:
    print("Allowed")
else:
    print("Not allowed")
```

### OR Operator

At least one condition must be True.

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Working day")
```

### NOT Operator

Reverses the result.

```python
is_raining = False

if not is_raining:
    print("You can go outside")
```

## 5.3 if Statement

An `if` statement executes a block of code only when its condition is True.

**Syntax:**

```python
if condition:
    # Code to execute
```

### Example

```python
age = 20

if age >= 18:
    print("You are eligible to vote")
```

## 5.4 if-else Statement

The `else` block executes when the `if` condition is False.

**Syntax:**

```python
if condition:
    # True block
else:
    # False block
```

### Example

```python
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

Output:

```text
Odd number
```

## 5.5 if-elif-else Statement

We use `elif` when we need to check multiple conditions.

**Syntax:**

```python
if condition1:
    # Code
elif condition2:
    # Code
elif condition3:
    # Code
else:
    # Default code
```

### Example

```python
marks = 85

if marks >= 90:
    print("Grade A+")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Fail")
```

Output:

```text
Grade A
```

Python checks the conditions from top to bottom. Once a condition is True, its block executes and the remaining branches are skipped.

## 5.6 Switch Statement in Python

Unlike languages such as C++, Java, and JavaScript, traditional Python does not use a `switch` statement.

Python provides `match-case` starting from Python 3.10.

### Example

```python
day = 2

match day:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case _:
        print("Invalid day")
```

Output:

```text
Tuesday
```

Here:

- `match` checks the value.
- `case` defines possible patterns.
- `_` acts as a wildcard/default case.

---

# 6. Loops

Loops allow us to execute a block of code repeatedly.

Suppose we want to print numbers from 1 to 100.

Without loops, we would need to write 100 print statements.

Loops solve this problem.

Python provides two main types of loops:

1. `for` loop
2. `while` loop

## 6.1 For Loop

A `for` loop is used to iterate over a sequence, such as a list, string, tuple, or range.

**Syntax:**

```python
for variable in sequence:
    # Code to execute
```

### Example 1: Iterating Over a List

```python
students = ["Ali", "Ahmed", "Basit"]

for student in students:
    print(student)
```

Output:

```text
Ali
Ahmed
Basit
```

### Example 2: Iterating Over a String

```python
name = "Python"

for character in name:
    print(character)
```

Output:

```text
P
y
t
h
o
n
```

## 6.2 range() Function

The `range()` function generates a sequence of numbers.

It is commonly used with `for` loops.

**Syntax:**

```python
range(start, stop, step)
```

- `start`: Starting number (included).
- `stop`: Ending number (excluded).
- `step`: Difference between numbers.

### Case 1: range(stop)

Starting from 0 by default.

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

### Case 2: range(start, stop)

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

### Case 3: range(start, stop, step)

```python
for i in range(1, 10, 2):
    print(i)
```

Output:

```text
1
3
5
7
9
```

### Case 4: Counting Backwards

Use a negative step.

```python
for i in range(5, 0, -1):
    print(i)
```

Output:

```text
5
4
3
2
1
```

### Case 5: Even Numbers

```python
for i in range(2, 11, 2):
    print(i)
```

Output:

```text
2
4
6
8
10
```

## 6.3 break Keyword

The `break` keyword immediately terminates the loop.

### Example

```python
for i in range(1, 6):

    if i == 3:
        break

    print(i)
```

Output:

```text
1
2
```

When `i` becomes 3, the loop terminates.

## 6.4 continue Keyword

The `continue` keyword skips the current iteration and moves to the next iteration.

### Example

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

When `i` becomes 3, Python skips that iteration.

## 6.5 while Loop

A `while` loop executes repeatedly as long as its condition remains True.

**Syntax:**

```python
while condition:
    # Code to execute
```

### Example

```python
number = 1

while number <= 5:

    print(number)

    number += 1
```

Output:

```text
1
2
3
4
5
```

**Important:** Always make sure that the condition eventually becomes False. Otherwise, you may create an infinite loop.

### Example of an Infinite Loop

```python
while True:
    print("Hello")
```

This loop continues until it is interrupted or terminated using a `break` statement.

## 6.6 Nested Loops

A nested loop means placing one loop inside another loop.

### Example 1: Nested For Loop

```python
for i in range(1, 4):

    for j in range(1, 4):

        print(i, j)
```

Output:

```text
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

The inner loop completes all its iterations for every single iteration of the outer loop.

### Example 2: Printing a Pattern

```python
for i in range(1, 5):

    for j in range(i):

        print("*", end="")

    print()
```

Output:

```text
*
**
***
****
```

---

# 7. Functions

## 7.1 Why Do We Need Functions?

Suppose we want to calculate the sum of two numbers at multiple places in our program.

Without functions:

```python
a = 10
b = 20
print(a + b)

x = 30
y = 40
print(x + y)

p = 50
q = 60
print(p + q)
```

We are repeating the same logic again and again.

This creates several problems:

1. Code duplication.
2. Difficult maintenance.
3. Difficult debugging.
4. Less readable code.

**Solution: Functions**

A function allows us to write a block of reusable code once and execute it whenever needed.

## 7.2 What is a Function?

A function is a reusable block of code that performs a specific task.

Python provides built-in functions such as:

```python
print()
len()
type()
sum()
max()
min()
```

We can also create our own functions. These are called user-defined functions.

## 7.3 Defining and Calling a Function

We use the `def` keyword to define a function.

**Syntax:**

```python
def function_name():
    # Function body
```

To execute the function, we call it using its name.

### Example

```python
def greet():
    print("Hello, welcome to Python")

greet()
```

Output:

```text
Hello, welcome to Python
```

## 7.4 Functions with Parameters and Arguments

A parameter is a variable defined in the function definition.

An argument is the actual value passed when calling the function.

### Example

```python
def greet(name):  # name is a parameter

    print("Hello", name)


greet("Basit")  # "Basit" is an argument
```

Output:

```text
Hello Basit
```

## 7.5 return Statement

The `return` statement sends a result back to the caller.

### Example

```python
def add(a, b):

    result = a + b

    return result


answer = add(10, 20)

print(answer)
```

Output:

```text
30
```

**Difference between print() and return:**

- `print()` displays information on the screen.
- `return` sends a value back to the caller so it can be stored or used in further calculations.

### Example

```python
def add(a, b):
    return a + b


result = add(10, 20)

final_result = result * 2

print(final_result)
```

Output:

```text
60
```

## 7.6 Types of Function Arguments

Python supports several ways of passing arguments.

### 1. Positional Arguments

Values are passed according to their positions.

```python
def student(name, age):

    print(name)
    print(age)


student("Basit", 22)
```

Output:

```text
Basit
22
```

The first argument goes to `name`, and the second goes to `age`.

### 2. Keyword (Named) Arguments

Values are passed using parameter names.

```python
def student(name, age):

    print(name)
    print(age)


student(age=22, name="Basit")
```

Output:

```text
Basit
22
```

The order does not matter when using keyword arguments.

### 3. Default Arguments

A default argument has a predefined value.

If the caller does not provide a value, Python uses the default value.

```python
def greet(name="Guest"):

    print("Hello", name)


greet("Basit")
greet()
```

Output:

```text
Hello Basit
Hello Guest
```

**Important:** Parameters with default values should come after parameters without default values.

```python
# Correct
def student(name, age=20):
    pass

# Incorrect
# def student(age=20, name):
#     pass
```

### 4. Variable-Length Positional Arguments (\*args)

Sometimes we do not know how many arguments will be passed.

We can use `*args` to accept multiple positional arguments.

```python
def add_numbers(*args):

    total = 0

    for number in args:
        total += number

    return total


print(add_numbers(10, 20))
print(add_numbers(10, 20, 30, 40))
```

Output:

```text
30
100
```

`args` is a tuple containing the supplied positional arguments.

### 5. Variable-Length Keyword Arguments (\*\*kwargs)

We use `**kwargs` to accept multiple keyword arguments.

```python
def student_details(**kwargs):

    for key, value in kwargs.items():

        print(key, ":", value)


student_details(name="Basit", age=22, city="Lahore")
```

Output:

```text
name : Basit
age : 22
city : Lahore
```

`kwargs` is a dictionary.

## 7.7 Local and Global Variables

### Local Variable

A local variable is created inside a function and is normally accessible only within that function.

```python
def greet():

    message = "Hello Python"

    print(message)


greet()

# print(message)  # NameError
```

Here, `message` is a local variable.

### Global Variable

A global variable is defined outside a function and can normally be accessed inside functions.

```python
name = "Basit"


def greet():

    print(name)


greet()
```

Output:

```text
Basit
```

### Modifying a Global Variable

To assign a new value to a global variable from inside a function, use the `global` keyword.

```python
count = 10


def update_count():

    global count

    count = 20


update_count()

print(count)
```

Output:

```text
20
```

**Important:** Avoid using global variables unnecessarily. Passing values through function parameters and returning results generally makes code easier to maintain.

## 7.8 Documentation String (Docstring)

A docstring is a string written at the beginning of a function, class, or module to explain its purpose.

We use triple quotes for docstrings.

### Example

```python
def add(a, b):
    """
    This function takes two numbers
    and returns their sum.
    """

    return a + b


print(add(10, 20))
```

We can access the documentation using:

```python
print(add.__doc__)
```

Output:

```text
    This function takes two numbers
    and returns their sum.
```

Docstrings help developers understand what a function does.

---

# 8. Dictionaries

## 8.1 What is a Dictionary?

A dictionary is a collection of key-value pairs.

It is used to store data in a structured format.

For example, instead of storing student information in separate variables, we can store everything in a dictionary.

### Example

```python
student = {
    "name": "Basit",
    "age": 22,
    "city": "Lahore"
}

print(student)
```

Output:

```text
{'name': 'Basit', 'age': 22, 'city': 'Lahore'}
```

## 8.2 Dictionary Syntax

```python
dictionary_name = {
    "key1": "value1",
    "key2": "value2"
}
```

Important properties:

1. Dictionaries store data as key-value pairs.
2. Keys must be unique.
3. Values can be duplicated.
4. Dictionaries are mutable.
5. Keys must be hashable (commonly strings, numbers, or tuples containing hashable values).
6. Dictionaries preserve insertion order in modern Python.

## 8.3 Accessing Values

We can access a value using its key.

```python
student = {
    "name": "Basit",
    "age": 22,
    "city": "Lahore"
}

print(student["name"])
print(student["age"])
```

Output:

```text
Basit
22
```

### Using get()

We can also use the `get()` method.

```python
print(student.get("name"))
print(student.get("email"))
```

Output:

```text
Basit
None
```

The main difference:

- `dictionary["key"]` raises a `KeyError` if the key does not exist.
- `dictionary.get("key")` returns `None` by default if the key does not exist.

We can provide a default value:

```python
print(student.get("email", "Not available"))
```

Output:

```text
Not available
```

## 8.4 Accessing Dictionary Elements

A dictionary element consists of a key and its associated value.

We can access all keys, values, or key-value pairs.

### keys()

```python
print(student.keys())
```

### values()

```python
print(student.values())
```

### items()

```python
print(student.items())
```

## 8.5 Adding an Entry

We can add a new key-value pair using assignment.

```python
student = {
    "name": "Basit",
    "age": 22
}

student["city"] = "Lahore"

print(student)
```

Output:

```text
{'name': 'Basit', 'age': 22, 'city': 'Lahore'}
```

## 8.6 Updating an Existing Entry

```python
student = {
    "name": "Basit",
    "age": 22
}

student["age"] = 23

print(student)
```

Output:

```text
{'name': 'Basit', 'age': 23}
```

## 8.7 Deleting an Entry

### Using pop()

Removes an entry using its key.

```python
student = {
    "name": "Basit",
    "age": 22,
    "city": "Lahore"
}

student.pop("age")

print(student)
```

### Using del

```python
del student["city"]

print(student)
```

### Using clear()

Removes all entries.

```python
student.clear()

print(student)
```

Output:

```text
{}
```

## 8.8 Printing All Keys and Values

We can use a `for` loop with the `items()` method.

```python
student = {
    "name": "Basit",
    "age": 22,
    "city": "Lahore"
}

for key, value in student.items():

    print(key, ":", value)
```

Output:

```text
name : Basit
age : 22
city : Lahore
```

---

# 9. Tuples

## 9.1 What is a Tuple?

A tuple is an ordered collection of items.

It is similar to a list, but the main difference is that tuples are immutable.

Tuples are created using parentheses `()`.

### Example

```python
student = ("Basit", 22, "Lahore")

print(student)
```

Output:

```text
('Basit', 22, 'Lahore')
```

## 9.2 Accessing Tuple Items

Tuples support indexing and slicing, just like lists.

```python
student = ("Basit", 22, "Lahore")

print(student[0])
print(student[1])
print(student[-1])
```

Output:

```text
Basit
22
Lahore
```

## 9.3 Tuples Are Immutable

Once a tuple is created, its items cannot be changed, added, or removed.

```python
numbers = (10, 20, 30)

# numbers[0] = 100  # TypeError
```

## 9.4 Difference Between List and Tuple

| Feature           | List         | Tuple         |
| ----------------- | ------------ | ------------- |
| Syntax            | `[]`         | `()`          |
| Mutable           | Yes          | No            |
| Ordered           | Yes          | Yes           |
| Allows duplicates | Yes          | Yes           |
| Indexing          | Yes          | Yes           |
| Slicing           | Yes          | Yes           |
| Methods           | More methods | Fewer methods |

### When to Use a List?

Use a list when you need to modify the collection.

```python
students = ["Ali", "Ahmed"]

students.append("Basit")
```

### When to Use a Tuple?

Use a tuple when the collection should not be modified.

```python
coordinates = (10, 20)
```

## 9.5 Single-Element Tuple

A single-element tuple requires a comma.

```python
numbers = (10,)

print(type(numbers))
```

Output:

```text
<class 'tuple'>
```

Without the comma:

```python
numbers = (10,)

# Without comma: (10) is an integer, not a tuple.
```

---

# 10. Modules in Python

## 10.1 What is a Module?

A module is a Python file containing reusable code, such as functions, variables, and classes.

Modules allow us to organize code and reuse functionality across different programs.

For example, Python provides built-in modules such as:

- `math`
- `random`
- `datetime`
- `os`
- `json`

## 10.2 How to Import a Module

We use the `import` keyword.

### Example: math Module

```python
import math

print(math.sqrt(25))
print(math.pi)
```

Output:

```text
5.0
3.141592653589793
```

### Importing a Specific Function

```python
from math import sqrt

print(sqrt(25))
```

### Using an Alias

We can give a module a shorter name using `as`.

```python
import math as m

print(m.sqrt(25))
```

## 10.3 Installing Third-Party Modules

Python provides a package manager called `pip`.

We use `pip` to install external packages.

### Installing a Package

```bash
pip install requests
```

Another example:

```bash
pip install matplotlib
```

### Using an Installed Package

```python
import requests

response = requests.get("https://example.com")

print(response.status_code)
```

**Note:** `pip` installs packages into a Python environment. In some systems, you may need:

```bash
python -m pip install requests
```

## 10.4 Creating a Custom Module

We can create our own Python module.

Suppose we have two files:

```text
project/
│
├── main.py
└── calculator.py
```

### Step 1: Create calculator.py

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b
```

### Step 2: Import the Module in main.py

```python
import calculator

print(calculator.add(10, 20))

print(calculator.subtract(20, 5))

print(calculator.multiply(5, 5))
```

Output:

```text
30
15
25
```

We have successfully created and imported our own module.

---

# 11. Working with JSON in Python

## 11.1 What is JSON?

JSON stands for JavaScript Object Notation.

It is a lightweight data format used to store and exchange data between applications.

JSON is commonly used in REST APIs.

### Example JSON Data

```json
{
  "name": "Basit",
  "age": 22,
  "city": "Lahore",
  "skills": ["Python", "JavaScript", "React"]
}
```

JSON supports these data types:

| JSON Type | Example             |
| --------- | ------------------- |
| String    | `"Basit"`           |
| Number    | `22`                |
| Boolean   | `true`              |
| Null      | `null`              |
| Array     | `[10, 20, 30]`      |
| Object    | `{"name": "Basit"}` |

## 11.2 JSON Module in Python

Python provides a built-in module called `json`.

We do not need to install it separately.

```python
import json
```

## 11.3 Understanding json.dumps()

The `json.dumps()` function converts a Python object into a JSON-formatted string.

**Python Object → JSON String**

```python
import json

student = {
    "name": "Basit",
    "age": 22,
    "city": "Lahore"
}

json_data = json.dumps(student)

print(json_data)
print(type(json_data))
```

Output:

```text
{"name": "Basit", "age": 22, "city": "Lahore"}
<class 'str'>
```

We can also format the output using indentation.

```python
json_data = json.dumps(student, indent=4)

print(json_data)
```

## 11.4 Understanding json.loads()

The `json.loads()` function converts a JSON string into a Python object.

**JSON String → Python Object**

```python
import json

json_data = '{"name": "Basit", "age": 22}'

student = json.loads(json_data)

print(student)
print(type(student))
```

Output:

```text
{'name': 'Basit', 'age': 22}
<class 'dict'>
```

We can access the values like a normal dictionary.

```python
print(student["name"])
print(student["age"])
```

## 11.5 Understanding json.dump()

The `json.dump()` function writes a Python object directly into a JSON file.

```python
import json

student = {
    "name": "Basit",
    "age": 22,
    "city": "Lahore"
}

with open("student.json", "w") as file:

    json.dump(student, file, indent=4)
```

This creates a file named `student.json`.

## 11.6 Understanding json.load()

The `json.load()` function reads JSON data from a file and converts it into a Python object.

```python
import json

with open("student.json", "r") as file:

    student = json.load(file)


print(student)
print(student["name"])
```

## 11.7 Difference Between JSON Functions

| Function       | Purpose                      |
| -------------- | ---------------------------- |
| `json.dumps()` | Python object to JSON string |
| `json.loads()` | JSON string to Python object |
| `json.dump()`  | Python object to JSON file   |
| `json.load()`  | JSON file to Python object   |

---

# 12. File Handling in Python

## 12.1 What is File Handling?

File handling allows a program to create, read, write, and modify files stored on a computer.

For example:

- Saving student information.
- Reading configuration files.
- Writing application logs.
- Storing user data.
- Reading text files.

Python provides the built-in `open()` function for file handling.

## 12.2 Absolute Path and Relative Path

### Absolute Path

An absolute path specifies the complete location of a file from the root of the filesystem.

Example on Windows:

```text
C:\Users\Basit\Desktop\Python\student.txt
```

Example on Linux:

```text
/home/basit/Desktop/Python/student.txt
```

### Relative Path

A relative path specifies a file location relative to the current working directory.

Example:

```text
student.txt
```

Or:

```text
files/student.txt
```

### Important Difference

| Absolute Path                                 | Relative Path                                  |
| --------------------------------------------- | ---------------------------------------------- |
| Complete file location                        | Location relative to current working directory |
| Usually starts from a root directory or drive | Depends on current working directory           |
| Less dependent on where the script is run     | Can be affected by where the script is run     |

You can check the current working directory using:

```python
import os

print(os.getcwd())
```

## 12.3 Creating a New File and Writing to It

We use `open()` with write mode (`w`).

**Syntax:**

```python
file = open("filename.txt", "w")
```

### Example

```python
file = open("student.txt", "w")

file.write("My name is Basit")

file.close()
```

This creates `student.txt` if it does not exist.

If the file already exists, write mode overwrites its existing contents.

## 12.4 Append Mode

Append mode (`a`) adds new content at the end of an existing file.

It does not remove the previous content.

```python
file = open("student.txt", "a")

file.write("\nI am learning Python")

file.close()
```

If the file does not exist, append mode creates it.

## 12.5 Reading a File

We use read mode (`r`) to read file contents.

```python
file = open("student.txt", "r")

content = file.read()

print(content)

file.close()
```

## 12.6 Reading a File Line by Line

We can use a `for` loop to read a file line by line.

```python
file = open("student.txt", "r")

for line in file:

    print(line)

file.close()
```

If you want to remove extra newline characters when printing:

```python
file = open("student.txt", "r")

for line in file:

    print(line.strip())

file.close()
```

## 12.7 Other Reading Methods

### read()

Reads the entire file.

```python
content = file.read()
```

### readline()

Reads one line at a time.

```python
line = file.readline()
```

### readlines()

Reads all lines and returns them as a list.

```python
lines = file.readlines()
```

## 12.8 Understanding split() with Files

The `split()` method divides a string into a list.

It is useful when reading structured text files.

### Example

Suppose `student.txt` contains:

```text
Basit,22,Lahore
Ali,23,Karachi
Ahmed,21,Islamabad
```

Python code:

```python
file = open("student.txt", "r")

for line in file:

    data = line.strip().split(",")

    print(data)

file.close()
```

Output:

```text
['Basit', '22', 'Lahore']
['Ali', '23', 'Karachi']
['Ahmed', '21', 'Islamabad']
```

We can access individual values:

```python
file = open("student.txt", "r")

for line in file:

    data = line.strip().split(",")

    name = data[0]
    age = data[1]
    city = data[2]

    print("Name:", name)
    print("Age:", age)
    print("City:", city)

file.close()
```

## 12.9 File Opening Modes

Python provides different file modes.

| Mode | Purpose                                       |
| ---- | --------------------------------------------- |
| `r`  | Read an existing file                         |
| `w`  | Write; creates or overwrites a file           |
| `a`  | Append; creates or adds to a file             |
| `x`  | Create a new file; fails if it already exists |
| `r+` | Read and write an existing file               |
| `w+` | Write and read; overwrites or creates a file  |
| `a+` | Append and read                               |
| `rb` | Read in binary mode                           |
| `wb` | Write in binary mode                          |
| `ab` | Append in binary mode                         |

## 12.10 The with Statement

The `with` statement is the recommended way to work with files.

It automatically closes the file after the block finishes, even if an exception occurs.

### Without with Statement

```python
file = open("student.txt", "r")

content = file.read()

print(content)

file.close()
```

### With Statement

```python
with open("student.txt", "r") as file:

    content = file.read()

    print(content)
```

We do not need to call `file.close()` manually.

### Writing with with Statement

```python
with open("student.txt", "w") as file:

    file.write("Learning Python")
```

### Appending with with Statement

```python
with open("student.txt", "a") as file:

    file.write("\nFile handling is easy")
```

**Best Practice:** Prefer the `with` statement whenever you work with files.

---

# 13. if **name** == "**main**"

## 13.1 What Does It Mean?

In Python, every module has a special built-in variable called `__name__`.

Its value depends on how the Python file is being executed.

There are two main cases:

**Case 1: Running a Python File Directly**

When we run a Python file directly, Python sets:

```python
__name__ = "__main__"
```

**Case 2: Importing a Python File as a Module**

When another Python file imports it, `__name__` contains the module's name.

## 13.2 Example Without if **name**

Suppose we have two files:

```text
project/
│
├── main.py
└── calculator.py
```

### calculator.py

```python
def add(a, b):

    return a + b


print("Calculator module executed")
```

### main.py

```python
import calculator

print(calculator.add(10, 20))
```

Output:

```text
Calculator module executed
30
```

The problem is that the print statement inside `calculator.py` executes even when we only want to import its function.

## 13.3 Solution: if **name** == "**main**"

We can prevent certain code from executing during imports.

### calculator.py

```python
def add(a, b):

    return a + b


if __name__ == "__main__":

    print("Calculator module executed directly")
```

### main.py

```python
import calculator

print(calculator.add(10, 20))
```

Output:

```text
30
```

The message is not printed because `calculator.py` is being imported rather than executed directly.

However, if we run `calculator.py` directly:

```bash
python calculator.py
```

Output:

```text
Calculator module executed directly
```

## 13.4 Why Do We Use It?

It is useful for:

1. Preventing code from executing during imports.
2. Separating reusable functions from execution code.
3. Creating clean and organized Python applications.
4. Providing an entry point for a Python script.

### Recommended Structure

```python
def main():

    print("Application started")


if __name__ == "__main__":

    main()
```

This is a common structure in professional Python applications.

---

# 14. Exception Handling

## 14.1 What is an Exception?

An exception is an error that occurs during program execution and interrupts the normal flow of the program.

For example:

- Dividing a number by zero.
- Accessing an invalid list index.
- Converting an invalid string into an integer.
- Opening a file that does not exist.

### Example Without Exception Handling

```python
a = 10
b = 0

result = a / b

print(result)

print("Program completed")
```

Output:

```text
ZeroDivisionError
```

The program stops before printing `"Program completed"`.

## 14.2 Why Do We Need Exception Handling?

Exception handling allows us to handle runtime errors without unexpectedly terminating the program.

Python provides:

- `try`
- `except`
- `else`
- `finally`

## 14.3 try-except

The code that may generate an exception is placed inside the `try` block.

The `except` block handles the exception.

### Syntax

```python
try:

    # Code that may generate an exception

except:

    # Code to handle the exception
```

### Example

```python
try:

    a = 10
    b = 0

    result = a / b

    print(result)

except:

    print("Something went wrong")

print("Program completed")
```

Output:

```text
Something went wrong
Program completed
```

## 14.4 Handling Specific Exceptions

It is better to catch specific exceptions instead of using a general `except` block.

### Example: ZeroDivisionError

```python
try:

    a = 10
    b = 0

    result = a / b

    print(result)

except ZeroDivisionError:

    print("Cannot divide by zero")
```

### Example: ValueError

```python
try:

    age = int("abc")

except ValueError:

    print("Please enter a valid number")
```

### Example: IndexError

```python
try:

    numbers = [10, 20, 30]

    print(numbers[5])

except IndexError:

    print("Invalid list index")
```

## 14.5 Handling Multiple Exceptions

Sometimes different operations can generate different exceptions.

We can handle them separately using multiple `except` blocks.

### Example

```python
try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)


except ValueError:

    print("Please enter valid numbers")


except ZeroDivisionError:

    print("Cannot divide by zero")


except Exception as error:

    print("Unexpected error:", error)
```

Here:

- `ValueError`: Handles invalid input conversion.
- `ZeroDivisionError`: Handles division by zero.
- `Exception`: Handles other exceptions not caught by the previous blocks.

**Important:** Place specific exceptions before general exceptions.

## 14.6 else Block

The `else` block executes only when no exception occurs inside the `try` block.

### Example

```python
try:

    a = 10
    b = 2

    result = a / b

except ZeroDivisionError:

    print("Cannot divide by zero")

else:

    print("Result:", result)
```

Output:

```text
Result: 5.0
```

## 14.7 finally Block

The `finally` block executes whether an exception occurs or not, provided normal control flow reaches it.

It is commonly used for cleanup operations.

### Example

```python
try:

    result = 10 / 2

    print(result)

except ZeroDivisionError:

    print("Cannot divide by zero")

finally:

    print("Execution completed")
```

Output:

```text
5.0
Execution completed
```

## 14.8 Complete Exception Handling Example

```python
try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b


except ValueError:

    print("Invalid input. Enter numbers only.")


except ZeroDivisionError:

    print("Cannot divide by zero.")


except Exception as error:

    print("Unexpected error:", error)


else:

    print("Result:", result)


finally:

    print("Program execution finished.")
```

## 14.9 Raising Exceptions

We can manually generate an exception using the `raise` keyword.

### Example

```python
age = 15

if age < 18:

    raise ValueError("Age must be at least 18")

print("Eligible")
```

This raises a `ValueError` when the age is below 18.

---

# Final Revision – Important Python Concepts

| Topic         | Important Concepts                                                |
| ------------- | ----------------------------------------------------------------- |
| Variables     | Assignment, naming rules, data types                              |
| Arithmetic    | Operators, int, float, precedence, round()                        |
| Strings       | Indexing, slicing, immutability, methods                          |
| Lists         | Indexing, slicing, mutability, list methods                       |
| Conditions    | Comparison operators, logical operators, if-elif-else, match-case |
| Loops         | for, while, range(), break, continue, nested loops                |
| Functions     | def, parameters, arguments, return, scope, docstrings             |
| Dictionaries  | Key-value pairs, keys(), values(), items()                        |
| Tuples        | Ordered, immutable, indexing                                      |
| Modules       | import, pip, custom modules                                       |
| JSON          | dumps(), loads(), dump(), load()                                  |
| File Handling | Paths, modes, read(), write(), append(), with                     |
| Main Guard    | if **name** == "**main**"                                         |
| Exceptions    | try, except, else, finally, raise                                 |

## Recommended Practice Order

After studying each topic, write small programs yourself.

1. Create a student information program using variables.
2. Build a simple calculator using arithmetic operators.
3. Write a program to reverse a string.
4. Create a student marks list and perform list operations.
5. Build a grading system using conditional statements.
6. Print multiplication tables using loops.
7. Create calculator functions using different argument types.
8. Build a student record system using dictionaries.
9. Store coordinates using tuples.
10. Create and import your own calculator module.
11. Convert Python dictionaries into JSON and back.
12. Create a text file, write data, append data, and read it.
13. Create a Python module with a proper main guard.
14. Build a calculator that handles invalid input and division by zero.

**Learning Tip:** Do not just read the code. Type each example yourself, execute it, change its values, and observe the output. This will help you understand Python fundamentals much more effectively.
