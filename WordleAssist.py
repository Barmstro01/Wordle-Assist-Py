class WordleAssist:
    # def __init__(this, word_list):
        # this.word_list = []
    def check_pres(self, sub, test_str):
        for ele in sub:
            if ele in test_str:
                return 0
        return 1    

    def get_word_list(self):
        with open('word_list_abrev.txt', 'r') as f:
            word_list = f.read().splitlines()
        return word_list

    def prompt_guess(self, word_list):
        print(word_list)
        guesses_remaining = 6
        while guesses_remaining > 0:
            guess = input("Please enter your guess: ")
            print(f"You guessed: {guess} and have {guesses_remaining - 1}"
                " guesses remaining")
            hints = self.prompt_correctness(guess)
            word_list = self.incorrect_pairs(guess, hints, word_list)
            guesses_remaining -= 1
            print(word_list)
    
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
                res = [ele for ele in word_list if self.check_pres(ele, guessed)]
            h += 1
        return res
                
            
new_assist = WordleAssist()

word_list = new_assist.get_word_list()

new_assist.prompt_guess(word_list)
