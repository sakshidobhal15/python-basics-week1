# while_loop.py
# This program demonstrates the use of while loop in Python

print("--- Printing numbers from 1 to 5 ---")
i = 1
while i <= 5:
    print(i)
    i += 1

print("\n--- Printing even numbers from 1 to 10 ---")
i = 2
while i <= 10:
    print(i)
    i += 2

print("\n--- Sum of first N natural numbers ---")
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum is:", sum)

print("\n--- User Controlled Loop ---")
choice = "y"
while choice == "y":
    num = int(input("Enter a number: "))
    print("Square of number:", num * num)
    choice = input("Do you want to continue? (y/n): ")

print("\n--- Countdown Program ---")
count = int(input("Enter countdown number: "))
while count > 0:
    print(count)
    count -= 1
print("Done!")
