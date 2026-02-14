chosen_number = 67
guess = int(input("Guess a number from the list: "))

if guess > chosen_number:
    print("Too high! Try again.")
elif guess < chosen_number:
    print("Too low! Try again.")
else:
    print("Correct! Well done 🎉")