import random

def roll_dice():
    # Generate a random number between 1 and 6
    dice_result = random.randint(1, 6)
    return dice_result

def roll_n_dice(n):
    result = []
    for i in range(n):
        roll = roll_dice()
        result.append(roll)
    return result

def tronder_yatzy_standard():
    sum = 0
    rolls = 6

    rolls += 3
    dice = 6
    for i in range(3):
        roll = roll_n_dice(dice)
        rolls -= 1
        occurences = roll.count(3)
        dice = dice - occurences
        sum = sum + 3*occurences
        if sum >= 9: break
    
    rolls += 3
    dice = 6
    for i in range(4):
        roll = roll_n_dice(dice)
        rolls -= 1
        occurences = roll.count(4)
        dice = dice - occurences
        sum = sum + 4*occurences
        if sum >= 21: break
    
    rolls += 3
    dice = 6
    for i in range(5):
        roll = roll_n_dice(dice)
        rolls -= 1
        occurences = roll.count(5)
        dice = dice - occurences
        sum = sum + 5*occurences
        if sum >= 41: break
    
    rolls += 3
    dice = 6
    for i in range(rolls):
        roll = roll_n_dice(dice)
        occurences = roll.count(6)
        dice = dice - occurences
        sum = sum + 6*occurences

    return sum

n = 1000000
total = 0
for i in range(n):
    total += tronder_yatzy_standard()

sum = total/n


# Simulate a dice roll and print the result
print(f"Poengsummen ble {sum}")