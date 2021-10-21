class Move:
    """A maneuver in the game. The responsibility of guess is to keep track of the stones to remove and which pile to remove them from.
    
    Stereotype: 
        Information Holder

    Attributes:
        _number (integer): The number to remove from.
        _guess (integer): The number of position to remove.
    """
    def __init__(self, guess, number):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._number = number
        self._guess = guess

    def get_number(self):
        """Returns the pile to remove from.

        Args:
            self (Guess): an instance of Guess.
        """
        return self._number

    def get_position(self):
        """Returns the number of stones to remove.

        Args:
            self (Guess): an instance of Guess.
        """
        return self._position