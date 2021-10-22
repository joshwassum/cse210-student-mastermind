class Guess:
    """A maneuver in the game. The responsibility of guess  is to keep track of the stones to remove and which pile to remove them from.
    
    Stereotype: 
        Information Holder

    Attributes:
        _number (integer): The number to remove from.
        _guess (integer): The number of position to remove.
    """
    def __init__(self, guess, player):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._guess = guess
        self._player = player

    def get_guess(self):
        """Returns the pile to remove from.

        Args:
            self (Guess): an instance of Guess.
        """
        return self._guess

    def get_player(self):
        """Returns the number of stones to remove.

        Args:
            self (Guess): an instance of Guess.
        """
        return self._player