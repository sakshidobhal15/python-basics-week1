# Print numbers from 1 to 100

for i in range(1, 101):
    print(i)
  
----------------------------------------------

# Sum of first N numbers

try:
    n = int(input("Enter a number: "))
    total = 0

    for i in range(1, n + 1):
        total += i

    print(f"Sum is {total}")

except ValueError:
    print("Please enter a valid number")
----------------------------------------------------


# Multiplication table

try:
    num = int(input("Enter a number: "))

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

except ValueError:
    print("Please enter a valid number")

------------------------------------------------------

# Check positive, negative or zero

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

----------------------------------------------------------

# Check voting eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")










