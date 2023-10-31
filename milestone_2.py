import random
world_list = ["strawberry","apple","bannana","orange"]
print(world_list)
word = random.choice(world_list)
print(word)

guess = input("enter a single letter ")

if len(guess) == 1 and ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    print("Good Guess!")
else:
    print("Oops! that is not a valid input!")