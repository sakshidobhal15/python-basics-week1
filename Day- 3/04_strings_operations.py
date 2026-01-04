# string_operations.py
# Common string operations

text = "  Hello Python World  "

print("Original string:", text)

print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Stripped:", text.strip())

print("Replace:", text.replace("Python", "Programming"))

words = text.split()
print("Split into list:", words)

joined = "-".join(words)
print("Joined string:", joined)

print("Find 'Python':", text.find("Python"))
print("Count of 'o':", text.count("o"))
