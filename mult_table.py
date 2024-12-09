import time

is_number = int(input("Enter number that will be main in multiplication table: "))

time.sleep(1)
print(f"multiplication table by {is_number}")
time.sleep(0.25)

for i in range(1, 11):
    print(f"{is_number} * {i} = {is_number * i}")
    time.sleep(0.5)