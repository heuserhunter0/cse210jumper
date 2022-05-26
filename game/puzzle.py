
from operator import truediv
import random


class Puzzle:
    """The word puzzle to guess. 
    
    The responsibility of Puzzle is to randomly choose a word and keep track of the guessing attempts. 
    
    Attributes:
        _word (string): The randomly chosen word to be guessed
        _guessed_letters (List[string]): List of guessed to complete the word.
    """    
    def __init__(self):
        """Constructs a new Puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        #list of words to gues
        _words = ["toast", "shark", "arrow", "flush", "health","detail","visual", "address", "publish", "collect", "execute"]
        #choose one randomly
        self._word = _words[random.randint(0,10)] #"assembly"
        #guessed letters list
        self._guessed_letters = []
        #print(f"[secret word: {self._word}]")


    def has_letter(self, letter):
        """ Checks if letter is in the word to guess

            Args:
                self (Puzzle): An instance of Puzzle.
                letter (string): letter guessed

            Returns:
                boolean: True if the letter was found in the word to guess; false if otherwise.
        """
        letter = letter.lower()
        if letter not in self._guessed_letters:
            self._guessed_letters.append(letter)

        if letter in self._word:
            return True
        else:
            return False
        
    def get_word_progress(self):
        """ Returns the word to guess with indicating spaces for missing letters (yet to guess)
                Example: if the word is "part" and only 'a' and 't' have been guessed it will return "_ a _ t"

            Args:
                self (Puzzle): An instance of Puzzle.

            Returns:
                string: shows the progress on the word to guess, showing each guessed letter 
                and the spaces for the missing ones.
        """
        word_progress = ""
        for letter in self._word:
            if letter in self._guessed_letters:
                word_progress += letter + " "
            else:
                word_progress+= "_ "

        return word_progress
        
        # word_spaces = []
        # for n in range(len(self._word)):
        #     word_spaces.append("_")


        # #update hint word
        # for letter in self._guessed_letters:
        #     find_index = self._word.find(letter)
        #     while find_index >=0:
        #         word_spaces[find_index] = letter
        #         find_index = self._word.find(letter, find_index + 1)

        #return " ".join(word_spaces)


    def has_missing_letters(self):
        """ Checks there are still some letter missing to complete the word

            Args:
                self (Puzzle): An instance of Puzzle.

            Returns:
                boolean: True if the are missing letter that need to be guessed yet; false if otherwise.
        """
        word_progress = self.get_word_progress()
        if "_" in word_progress:
            return True
        else:
            return False
