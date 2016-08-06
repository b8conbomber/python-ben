#import random
from random import choice
#random = sprinkles

def handleQuestion(jeff,bill):
    if "jeff" in jeff:
        print("You found the holy grail")
        return ""
    else:
        answer = choice(bill)
        return answer
