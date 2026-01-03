# user_input.py
# This program demonstrates how to take user input in Python
#bydefault python will take input of string datatype
# Taking string input
name = input("Enter your name: ")

# Taking integer input
age = int(input("Enter your age: "))

# Taking float input
percentage = float(input("Enter your percentage: "))

# Displaying the output
print("\n--- User Details ---")
print("Name:", name)
print("Age:", age)
print("Percentage:", percentage)

# Simple calculation using input
birth_year = 2025 - age
print("Estimated Birth Year:", birth_year)
