# operators.py
# This program demonstrates different types of operators in Python

# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\n--- Arithmetic Operators ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

print("\n--- Comparison Operators ---")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\n--- Logical Operators ---")
print("a > 0 and b > 0:", a > 0 and b > 0)
print("a > 0 or b > 0:", a > 0 or b > 0)
print("not(a > 0):", not (a > 0))

print("\n--- Assignment Operators ---")
x = a
x += b
print("x += b:", x)

x -= b
print("x -= b:", x)

x *= b
print("x *= b:", x)

x /= b
print("x /= b:", x)
