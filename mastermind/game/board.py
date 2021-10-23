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
        self._hint = []
        self._guess =[]
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

        board += border

        for i in range(len(players.players)):
            name = players.players[i].get_name()

            board +=(f"\nPlayer name: {name} " + self._guess[i] + ", " + self._hint[i]) 
         
        board += border
        return board


    def hint(self, current_player, player_number):
        """Generates a hint based on the given code and guess.

        Args:
        self (Board): An instance of Board.
        current_player (Player): and instance of Player.
        player_number (int): player postition.

        Returns:
        string: A hint in the form [xxxx]
        """
        temp_code = list(str(current_player.get_code()))
        temp_hint = list(str(self._hint[player_number]))
        player_guess = list(str(current_player.get_guess().get_guess()))

        for i in range(4):
            if player_guess[i] == temp_code[i]:
                temp_hint[i] = "x"
            elif player_guess[i] in temp_code:
                temp_hint[i] = "o"
            else:
                temp_hint[i] = "*"
        self._hint[player_number] = "".join(temp_hint)
        self._guess[player_number] = "".join(player_guess)


    def check_guess(self, player):
        '''Checks the users letter guess a letter with a true or false then return
        
        
        Args:
            self (Board): an instance of Board.
        '''
        if "o" in self._hint[player] or "*" in self._hint[player]:
            return False
        else:
            return True


    def _prepare(self):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        for i in range(2):
            self._hint.append("****")
            self._guess.append("----")
