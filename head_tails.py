import random

spin = input("input head or tail :")
random_no = random.randint(0, 1)

if spin == "head" and random_no == 1:
    print("win")
elif spin == "head" and random_no == 0:
    print("lose")
elif spin == "tail" and random_no == 0:
    print("win")
else:
    print("lose")
