# lists.py
# Basic list concepts in Python

numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Updating list element
numbers[2] = 35
print("Updated List:", numbers)

# Traversing list
print("Traversing list:")
for num in numbers:
    print(num)
