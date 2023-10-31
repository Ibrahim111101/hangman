import random
world_list = ["strawberry","apple","bannana","orange"]
guessed_word = random.choice(world_list)


def check_guess(guess_letter_input):
    guess_letter_input.lower()
    if guess_letter_input in guessed_word:
        print(f'Good guess! {guess_letter_input} is in the word')
    else:
        print(f'Sorry, {guess_letter_input} is not in the word')


def ask_for_input():
    while True:
        guess_letter_input = input("guess a letter ")
        if len(guess_letter_input) == 1 and ('isalpha'):
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess_letter_input)

ask_for_input()