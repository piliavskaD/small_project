import random
import time

N = int(input("Enter the number of tries you what to toss the cube: "))

all_tuples = []

tries = 0

while tries < N:
    all_num = list()

    for i in range(2):
        numbers = random.randint(1, 6)
        all_num.append(numbers)

    main_num = tuple(all_num)
    all_tuples.append(main_num)

    tries += 1

total=0

time.sleep(0.5)

for i in range(len(all_tuples)):
    print(f"{i + 1} attemp numbers is {all_tuples[i]}")
    time.sleep(1)

print("Hmm... one second we are counting all your attempt")

time.sleep(2)

for elem in all_tuples:
    for i in elem:
        total += i
print(f"Your scores is {total}")