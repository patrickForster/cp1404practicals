import random

MIN = 1
MAX = 45
NUMBERS_PER_LINE = 6

no_of_quick_picks = int(input("How many Quick Picks would you like: "))
while no_of_quick_picks <= 0:
    print("you need at least 1!")
    no_of_quick_picks = int(input("How many Quick Picks would you like: "))

for i in range(no_of_quick_picks):
    quick_pick = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MIN, MAX)
        while number in quick_pick:
            number = random.randint(MIN, MAX)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join("{:2}".format(number) for number in quick_pick))
