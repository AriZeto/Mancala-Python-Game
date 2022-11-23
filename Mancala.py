# Author: Ari Zeto
# GitHub username: AriZeto
# Date: 11/19/2022
# Description: Fill in Later.

class Mancala:
    """
    Class representing the board game dubbed 'Mancala'. Contains characteristics about its players as well as
    information about the board.
    """
    def __init__(self):
        # Index 0 represents Player 1 Store, Index 1 represents Player 2 Store
        # Index 2 through 7 represents Player 1 Seeds, Index 8 through 13 represents Player 2 Seeds
        self._mancala_board = []

    def create_player(self, name):
        """
        Takes as a parameter the name of the Player. Returns the player object.
        """

        # Create Player Object, Return Player Object
        player_char = Player(name)
        return player_char

    def print_board(self):
        """
        Contains no parameters. Returns specific formatted board information.
        """

        return self._board_info


class Player(Mancala):
    """
    A subclass of the Mancala class. Contains information about a player of the Mancala board.
    """
    def __init__(self, name):
        super().__init__()
        self._name = name


    def get_player_name(self):
        """
        Returns the name of a Mancala Player.
        """
        return self._name
