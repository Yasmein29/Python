def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)
    
num1 = int(input("Enter a number: "))
if num1 < 0:
    print("Sorry , factorial does not exist for negative numbers")
elif num1 == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num1, "is", factorial(num1))
a = factorial(num1 )
print(a)