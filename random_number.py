"This code generate random number >= 0. You can guess the numebr."

import random as rd

number = int(input("CHOOSE Range!: "))

def guess(number):
    "Function chich help you guess the random number"
    random_numeber = rd.randint(1, number)
    guess = 0
    random_range = []
    for range_elem in range(number):
        if range_elem in range(random_numeber - 5, random_numeber + 6):
            random_range.append(range_elem)
    while guess != random_numeber:
        guess = int(input(f"Guess a number beetewen 1 and {number}! \n:"))
        if guess == random_numeber:
            out = "Congratulations!!YOU WON!"
        elif guess > random_numeber:
            out = "TO HIGH!"
        elif guess in random_range:
            out = "YOU ARE CLOSE!"
        else:
            out = "TO LOW!"
        print(out)
    return out
computer_range = int(input(
"""
CHOOSE Range for computer
and think about a number inside this range.
Memorise it!:
"""
))
def computer_guess(computer_range):
    "This function guesses the number which you have chosen"
    low = 1
    high = computer_range
    feedback = ""
    while feedback != "c":
        if low != high:
            computer_guess = rd.randint(low,high)
        else:
            computer_guess = low
        feedback = input(f"{computer_guess} is too low (L), too high (H) or correct (C)" ).lower()

        if feedback == "l":
            low = computer_guess +1
        elif feedback == "h":
            high = computer_guess -1
    print(f"CONGRATULATIONS {computer_guess} is your number!!!")
