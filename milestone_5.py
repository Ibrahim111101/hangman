import random

class Hangman:
    def __init__(self,word_list,num_lives):
        """
Initializes a Hangman game instance.

Args:
    word_list (list): List of words to choose from for the game.
    num_lives (int): Number of lives the player has.

Attributes:
    word (str): The word to guess.
    word_guessed (list): List representing the word with underscores for hidden letters.
    num_letters (int): Number of unique letters in the word.
    num_lives (int): Number of lives the player has.
    word_list (list): List of words for the game.
    list_of_guesses (list): List to keep track of guessed letters.
"""
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        """
        Checks a guessed letter against the word and updates the game state.

        Args:
            guess (str): The letter guessed by the player.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for letter in range(len(self.word)):
                if self.word[letter] == guess:
                    self.word_guessed[letter] = guess # indexing the guessed letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'sorry {guess} is not in the word')
            print(f'you have {self.num_lives} lives left')


    def ask_for_input(self):
        """
        Continuously prompts the player to guess a letter and updates the game state.
        """
        while True:
            guess = input('Guess a letter ')
            if len(guess) != 1 and ('isalpha'):
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print("Current word:", " ".join(self.word_guessed))
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives > 0 and game.num_letters == 0:
            print("Congratulations. You won the game pal!")
            break


word_list = ["strawberry", "apple", "banana", "orange"]
play_game(word_list)
