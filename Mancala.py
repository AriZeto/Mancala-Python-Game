# Author: Ari Zeto
# GitHub username: AriZeto
# Date: 12/3/2022
# Description: Fill in Later!!! MISSING DECENT AMOUNT OF COMMENTS/DOCUMENTATION

class Mancala:
    """
    Class representing the board game dubbed 'Mancala'. Contains information regarding the board, such as the player
    pits, their store, as well as opposite pit indexes.
    """
    def __init__(self):
        # Index 6 represents Player 1 Store, Index 13 represents Player 2 Store
        # Index 0 through 5 represents Player 1 Seeds, Index 7 through 12 represents Player 2 Seeds
        # Each pit contains a default of four seeds, each store contains a default of 0 seeds.
        self._mancala_board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

        # Define player store indexes for easy access
        self._player_1_store_index = 6
        self._player_2_store_index = 13

        # Player names defaulted to the empty string, to be initialized.
        self._player_1 = ''
        self._player_2 = ''

        # A dictionary containing the key's as the player pit index, values as opposite player pit index
        self._index_opposites = {
            # (Player 1) key is their pit, value is player 2 pit
            0:12,
            1:11,
            2:10,
            3:9,
            4:8,
            5:7,

            # (Player 2) key is their pit, value is player 1 pit
            7:5,
            8:4,
            9:3,
            10:2,
            11:1,
            12:0
        }


    def create_player(self, name):
        """
        Takes as a parameter the name of the Player and returns the player object.
        """

        # Create a Player object with parameter as their name.
        player_char = Player(name)

        # As long as the player name is empty (which it will be), set player name to 'name' passed in and return object
        if self._player_1 == '':
            self._player_1 = name
        elif self._player_2 == '':
            self._player_2 = name
        return player_char


    def print_board(self):
        """
        Contains no parameters. Prints specific formatted board information, such as the status of each
        player, such as how many seeds are in their store, as well as the seeds in their pits. Returns the method
        'return_winner()' which indicates the status of the game.
        """
        # Returns the status of Player 1
        print("player1:")
        print("store: " + str(self._mancala_board[self._player_1_store_index]))
        print(str(self._mancala_board[0:6]))

        # Returns the Status of Player 2
        print("player2:")
        print("store: " + str(self._mancala_board[self._player_2_store_index]))
        print(str(self._mancala_board[7:13]))

        # Returns the winner or the status of the game.
        return self.return_winner()


    def grab_seeds(self, pit_index):
        """
        Takes as a parameter a particular indexed pit value of the Mancala Board array to 'grab' the amount of seeds
        within a particular pit. Returns the amount of seeds from that pit.
        """

        # To grab the amount of seeds from a pit index, use the pit index within the mancala board array, such that
        # it contains the 'amount' of seeds from that particular pit. Set to variable and return that amount.
        grab_seed_from_pit = self._mancala_board[pit_index]

        # Now, once the seeds have been picked up from that particular pit, set it equal to 0 such that the pit is empty.
        self._mancala_board[pit_index] = 0

        # Return the grabbed amount of seeds from that pit.
        return grab_seed_from_pit


    def move_seed_per_pit(self, pit_index, store_index, opponent_store_index):
        """
        Takes as parameters the pit index, the store index, and the opponent store index. These parameters are used
        such that the seeds can be distributed to the players pits, their own store, but skipping the opponent store.
        Returns the positioned pit index."""

        # Use the prior defined 'grab_seeds()' method and pass in the pit index to grab the amount of seeds from
        # the players chosen pit.
        amount_of_seeds = self.grab_seeds(pit_index)

        # As long as the seeds is greater than zero, loop through the Mancala board.
        while amount_of_seeds > 0:
            # Go back to beginning of the board if going past final mancala pit spot by setting pit index to 0.
            if pit_index >= 13:
                pit_index = 0
            else:
                # Otherwise, increment/move the pit index to go around the board.
                pit_index += 1

            # As long as pit index is not the opposite players store, to distribute the seeds we decrement the amount
            # by one.
            if pit_index != opponent_store_index:
                amount_of_seeds -= 1

                # If the amount of seeds in hand is 0, and the hand/pit we're looking over contains no pits;
                # and the hand is not over either player store, add the 'last seed in hand' to player store as well
                # as steal the seeds in the opposite pit (opposite player).
                if amount_of_seeds == 0 and self._mancala_board[pit_index] == 0 and pit_index != self._player_1_store_index and pit_index != self._player_2_store_index:

                    # Add seed to player store
                    self._mancala_board[store_index] += 1

                    # Steal the opposite pit
                    self.steal_player_seeds(pit_index, store_index)

                else:
                    # Otherwise, if the player hand contains seeds, distribute throughout the pit indexes.
                    self._mancala_board[pit_index] += 1

        # Return positioned pit index.
        return pit_index


    def end_game_store(self):
        """
        Takes no parameters. Once the game is over, this method updates the losing players store by allocating remaining
        seeds to the respective player store (and zeroing out the loser player pits).
        """

        # Update the losing player store. Checks first if any player rows are zeroed out.
        if self.if_row_zero(self._mancala_board[0:6]) or self.if_row_zero(self._mancala_board[7:13]):

            # Iterates over the player pits within the mancala board.
            for i in range(0, 6):
                # Update Player Store (after game is over, player who lost) by how many seeds within pit.
                self._mancala_board[self._player_1_store_index] += self._mancala_board[i]
                # Set player pits to 0 (after game is over, player who lost)
                self._mancala_board[i] = 0

            # Iterates over the player pits within the mancala board.
            for i in range(7, 13):
                # Update Player Store (after game is over, player who lost) by how many seeds within pit.
                self._mancala_board[self._player_2_store_index] += self._mancala_board[i]
                # Set player pits to 0 (after game is over, player who lost)
                self._mancala_board[i] = 0


    def steal_player_seeds(self, pit_index, store_index):
        """

        :param store_index:
        :param pit_index:
        :return:
        """
        self._mancala_board[store_index] += self._mancala_board[self._index_opposites[pit_index]]
        self._mancala_board[self._index_opposites[pit_index]] = 0


        # Return something here
        # return store_index


    # def take_another_turn(self, player_number):
    #     """
    #     When the last seed in the hand lands in your own store, take another turn.
    #     """
    #     print(f"player {player_number} takes another turn")


    def set_indexed_pit_to_0(self, player_number):
        """
        Sets the chosen pit to zero after selecting it to move across the board.
        :param pit_index:
        :return:
        """
        return (f"This pit is empty! Choose a different pit, Player {player_number}.")


    def play_game(self, player_number, pit_index):
        """
        Player moves seeds across the board.
        """


        if pit_index > 6 or pit_index <= 0:
            return "Invalid number for pit index"

        # If one of the rows is zeroed out completely, return message that the game has ended.
        if self.if_row_zero(self._mancala_board[0:6]) or self.if_row_zero(self._mancala_board[7:13]):
            return "Game is ended"

        # Gather the number of seeds
        if pit_index >= 1 and pit_index <= 6:

            # Player 1
            if player_number == 1:
                # Subtract from index to get appropriate pit index
                pit_index -= 1

                # If Pit contains no seeds
                if self._mancala_board[pit_index] == 0:
                    return self.set_indexed_pit_to_0(player_number)

                # num_of_seeds = self._mancala_board[pit_index]

                # Distribute them across each move
                landed_pit_index = self.move_seed_per_pit(pit_index, self._player_1_store_index, self._player_2_store_index)


            # Player 2
            if player_number == 2:
                # Add seven (six?) to get appropriate pit index
                pit_index += 6

                # If Pit contains no seeds
                if self._mancala_board[pit_index] == 0:
                    return self.set_indexed_pit_to_0(player_number)

                # Distribute them across each move
                landed_pit_index = self.move_seed_per_pit(pit_index, self._player_2_store_index, self._player_1_store_index)


            if player_number == 1:
                # Apply special rule number 1
                if self._mancala_board[landed_pit_index] == 1 and self._player_1_store_index == landed_pit_index:
                    print("player 1 take another turn")

            elif player_number == 2:
                # Apply special rule number 1
                if self._mancala_board[landed_pit_index] == 1 and self._player_2_store_index == landed_pit_index:
                    print("player 2 take another turn")

        # Tally up any remaining pits once game is over and add to other player store.
        self.end_game_store()

        return self._mancala_board


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
        if self.if_row_zero(self._mancala_board[0:6]) or self.if_row_zero(self._mancala_board[7:13]):
            if self._mancala_board[self._player_1_store_index] > self._mancala_board[self._player_2_store_index]:
                return "Winner is player 1: " + self._player_1
            elif self._mancala_board[self._player_1_store_index] < self._mancala_board[self._player_2_store_index]:
                return "Winner is player 2: " + self._player_2
            elif self._mancala_board[self._player_1_store_index] == self._mancala_board[self._player_2_store_index]:
                return "It's a tie"
        else:
            return "Game has not ended"


class Player:
    """
    A class representing the Player. Contains the characteristic of the Player 1 or 2's name.
    """
    def __init__(self, name):
        self._name = name


    def get_player_name(self):
        """
        Returns the name of a Mancala Player.
        """
        return self._name


# CREATE MANCALA PROJECT
# game = Mancala()

# CHECKS IF CREATE PLAYER WORKS
# p1 = game.create_player('Ari')
# p2 = game.create_player('Milky')

# Return Player Names
# print(p1.get_player_name())     # Works, Prints Ari
# print(p2.get_player_name())     # Works, Prints Milky

# PLAYER 1 TESTS
# print(game.play_game(1, 0))       # Works, returns Invalid number for pit index
# print(game.play_game(1, 1))       # Works
# print(game.play_game(1, 1))
# print(game.play_game(1, 2))
# print(game.play_game(2, 1))
# print(game.play_game(1, 1))       # Works, returns pit is empty if already chosen
# print(game.play_game(1, 2))         # Works
# print(game.play_game(1, 3))         # Works, returns player gets another turn, adds to correct store
# print(game.play_game(1, 4))       # Works, adds to correct store
# print(game.play_game(1, 5))         # Works
# print(game.play_game(1, 6))       # Works
# print(game.play_game(1, 7))         # Works, returns Invalid number for pit index

# PLAYER 2 TESTS
# print(game.play_game(2, 0))         # Works, returns Invalid number for pit index
# print(game.play_game(2, 1))         # Works
# print(game.play_game(2, 1))             # Works, returns pit is empty if already chosen
# print(game.play_game(2, 2))            # Works
# print(game.play_game(2, 3))             # WOrks, returns player gets another turn, adds to correct store
# print(game.play_game(2, 4))             # Works, adds to store as passes by,
# print(game.play_game(2, 5))         # Works
# print(game.play_game(2, 6))       # Works
# print(game.play_game(2, 7))         # Works, returns Invalid number for pit index

# CHECKS IF RETURN WINNER WORKS
# print(game.return_winner())         # Works for all conditions

# CHECKS IF PRINT BOARD WORKS
# print(game.print_board())           # Works for all conditions (manually changing array and game)
#
# print(game.play_game(1, 6))

# print(game._mancala_board)
# print(game.play_game(1, 5))
# print(game.play_game(1, 1))

# print(game.play_game(1, 1))
# print(game.play_game(1, 2))
# print(game.play_game(1, 3))
# print(game.play_game(1, 4))
# print(game.play_game(1, 5))
# print(game.play_game(1, 6))
# game.print_board()
# print(game.return_winner())