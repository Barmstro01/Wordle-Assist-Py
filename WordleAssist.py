class WordleAssist:
    # def __init__(this, word_list):
        # this.word_list = []

    def get_word_list(self):
        with open('word_list_abrev.txt', 'r') as f:
            word_list = f.readlines()
        return word_list

    def prompt_guess(self, dictionary):
        guesses_remaining = 6
        while guesses_remaining > 0:
            guess = input("Please enter your guess: ")
            print(f"You guessed: {guess} and have {guesses_remaining - 1}"
                " guesses remaining")
            correctness = self.prompt_correctness(guess)
            print(correctness)
            guesses_remaining -= 1
    
    def prompt_correctness(self, guess):
        hints = [0,0,0,0,0]
        h = 0
        while h <= 4:
            hints[h] = input(f"Enter correctness of guess {guess[h]}: ")
            h += 1     
        return [guess, hints]

   # def incorrect_pairs(self, guess, hint, dictionary):
    #    h = 0
     #   while h <= 4:
      #      if 



new_assist = WordleAssist()

dictionary = new_assist.get_word_list()

new_assist.prompt_guess(dictionary)



