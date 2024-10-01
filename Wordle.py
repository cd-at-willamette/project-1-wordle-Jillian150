########################################
# Name: Jillian Price
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr):
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random
gw = WordleGWindow()
def random_five_letter_word():
        return random.choice(ENGLISH_WORDS)

def display_word(word):
     for i, letter in enumerate(word):
          gw.set_square_letter(0, i, letter)

def wordle():
    # The main function to play the Wordle game.
    
    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        gw.show_message("You need to implement this method")

        guess_str = gw.get_input().strip().lower()
        answer_str = random_five_letter_word()
    
        if guess_str in ENGLISH_WORDS:
            color_row(current_row, guess_str, answer_str)
            if guess_str == answer_str:
                gw.show_message("Congratulations! You've guessed the word!")
                gw.set_current_row(N_ROWS)  # Stop reading new guesses
            else:
                current_row += 1
                if current_row < N_ROWS:
                    gw.set_current_row(current_row)
                else:
                    gw.show_message(f"Game over! The correct word was: {answer_str}")
        else:
             gw.show_message("Not in word list")
             
    def color_row():
        guess_cap = guess_str.upper()
        answer_cap = answer_str.upper
        
        #finding green
        remaining_letters = list(answer_cap)
        for i in range(len(guess_cap)):
            if guess_cap[i] == answer_cap[i]:       
                gw.set_square_letter(0, i, guess_cap[i])
                gw.set_square_color(0, i, CORRECT_COLOR)
                remaining_letters[i] = None
        #finding yellow
        for i in range(len(guess_cap)):
            if guess_cap[i] != answer_cap[i] and guess_cap[i] in remaining_letters:
                gw.set_square_letter(0, i, guess_cap[i])
                gw.set_square_color(0, i, PRESENT_COLOR)
                remaining_letters[remaining_letters.index(guess_cap[i])] = None
        #any colors remaining(gray)
        for i in range(len(guess_cap)):
            if gw.get_square_color(0, i) == UNKNOWN_COLOR:
                gw.set_square_letter(0, i, guess_cap[i])
                gw.set_square_color(0, i, MISSING_COLOR)
            


    def word_to_row(word:str, row:int):
            gw.show_message("To do: word_to_row")
            
    def word_from_row(row:int) -> str:
            gw.show_message("To do: row_to_word")
            return "" # placeholder
    # to see if a word is in ENGLISH_WORDS, make it lower case.
    guess_str = "Hello"
    guess_low = guess_str.lower()
    guess_cap = guess_str.upper()
    print(guess_str, guess_str in ENGLISH_WORDS) # Hello False
    print(guess_low, guess_low in ENGLISH_WORDS) # hello True
    print(guess_cap, guess_cap in ENGLISH_WORDS) # HELLO False

    # places 'H' in the upper left  
    gw.set_square_letter(0,0,guess_cap[0])
    def enter_action():
        entered_word = gw.get_input().strip().lower()
        if entered_word() in ENGLISH_WORDS:
            gw.show_message("That's a 5 letter word")
        else:
            gw.show_message("Not in word list")

display_word(randome_five_letter_word())
enter_action

gw = WordleGWindow()
gw.add_enter_listener(enter_action)


# Startup boilerplate
if __name__ == "__main__":
    wordle()
