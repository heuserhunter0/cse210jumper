class Jumper:
    """
    The Jumper class manages the parachute size and draws it on the screen
    accordingly.

    The parachute lines will be deleted every time remove_line() is called.
    If there are no remaining lines on the parachute, the player's head will be
    replaced by an "x".

    Attributes:
        parachute_lines (list): list of tuples containing the X and Y
        coordinates of each line and the char in the position.
    """

    def __init__(self):
        """
        Constructs the Jumper object and initializes the starting parachute.
        """
        self.parachute_lines = [
            (2, 0, "_"), (3, 0, "_"), (4, 0, "_"),
            (1, 1, "/"), (2, 1, "_"), (3, 1, "_"), (4, 1, "_"), (5, 1, "\\"),
            (1, 2, "\\"), (5, 2, "/"),
            (2, 3, "\\"), (4, 3, "/")
        ]

    def get_parachute_size(self):
        """
        Gets the current number of lines in the parachute.

        Returns:
            Integer representing the number of lines left in the parachute.
        """
        return len(self.parachute_lines)

    def remove_line(self):
        """
        Remove a single line from the parachute. If there are no more lines,
        ignore call.
        """
        if self.get_parachute_size() > 0:
            self.parachute_lines.pop(0)

    def draw(self):
        """
        Draws parachute based on the number of lines left, the player, and the
        floor.
        """
        last_drawn_x = -1
        last_drawn_y = 0

        # Draw parachute
        for line in self.parachute_lines:
            x, y, char = line

            while last_drawn_y < y:
                print("\n", end="")
                last_drawn_y += 1
                last_drawn_x = -1

            while last_drawn_x < x:
                last_drawn_x += 1

                if last_drawn_x < x:
                    print(" ", end="")

            print(char, end="")

        # Draw player
        if self.get_parachute_size() == 0:
            print("\n   x")
        else:
            print("\n   o")

        print("  /|\\\n  / \\")

        # Draw floor
        print("\n^^^^^^^")
