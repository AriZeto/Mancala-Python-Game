# Author: Ari Zeto
# GitHub username: AriZeto
# Date: 11/29/2022
# Description: Fill in Later!!! MISSING DECENT AMOUNT OF COMMENTS/DOCUMENTATION

class Mancala:
    """
    Class representing the board game dubbed 'Mancala'. Contains information regarding the Board status as well as
    information regarding player names.
    """
    def __init__(self):
        # Index 6 represents Player 1 Store, Index 13 represents Player 2 Store
        # Index 0 through 5 represents Player 1 Seeds, Index 7 through 12 represents Player 2 Seeds
        # Each pit contains four seeds

        ########### INDEX SPORE FOR PLAYER 2 NOT WORKING #####################
        self._mancala_board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        self._player_1_store_index = 6
        self._player_2_store_index = 13
        # Player names
        self._player_1 = ''
        self._player_2 = ''
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
        print("Player 1: ")
        print("Number of seeds in Player 1's Store: " + str(self._mancala_board[self._player_1_store_index]))
        print("Player 1 Pits..:")
        print(str(self._mancala_board[0:6]))

        # Returns the Status of Player 2
        print("Player 2: ")
        print("Number of seeds in Player 2's Store: " + str(self._mancala_board[self._player_2_store_index]))
        print("Player 2 Pits:")
        print(str(self._mancala_board[7:13]))

        # Return the winner
        return self.return_winner()


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


    def move_seed_per_pit(self, pit_index, store_index, opponent_store_index):
        """
        Distributes/drops a seed per each index pass of the Mancala board array.
        """
        # Grabs the amount of seeds from a pit.
        amount_of_seeds = self.grab_seeds(pit_index)

        # print(opponent_store_index)
        while amount_of_seeds > 0:

            if pit_index >= 13:
                pit_index = 0
            else:
                pit_index += 1

            ####### FIX THIS ##############
            if pit_index != opponent_store_index:
                # Decrease amount of seeds by one per each pit
                amount_of_seeds -= 1

                if amount_of_seeds == 0 and self._mancala_board[pit_index] == 0 and pit_index != self._player_1_store_index and pit_index != self._player_2_store_index:


                    # Add seed to indexed pits
                    self._mancala_board[store_index] += 1         # test


                    # print("store index value", self._mancala_board[store_index])
                    self.steal_player_seeds(pit_index, store_index)

                    # print(self._mancala_board[store_index])
                else:
                    # Add seed to indexed pits
                    self._mancala_board[pit_index] += 1

        return pit_index


    def steal_player_seeds(self, pit_index, store_index):
        """

        :param store_index:
        :param pit_index:
        :return:
        """
        # print("meow", self._mancala_board[pit_index+7])
        # print(self._mancala_board[store_index])
        self._mancala_board[store_index] += self._mancala_board[self._index_opposites[pit_index]]
        self._mancala_board[self._index_opposites[pit_index]] = 0


        # Return something here
        return store_index


    def take_another_turn(self, player_number):
        """
        When the last seed in the hand lands in your own store, take another turn.
        """
        print(f"player {player_number} takes another turn")


    # def special_rule_2(self, player_number, pit_index, store_index):
    #     """
    #     When the last seed in your hand lands in one of your own empty pits, get to keep all the seeds in your opponents
    #     opposite pit. The captured seeds as well as the last seed from your hand gets to go into your player store.
    #     :return:
    #     """
    #     # NOT SURE IF THIS IS CORRECT ! ! ! ! ! ! ! ! !
    #     if self._mancala_board[pit_index] == 1 and self._mancala_board[pit_index + 1] == 0:
    #         if self._mancala_board[pit_index + 7] != 0:
    #             grab_opposite_seeds = self.grab_seeds(pit_index + 7)
    #             grab_player_seed = self.grab_seeds(pit_index)
    #
    #             # Add your final seed and opposite pit/other player seeds to your store.
    #             self._mancala_board[store_index] += grab_opposite_seeds + grab_player_seed
    #             print("\n Player" + {player_number} + " Just stole seeds from your pit!")


    def set_indexed_pit_to_0(self, player_number):
        """
        Sets the chosen pit to zero after selecting it to move across the board.
        :param pit_index:
        :return:
        """
        return (f"This pit is empty! Choose a different pit, Player {player_number}.")


    # def skip_opponent_store(self, pit_index, store_index):
    #     """
    #     Skips the opponents turn when passing.
    #     :return:
    #     """
    #     # FILL THIS IN!
    #     if self._mancala_board[pit_index] != 0 and self.move_seed_per_pit(pit_index, store_index):
    #         self._mancala_board[pit_index] = self.move_seed_per_pit(pit_index+1, store_index)

    def play_game(self, player_number, pit_index):
        """
        Player moves seeds across the board.
        """

        ##### WORKS WITHOUT THIS (STILL TRYING TO FIGURE OUT WHY) #####
        # elif player_number == 2 and self._mancala_board[pit_index - 1] == 0:
        #     return self.set_indexed_pit_to_0(player_number)

        ##### NEEDS TO BE FIXED. IF PIT IS 0 IT DOES NOT WORK #########
        if pit_index > 6 or pit_index <= 0:
            return "Invalid number for pit index"

        # If one of the rows is zeroed out completely, return message that the game has ended.
        if self.if_row_zero(self._mancala_board[0:6]) or self.if_row_zero(self._mancala_board[7:13]):
            return "Game is ended"

        # Gather the number of seeds
        if pit_index >= 1 and pit_index <= 6:

            # Player 1
            if player_number == 1:

                # If Pit contains no seeds
                pit_index -= 1
                if self._mancala_board[pit_index] == 0:
                    return self.set_indexed_pit_to_0(player_number)

                # print("\nplayer " + str(player_number) + " takes a turn.")

                num_of_seeds = self._mancala_board[pit_index]

                # Distribute them across each move
                landed_pit_index = self.move_seed_per_pit(pit_index, self._player_1_store_index, self._player_2_store_index)

                # # If Player 1 lands on empty space of their own and opposite (Player 2) pit contains seeds
                # self.steal_player_seeds(landed_pit_index, self._player_1_store_index)

                # # Apply special rule number 1
                # if self._mancala_board[landed_pit_index] == 1 and self._player_1_store_index == landed_pit_index:
                #     self.special_rule_1(player_number)
                #
                # # SPECIAL RULE 2 #
                # self.special_rule_2(player_number, pit_index, self._player_1_store_index)

            # Player 2
            if player_number == 2:
                # Add seven (six?) to get appropriate pit number
                pit_index = pit_index + 6

                # If Pit contains no seeds
                if self._mancala_board[pit_index] == 0:
                    return self.set_indexed_pit_to_0(player_number)

                # print("\nplayer " + str(player_number) + " takes a turn.")

                ### Go around board ###
                # if self._mancala_board[pit_index] >= self._mancala_board[pit_index + 6]:
                #     num_of_seeds = self._mancala_board[pit_index]

                # Go around the board
                # if self._mancala_board[pit_index] >= self._mancala_board[pit_index + 6]:
                #     pit_index = 0

                # Distribute them across each move
                landed_pit_index = self.move_seed_per_pit(pit_index, self._player_2_store_index, self._player_1_store_index)

                # # If Player 2 lands on empty space of their own and opposite (Player 1) pit contains seeds
                # self.steal_player_seeds(landed_pit_index, self._player_2_store_index)

                # # Apply special rule number 1
                # if self._mancala_board[landed_pit_index] == 1 and self._player_2_store_index == landed_pit_index:
                #     self.special_rule_1(player_number)
                #
                # # SPECIAL RULE 2 #
                # self.special_rule_2(player_number, pit_index, self._player_2_store_index)

            # Prints the updated Mancala game
            # print("\nThe Mancala board now looks like this.")
            # print(self._mancala_board[self._player_2_store_index], ' ', self._mancala_board[7:13])
            # print('   ', self._mancala_board[0:6], ' ', self._mancala_board[self._player_1_store_index])


            # print(self._mancala_board)

            if player_number == 1:
                # Apply special rule number 1
                if self._mancala_board[landed_pit_index] == 1 and self._player_1_store_index == landed_pit_index:
                    self.take_another_turn(player_number)

            elif player_number == 2:
                # Apply special rule number 1
                if self._mancala_board[landed_pit_index] == 1 and self._player_2_store_index == landed_pit_index:
                    self.take_another_turn(player_number)

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
