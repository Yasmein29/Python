number = int(input("Enter a number: "))

digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

sum_num = digit1**3 + digit2**3 + digit3**3

if number == sum_num:
    print(number, "is an Armstrong number.")
else:
    print(number, "isn't an Armstrong number.")