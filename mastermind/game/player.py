import random

class Player:
    """A person taking part in a game.

    Attributes:
        _name (string): An instance of the player name.
        _guess (Guess): An instance of Guess.
        _code (str): The players secret code to guess.
    """
    def __init__(self, name):
        """The glue to the class.

        Args:
            self (Player): An instance of Player.
            name (string): The players name.
        """
        self._name = name
        self._guess = None
        self._code = str(random.randint(1000, 9999))
        
    def get_guess(self):
        """Stores the players last guess, if no move has occurred nothing will happen
        """
        return self._guess

    def get_name(self):
        """This will return the players name
        """
        return self._name

    def set_guess(self, guess):
        """Sets the players guess, different than get_guess
        """
        self._guess = guess
    
    def get_code(self):

       return self._code