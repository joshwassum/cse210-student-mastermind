
class Roster:

    """
        This class keeps track of the players name, who's turn it is, and changes the turn. 
    
        Attributes:
            self.current_player
            self.players
    """

    def __init__(self):
        """
            this is the class constructro that holds the list of players names and who's turn it is.
        """

        self.current = 0
        self.players = []

    def add_player(self, player):
        """
            This module gets player and adds it to the self.players list.
        """
        if player not in self.players:
            self.players.append(player)
        else:
            return f"{player.title()} is already a player. "

    def get.current(self):
        """
            This will return the current player when called.
        """

        current_player = self.players[self.current]
        return current_player

    def next_player(self):
        """
            this function changes the attribute self.current to change the current player.
        """

        self.current = (self.current + 1) % len(self.players)
