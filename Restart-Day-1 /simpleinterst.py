
# Simple Interest with error handling 

try:
    #taking input from the user 👤 
    p = int(input(""Enter the principal amount :"))
    r = int(input("enter the rate amount:"))
    t = int(input("Enter the time :"))

    Simple_interest=(p*r*t)/100

    print("Simpleinterest is" , Simple_interest)

except ValueError:
    print("please enter valid number")
