import random

class Board():
    """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder
    Attributes:
        _piles (list): The number of piles of stones.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """

        self._number = []
        self._prepare()
        


    def to_string(self, players):
        """Converts the board data to its string representation.
        Args:
           self (Board): an instance of Board.
        Returns:
            string: A representation of the current board.
        """ 
        
          
        board = ""

        border = "\n---------------------"
        guess = self._number[1]
        hint = self._number[2]

        board += border

        for i in range(len(players.players)):
            name = players.players[i].get_name()
            i+=1

            board +=(f"\nPlayer name: {name} " + guess + ", " + hint) 
         
        board += border
        return board


    def hint(self, number, guess):
        """Generates a hint based on the given code and guess.

        Args:
        self (Board): An instance of Board.
        code (string): The code to compare with.
        guess (string): The guess that was made.

        Returns:
        string: A hint in the form [xxxx]
        """ 
        hint = ""
        for index, letter in enumerate(guess):
            if number[index] == letter:
                hint += "x"
            elif letter in number:
                hint += "o"
        else:
            hint += "*"
        return hint
        

    def check_guess(self, guess):
        '''Checks the users letter guess a letter with a true or false then return
        
        
        Args:
            self (Board): an instance of Board.
        '''

        if guess == self._number[0]:
            return True
        else:
            return False  


    def _prepare(self):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        self._number = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._number = [self._number, guess, hint]
        print(self._number)
        
        
