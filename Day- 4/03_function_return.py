# function_return.py
# Demonstrates return values in functions

def add(a, b):
    return a + b

result = add(3, 4)
print("Result:", result)


def square(num):
    return num * num

print("Square:", square(6))


def get_details():
    name = "Sakshi"
    age = 20
    return name, age

n, a = get_details()
print("Name:", n)
print("Age:", a)
