class Jumper:
    """The jumper (player) guessing the word. 
    
    The responsibility of Jumper is to tack the number of attemprs and create a draw representing the status (number of opportunities).
    
    Attributes:
        _error_count (int): The number of failed attempts guessing teh word
    """    

    def __init__(self) -> None:
        self._error_count = 0

    def draw_jumper(self):
        """ Provides a fdrawing of the jumper based on the number of incorrect guesses 

            Args:
                self (Jumper): An instance of Jumper.

            Returns:
                string: A drawing representing the status of the jumpers
        """
        drawing = []
        if self._error_count == 0:
            drawing.append("   ___")
        if self._error_count <= 1:
            drawing.append("  /___\\")
        if self._error_count <= 2:
            drawing.append("  \   /")
        if self._error_count <= 3:
            drawing.append("   \ /")
            drawing.append("    0")
        else:
            drawing.append("    x")

        drawing.append("   /|\\")
        drawing.append("   / \\")
        drawing.append("      ")
        drawing.append("^^^^^^^^^")

        return "\n".join(drawing)

    def add_incorrect_guess(self):
        """ Adds up on counting of incorrect guesses 

            Args:
                self (Jumper): An instance of Jumper.

            Returns:
                Nothing
        """
        self._error_count += 1

    def can_guess(self):
        """ Checks if no more than 3 incorrect guesses have been made

            Args:
                self (Jumper): An instance of Jumper.

            Returns:
                boolean: True if number of incorrect guesses is less than 4; false if otherwise.
        """
        return self._error_count < 4
