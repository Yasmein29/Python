print("Printing a star pattern")
n = int(input("Enter the number of rows you want to print: "))
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()