# for_loop.py
# These programs demonstrates the use of for loop in Python

print("--- Printing numbers from 1 to 5 ---")
for i in range(1, 6):
    print(i)

print("\n--- Printing even numbers from 1 to 10 ---")
for i in range(2, 11, 2):
    print(i)

print("\n--- Multiplication Table ---")
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("\n--- Sum of first N natural numbers ---")
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum is:", sum)

print("\n--- Loop through a string ---")
name = input("Enter your name: ")
for ch in name:
    print(ch)
