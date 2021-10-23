from game.roster import Roster
from game.guess import Guess
from game.console import Console
from game.player import Player
from game.board import Board

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        board (Board): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        guess (Guess): An instance of the class of objects known as Guess.
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """

        self._board = Board()
        self._console = Console()
        self._keep_playing = True
        self._roster = Roster()

    def start_game(self):
        """Controls the flow of the game.

        Args:
            self (Director): an instance of Director
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.

        Args:
            self (Director): An instance of Director.
        """
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the guess from the current player.

        Args:
            self (Director): An instance of Director.
        """

        board = self._board.to_string(self._roster)
        self._console.write(board)
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        guessing = True
        while guessing:
            player_guess = self._console.read_number("What is your guess? ")

            if len(str(abs(player_guess))) == 4:
                guess = Guess(player_guess)
                player.set_guess(guess)
                guessing = False
            else:
                self._console.write("Incorrect guess format, please enter a four digit number.")

    def _do_updates(self):
        """Updates the important game information for each round of play. In
        this case, that means updating the board with the current guess.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        guess = player.get_guess()
        self._board.hint(guess, player._)

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if the guess is correct and declaring a winner.

        Args:
            self (Director): An instance of Director.
        """
        if self._board.check_guess():
            winner = self._roster.get_current()
            name = winner.get_name()
            self._console.write(f"\n {name} won!")
            self._keep_playing = False
        self._roster.next_player()
