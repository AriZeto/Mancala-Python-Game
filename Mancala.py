# Author: Ari Zeto
# GitHub username: AriZeto
# Date: 11/27/2022
# Description: Fill in Later.

class Mancala:
    """
    Class representing the board game dubbed 'Mancala'. Contains information regarding the Board status as well as
    information regarding player names.
    """
    def __init__(self):
        # Index 0 represents Player 1 Store, Index 7 represents Player 2 Store
        # Index 1 through 6 represents Player 1 Seeds, Index 8 through 13 represents Player 2 Seeds
        # Each pit contains four seeds
        self._mancala_board = [0, 4, 0, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
        self._player_1_store_index = self._mancala_board[0]
        self._player_2_store_index = self._mancala_board[7]
        # Player names
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
        # Returns the status of Player 1
        print("\nPlayer 1: ")
        print("Number of seeds in Player 1's Store: " + str(self._player_1_store_index))
        print("Player 1 Pits..:")
        print(str(self._mancala_board[1:7]))

        # Returns the Status of Player 2
        print("\nPlayer 2: ")
        print("Number of seeds in Player 2's Store: " + str(self._player_2_store_index))
        print("Player 2 Pits:")
        print(str(self._mancala_board[8:14]))

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

    def move_seed_per_pit(self, pit_index, store_index):
        """
        Distributes/drops a seed per each index pass of the Mancala board array.
        """
        # Grabs the amount of seeds from a pit.
        amount_of_seeds = self.grab_seeds(pit_index)

        # To begin dropping seeds into next pit, increment pit index by 1
        pit_index = pit_index + 1

        while amount_of_seeds > 0:
            # Decrease amount of seeds by one per each pit
            amount_of_seeds -= 1
            pit_index += 1
            # Add seed to indexed pits
            self._mancala_board[pit_index] += 1

        # Move amount of seeds to Store
        if self._mancala_board[pit_index] == 0:
            store_index += amount_of_seeds

        return pit_index

    def steal_player_seeds(self, pit_index, store_index):
        """

        :param store_index:
        :param pit_index:
        :return:
        """
        if self._mancala_board[pit_index] == 0:
            self._mancala_board[store_index] = self._mancala_board[pit_index+7]
            self._mancala_board[pit_index+7] = 0

        # Return something here
        return store_index

    def special_rule_1(self, player_number, pit_index, score_index):
        """
        When the last seed in the hand lands in your own store, take another turn.
        """
        print(player_number + " takes another turn")

    def play_game(self, player_number, pit_index):
        """
        Player moves seeds across the board.
        """
        print("\nPlayer " + str(player_number) + " takes a turn")

        # Gather the number of seeds
        if pit_index >= 1 and pit_index <= 6:

            # Player 1
            if player_number == 1:

                # CHANGED FROM PIT+NUMBER TO PIT INDEX #
                # MAY NOT NEED #
                # pit_index = pit_index
                # MAY NOT NEED #

                num_of_seeds = self._mancala_board[pit_index]

                # Gather the number of seeds, and distribute them across each move
                grab_seed_amount = self.grab_seeds(pit_index)
                pit_index = self.move_seed_per_pit(pit_index, self._player_1_store_index)

                # If Player 1 lands on empty space of their own and opposite (Player 2) pit contains seeds
                self.steal_player_seeds(pit_index, self._player_1_store_index)

                # Apply special rule number 1
                if self._mancala_board[pit_index] == 1 and self._mancala_board[self._player_1_store_index]:
                    self.special_rule_1(player_number, pit_index, self._player_1_store_index)

            # Player 2
            if player_number == 2:
                # Add seven to get appropriate pit number
                pit_index = pit_index + 7
                num_of_seeds = self._mancala_board[pit_index + 7]

                # Gather the number of seeds, and distribute them across each move
                grab_seed_amount = self.grab_seeds(pit_index)
                self.move_seed_per_pit(pit_index, self._player_2_store_index)

                # If Player 2 lands on empty space of their own and opposite (Player 1) pit contains seeds
                pit_index = self.steal_player_seeds(pit_index, self._player_2_store_index)

                # Apply special rule number 1
                if self._mancala_board[pit_index] == 1 and self._mancala_board[self._player_2_store_index]:
                    self.special_rule_1(player_number, pit_index, self._player_2_store_index)

            # Prints the updated Mancala game
            print("The Mancala board now looks like this.")
            print(self._mancala_board[0], ' ', self._mancala_board[1:7])
            print('   ', self._mancala_board[8:14], ' ', self._mancala_board[7])

        elif pit_index >= 6 or pit_index <= 0:
            return "Invalid number for pit index."

        # RETURN WINNER????????
        # self.return_winner()


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
p1 = game.create_players('Ari')
p2 = game.create_players('Milky')
# print(p1.get_player_name())     # Prints Ari
# print(p2.get_player_name())     # Prints Milky
game.play_game(1, 1)            # Player 1 takes a turn, prints board array in unique design
# game.play_game(2, 1)            # Player 2 takes a turn, prints board array in unique design
# print(game.return_winner())   # Game has not ended
# game.play_game(1, 2)
# game.play_game(1, 3)
# game.play_game(1, 4)
# game.play_game(1, 5)
# game.play_game(1, 6)
# game.play_game(2, 6)
# game.play_game(2, 5)
# game.play_game(2, 4)
# game.play_game(2, 3)
# game.play_game(2, 2)
# game.play_game(2, 1)
print(game.print_board())
