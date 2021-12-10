winning_guess = 8
guess_count = 0
guess_limit = 2
guess = int(input("Guess a number\n"))
while guess_count < guess_limit:
    guess = int(input("wrong answer, try again\n"))
    guess_count += 1
    if guess == winning_guess:
        print("You won!!")
        break
else:
    print("You failed :(")