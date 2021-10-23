class Guess:
    """A maneuver in the game. The responsibility of guess  is to keep track of the stones to remove and which pile to remove them from.
    
    Stereotype: 
        Information Holder

    Attributes:
        _guess (integer): The current players guess.
    """
    def __init__(self, guess):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._guess = guess

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