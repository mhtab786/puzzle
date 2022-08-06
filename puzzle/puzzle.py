import random

print("welcome to treasure island,\n your mission is to find the treasure")
print("\n first you have to choose a path\n then you will cross the river\n you have to open a gate ")

path = ["left", "right"]
me = input("you are at a crossroad, where do you want to go? \n type left or right: ").lower()
ghost = random.choice(path)
if me != ghost:
    print("your luck, move forward")

    river = ["swim", "boat"]
    me = input("you came across a river, there is an island in the middle"
               " of the river. \n type swim or boat: ")
    ghost = random.choice(river)
    if me != ghost:
        print("your luck, move forward")

        gate = ["red", "blue", "yellow"]
        me = input("you have to choose a gate \n type red or blue or yellow: ")
        ghost = random.choice(gate)
        if me == ghost:
            print("you are dead meat")
        else:
            print("you win")

    else:
        print("you are dead meat")

else:
    print(f"you are dead meat, a beast is behind {ghost} gate")


