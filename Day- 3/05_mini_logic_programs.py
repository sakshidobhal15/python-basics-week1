# mini_logic_programs.py
# Mini logic programs using lists and strings

# Count vowels in a string
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in string:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)


# Reverse a string
print("Reversed string:", string[::-1])


# Search element in list
numbers = [5, 10, 15, 20, 25]
key = int(input("Enter number to search: "))

if key in numbers:
    print("Element found in list")
else:
    print("Element not found")


# Find length of list without len()
length = 0
for _ in numbers:
    length += 1

print("Length of list:", length)
