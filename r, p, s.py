import random

should_coun = True

#computer = ["p", "r", "s"]
#choise_computer = random.choice(computer)

while should_coun:
    player_choice = input("Choise player: ").lower()

    if player_choice not in ["r", "s", "p"]:
        print("Incorrect input. try again")
        continue

    gen = {1:"r", 2:"s", 3:"p"}
    comp_choice = gen[random.randint(1, 3)]

    print(f"Computer choice: {comp_choice}")

    winning_comb = [("p", "r"), ("r", "s"), ("s", "p")]

    if player_choice == comp_choice:
        print("draw")
    elif (player_choice, comp_choice) in winning_comb:
        print("player wins")
    else:
        print("comp wins")

    should_coun = input("want to proceed? [y/n]").lower()

