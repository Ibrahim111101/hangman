import random

class Hangman:
    def __init__(self,word_list,num_lives):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess # indexing the guessed letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'sorry {guess} is not in the word')
            print(f'you have {self.num_lives} lives left')


    def ask_for_input(self):
        while True:
            guess = input('Guess a letter ')
            if len(guess) != 1 and ('isalpha'):
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')

           
            if len(guess) == 1 and guess.isalpha():
                if guess not in self.list_of_guesses:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess) 

word_list = ["strawberry", "apple", "banana", "orange"]
num_lives = 5
game = Hangman(word_list,num_lives)
game.ask_for_input()

    