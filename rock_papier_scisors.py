"""
Code which plays rock,papier, scisors with you!
"""
import random

def play():
    "This functon returns the outcome"
    user = input("Choose 'r' for rock, 's' for scisors, and 'p' for papier: ")
    comuter = random.choice(['p','s','r'])
    if user == comuter:
        out = "Tie!"
    elif is_win(user,comuter) is True:
        out = "You WON!"
    else:
        out = "You Lost"
    return out

def is_win(palyer, oponent):
    "This function sets the rules"
    if \
            (palyer == 's' and oponent == 'p') or \
            (palyer == 'p' and oponent == 'r') or \
            (palyer == 'r' and oponent == 's'):
        return True

