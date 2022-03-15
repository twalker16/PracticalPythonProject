
def main():
    import random
    number = random.randint(1,100)
    guessMatch = False
    tries = 0
    name = input("What's your name? ")
    print(name + " I'm thinking of a number between 1  and 100.\n" + "Try to guess my Number")

    while guessMatch == False:
        guess = int(input("Whats your guess? "))
        if guess == number:
            tries = tries+1
            guessMatch = True
            print("Well done " + name +", you guessed it in " + str(tries) + " tries!")
        elif guess > number:
            print("Your guesss is too high, try again")
            tries = tries+1
        elif guess < number:
            print("Your guess is too low, try again")
            tries = tries+1

    print(number)

main()