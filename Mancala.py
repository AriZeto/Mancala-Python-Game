# Author: Ari Zeto
# GitHub username: AriZeto
# Date: 11/19/2022
# Description: Fill in Later.

class Mancala:
    """
    Class representing the board game dubbed 'Mancala'. Contains characteristics about its players status tas well as
    information about the board.
    """
    def __init__(self):
        # Index 0 represents Player 1 Store, Index 7 represents Player 2 Store
        # Index 1 through 6 represents Player 1 Seeds, Index 8 through 13 represents Player 2 Seeds
        # Each pit contains four seeds
        self._mancala_board = [2, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0]
        self._player_1_store_index = self._mancala_board[0]
        self._player_2_store_index = self._mancala_board[7]
        self._player_1 = ''
        self._player_2 = ''

    def create_players(self, name):
        """
        Takes as a parameter the name of the Player. Returns the player object.
        """

        # Create Player Object, Return Player Object
        player_char = Player(name)

        if self._player_1 == '':
            self._player_1 = name

        elif self._player_2 == '':
            self._player_2 = name

        return player_char

    def print_board(self):
        """
        Contains no parameters. Prints specific formatted board information, such as the status of each
        player, their turns, and the data of the mancala board array itself.
        """
        print("Player 1: ")
        print("\nNumber of seeds in Player 1's Store: " + str(self._player_1_store_index))
        print("\nPlayer 1 contains seeds in pits 1 through 6 (index 1 - 6). Their current pits look like...:")
        print('\n' + str(self._mancala_board[1:7]))

        print("\nPlayer 2: ")
        print("\nNumber of seeds in Player 2's Store: " + str(self._player_2_store_index))
        print("\nPlayer 1 contains seeds in pits 1 through 6 (index 8 through 13). Their current pits look like...:")
        print('\n' + str(self._mancala_board[8:14]))

        # Return the winner
        return '\n' + self.return_winner()

    def grab_seeds(self, pit_index):
        """
        Takes as a parameter the indexed value of the Mancala Board for the specified Pit the user chooses.
        Gathers the amount of seeds from the specified indexed pit. Returns the amount of seeds from the pit.
        """
        # Grab the amount of seeds from the array position that contains pits.
        grab_seed_from_pit = self._mancala_board[pit_index]

        # Set the pit the user is picking the seeds up from to zero
        self._mancala_board[pit_index] = 0

        return grab_seed_from_pit

    def move_seed_per_pit(self, pit_index):
        """
        Distributes/drops a seed per each index pass of the Mancala board array.
        """
        # Grabs the amount of seeds from a pit.
        amount_of_seeds = self.grab_seeds()
        # To begin dropping seeds into next pit, increment pit index by 1
        pit_index = pit_index + 1
        while amount_of_seeds > 0:
            # Decrease amount of seeds by one per each pit
            amount_of_seeds -= 1
            pit_index += 1
            # Add seed to indexed pits
            self._mancala_board[pit_index] += 1


    def steal_player_seeds(self, pit_index):
        """

        :param pit_index:
        :return:
        """
        pass

    def play_game(self, player_number, pit_number):
        """
        Player moves seeds across the board.
        """
        print("Player " + {player_number} + " takes a turn")
        # Gather the number of seeds
        if pit_number >= 1 and pit_number <= 6:
            if player_number == 1:
                pit_index = pit_number
                num_of_seeds = self._mancala_board[pit_number]

                # Gather the number of seeds, and distribute them across each move
                grab_seed_amount = self.grab_seeds()
                self.move_seed_per_pit()

                # self._mancala_board[pit_index + num_of_seeds]

            if player_number == 2:
                # Add seven to get appropriate pit number
                pit_index = pit_number + 7
                num_of_seeds = self._mancala_board[pit_number + 7]

                # Gather the number of seeds, and distribute them across each move
                grab_seed_amount = self.grab_seeds()
                self.move_seed_per_pit()

    def if_row_zero(self, list_slice):
        """
        Helper function to 'return_winner'. Takes a slice of a list of the mancala board data member. Returns True
        if the row values of that list are 0, False otherwise.
        """
        for pit in list_slice:
            if pit != 0:
                return False
        return True


    def return_winner(self):
        """
        Takes no parameters. Returns the winner.
        """
        # Checks and compares index 0 and 7 (Mancala stores for Player 1 and Player 2) to see who has larger amount
        # Also checks if one of the player rows is empty.
        # if self._mancala_board[1:7] and self._mancala_board[8:14] == 0:
        if self.if_row_zero(self._mancala_board[1:7]) and self.if_row_zero(self._mancala_board[8:14]):
            if self._player_1_store_index > self._player_2_store_index:
                return "Winner is Player 1: " + self._player_1
            elif self._player_1_store_index < self._player_2_store_index:
                return "Winner is Player 2: " + self._player_2
            elif self._player_1_store_index == self._player_2_store_index:
                return "It's a tie!"
        else:
            return "Game has not ended."


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



game = Mancala()
player_1 = game.create_players('Ari')
player_2 = game.create_players('Milky')
# print(player_1.get_player_name())
# print(player_2.get_player_name())

print(game.print_board())