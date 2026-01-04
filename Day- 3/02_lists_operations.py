# list_operations.py
# Demonstrates common list operations

marks = [45, 78, 60, 89]

print("Original List:", marks)

marks.append(95)
print("After append:", marks)

marks.insert(1, 50)
print("After insert:", marks)

marks.remove(60)
print("After remove:", marks)

marks.pop()
print("After pop:", marks)

marks.sort()
print("Sorted list:", marks)

marks.reverse()
print("Reversed list:", marks)

print("Length of list:", len(marks))

# Membership check
print("78 in list?", 78 in marks)
