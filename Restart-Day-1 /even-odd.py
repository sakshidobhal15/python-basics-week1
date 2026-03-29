# Even Odd Checker with error handling

try:
    num = int(input("Enter a number: "))
    
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")

except ValueError:
    print("Please enter a valid number")



