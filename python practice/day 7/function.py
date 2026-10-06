# Task 1 — Basic Function
def greet():
    print("Hello Abhishek")
greet()

# Task 2 — Parameter
def greet(name):
    print(f"Hello {name}")

greet("Abhishek")

# Task 3 — Two Parameters
def greet(a, b):
    return a+b
result = greet(10, 20)
print(result)

# Task 4 — Square
def square(num):
    return num*num
print(square(5))

# Task 5 — Even/Odd
def check_number(num):
    if num%2==0:
        return "Even"
    else:
        return "odd"
number = int(input("Enter a number: "))
print(check_number(number))

# Task 6 — Age Check
def check_age(age):
    if age>=18:
        return "eligible"
    else:
        return "not eligible"

age = int(input("Enter your age: "))
print(check_age(age))

# Task 7 — List Sum
def calculate_sum(number):
    total = 0
    for num in number:
        total+=num
    return total

numbers = [10, 20, 30, 40, 50]
print("sum of the list is: ", calculate_sum(numbers))

# Task 8 — Largest Number
def find_largest(numbers):
    larg_num = numbers[0]
    for num in numbers:
        if num>larg_num:
            larg_num = num
    return larg_num
number = [10, 25, 5, 40, 15]
print("largest number is : ", find_largest(number))

