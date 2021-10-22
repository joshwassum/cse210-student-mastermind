class Player:
    """A person taking part in a game. 
    """
    def __init__(self, name):
        """The glue to the class
        """
        self._name = name
        self._guess = None
        
    def get_guess(self):
        """Stores the players last guess, if no move has occured nothing will happen
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