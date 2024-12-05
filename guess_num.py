import random

tries = 0
number = random.randint(1, 50)

print("Hmm.. Try to guess what number between 1 and 50 i was thinking about")

while tries < 6:
    guess = int(input("Take a guess: "))
    tries+=1

    if guess < number:
        print("Small")
    
    if guess > number:
        print("Big")

    if guess == number:
        print(f"You're right. You guess my number in {tries} guesses")
        break

    if guess != number and tries == 6:
        print("You are loser")
        break