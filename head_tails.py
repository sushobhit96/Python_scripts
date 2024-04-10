import random

spin = input("input head or tail :").lower()
random_no = random.randint(0, 1)

if spin == "head" and random_no == 1:
    print("Its heads : You win")
elif spin == "head" and random_no == 0:
    print("Its Tails : You lose")
elif spin == "tail" and random_no == 0:
    print("Its Tails : You win")
else:
    print("Its heads : You lose")
