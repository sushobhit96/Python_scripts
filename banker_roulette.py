import random

names_string = input("Input names of the person")   # taking input
names = names_string.split()     # converting to a list
num_of_names = len(names)        # counting the no of names in list
random_name = random.randint(0, num_of_names - 1)    # selecting a random no from list
paying_person = names[random_name]          # passing the random no as index position to "names" list
                                            # to get the person name
print(f"the person who will pay the bill is {paying_person}")
