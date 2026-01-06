# function_logic_programs.py
# Logic programs using functions

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
print("Number is:", even_or_odd(number))


def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter n: "))
print("Sum:", sum_of_numbers(n))


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter number: "))
print("Factorial:", factorial(num))
