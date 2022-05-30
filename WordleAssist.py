from operator import contains

class WordleAssist:
    # def __init__(this, word_list):
        # this.word_list = []

    def get_word_list(self):
        with open('word_list_abrev.txt', 'r') as f:
            word_list = f.read().splitlines()
        return word_list

    def prompt_guess(self, word_list):
        guesses_remaining = 6
        while guesses_remaining > 0:
            guess = input("Please enter your guess: ")
            print(f"You guessed: {guess} and have {guesses_remaining - 1}"
                " guesses remaining")
            hints = self.prompt_correctness(guess)
            self.incorrect_pairs(guess, hints, word_list)
            guesses_remaining -= 1
    
    def prompt_correctness(self, guess):
        hint = [0,0,0,0,0]
        h = 0
        while h <= 4:
            hint[h] = input(f"Enter correctness of guess {guess[h]}: ")
            h += 1     
        return hint

    def incorrect_pairs(self, guess, hint, word_list):
        h = 0
        while h <= 4:
            hints = hint[h]
            if hints == '0':
                guessed = guess[h]
                print(f"Found {guessed}")
            h += 1
                
            
new_assist = WordleAssist()

word_list = new_assist.get_word_list()

new_assist.prompt_guess(word_list)
