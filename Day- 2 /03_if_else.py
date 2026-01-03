# conditional_statements.py
# This program demonstrates conditional statements in Python
# This Program is done by both methods of conditional statements ie if else and if elif else ladder
# Taking input from user
num = int(input("Enter a number: "))

print("\n--- If Statement ---")
if num > 0:
    print("The number is positive")

print("\n--- If-Else Statement ---")
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

print("\n--- If-Elif-Else Ladder ---")
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

print("\n--- Simple Eligibility Check ---")
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
