from jumper import Jumper
from puzzle import Puzzle
from terminal_service import TerminalService

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        jumper (Jumper): The game's jumper (player).
        puzzle (Puzzle): The game's word puzzle.
        terminal_service: For getting and displaying information on the terminal.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._puzzle = Puzzle()
        self._terminal_service = TerminalService()
    
    def start_game(self):
        """Starts the game by running the main game loop, until puzzle is solved or player is our of atttempts.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._jumper.can_guess() and self._puzzle.has_missing_letters():
            # ask for a letter
            guess = self._terminal_service.read_text("Guess a letter [a-z]: ")
            
            # check if guessed letter is in word
            if not self._puzzle.has_letter(guess):
                self._jumper.add_incorrect_guess()
            
            # print current progress
            word_progress = self._puzzle.get_word_progress()
            self._terminal_service.write_text(word_progress)
            #spacing
            self._terminal_service.write_text("")
            # parachute drawing
            drawing = self._jumper.draw_jumper()
            self._terminal_service.write_text(drawing)

        # output win or lose message
        if self._jumper.can_guess():
            self._terminal_service.write_text("\n ====    You won! You completed the word.    ====\n\n");
        else:
            self._terminal_service.write_text("\n\n ====    You lost :(     ==== \n\n");
            