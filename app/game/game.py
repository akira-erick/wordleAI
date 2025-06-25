from words.words import get_words
import random


class Game:
    def __init__(self):
        self.words_list = None
        self.word = ""
        self.guesses = []
        self.attempts = 0

    def seeded_word(self, word: str):
        self.words_list = get_words()
        if word.upper() not in self.words_list:
            raise ValueError("Word not in words list")
        self.word = word.upper()
        self.guesses = []
        self.attempts = 0

    def start_game(self):
        self.words_list = get_words()
        self.word = random.choice(self.words_list).upper()
        self.guesses = []
        self.attempts = 0

    def make_guess(self, guess: str):
        guess = list(guess.upper())
        word = list(self.word)

        if guess in self.guesses:
            return

        resp = ['R', 'R', 'R', 'R', 'R']
        self.guesses.append(guess)

        for i in range(len(guess)):
            if guess[i] == word[i]:
                resp[i] = 'G'
                word[i] = ' '
        for i in range(len(guess)):
            if resp[i] != 'G':
                for j in range(len(word)):
                    if guess[i] == word[j]:
                        resp[i] = 'Y'
                        word[j] = ' '

        self.attempts += 1
        return resp

    def get_word(self):
        return self.word

    def get_attempts(self):
        return self.attempts


game = Game()

game.start_game()
print(game.get_word())
