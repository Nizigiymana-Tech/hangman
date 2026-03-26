from random import randint

Words = [
    "Apple",
    "Banana",
    "Grapes",
    "Oranges",
    "Apples and Snickers"
    "Snickers"
]

def RNGWord():
    return Words[randint(0, (len(Words) - 1))]