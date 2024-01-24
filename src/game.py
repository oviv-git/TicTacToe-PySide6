import random
import time
from src.player import HumanPlayer, ComputerPlayer


class TicTacToe:
    # find out what type board_ui is for the annotation
    def __init__(self, board_ui):
        self.board = [i + 1 for i in range(9)]
        self.available_moves = [i + 1 for i in range(9)]
        self.board_ui = board_ui
        self.winning_tiles = []

    def remake_board(self):
        self.board = [i + 1 for i in range(9)]
        self.available_moves = [i + 1 for i in range(9)]
        # self.winning_tiles = []

    def make_move(self, move, symbol):
        self.board[move - 1] = symbol
        self.available_moves.remove(move)

    def check_for_win(self):
        # Horizontal Win Condition
        for i in range(0, 9, 3):
            row = set(self.board[i : i + 3])
            if len(row) == 1:
                self.winning_tiles = [i + 1, i + 2, i + 3]
                return True

        # Vertical Win Condition
        for i in range(0, 3):
            column = set([self.board[i], self.board[i + 3], self.board[i + 6]])
            if len(column) == 1:
                self.winning_tiles = [i + 1, i + 4, i + 7]
                return True

        # Left Diagonal Win
        l_diagonal = set([self.board[0], self.board[4], self.board[8]])
        if len(l_diagonal) == 1:
            self.winning_tiles = [1, 5, 9]
            return True

        # Right Diagonal Win
        r_diagonal = set([self.board[2], self.board[4], self.board[6]])
        if len(r_diagonal) == 1:
            self.winning_tiles = [3, 5, 7]
            return True
        return False


class Play:
    def __init__(self, game):
        self.game = game
        self.players = [HumanPlayer(), ComputerPlayer()]
        self.current_player_choice = self.select_first_player()

        self.setup_connections()
        self.game.board_ui.button_clicked.connect(self.board_button_click)

    def setup_connections(self):
        self.game.board_ui.window.start_game_button.clicked.connect(
            self.start_game_button
        )

    def start_game_button(self):
        # The only way to change tabs is with the 'Start Game' button
        self.game.board_ui.window.tab_menu.setCurrentIndex(1)

        # Map to set the the proper player object based on the dropdown menu (QComboBox)
        playerMap = {"Human Player": HumanPlayer, "Computer Player": ComputerPlayer}
        self.players[0] = playerMap[
            self.game.board_ui.window.playerSelections[0].currentText()
        ]()
        self.players[1] = playerMap[
            self.game.board_ui.window.playerSelections[1].currentText()
        ]()

        # Uses random.choice on self.players_index to decide who goes first
        current_player = self.players[self.current_player_choice]
        self.set_symbols()

        # Sets up the labels based on the player types
        self.game.board_ui.set_game_labels(self.players)

        # Displays a visual queue to represent which players turn it is
        self.game.board_ui.display_current_player_game_label(self.current_player_choice)

        # If the current_player is a CPU then delay the action so its not instant
        if isinstance(current_player, ComputerPlayer):
            self.game.board_ui.delay_action(100, self.game_logic)

    def board_button_click(self, button):
        self.current_button = button
        self.game_logic()

    def select_first_player(self):
        """
        Randomly selects which player object goes first by choosing between 0,1

        :return: returns it to self.current_player_choice so it can be used to index
                 into the self.players list of player objects
        :rtype: int
        """
        return random.choice([0, 1])

    def set_symbols(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        self.players[self.current_player_choice].set_symbol("X")
        self.players[self.current_player_choice - 1].set_symbol("O")

    def swap_current_player(self):
        """
        Swaps the self.current_player_choice variable back and forth whenever its called
        so that the correct player object can be indexed from the self.players_list.
        """

        if self.current_player_choice == 0:
            self.current_player_choice = 1
        else:
            self.current_player_choice = 0

    def game_logic(self):
        current_player = self.players[self.current_player_choice]
        symbol = current_player.get_symbol()

        self.game.board_ui.reset_game_label()

        if isinstance(current_player, ComputerPlayer):
            move = current_player.make_move(self.game.available_moves)
            button = self.game.board_ui.window.board_tiles[move - 1]

        elif isinstance(current_player, HumanPlayer):
            move = current_player.make_move(self.current_button)
            button = self.game.board_ui.window.board_tiles[move - 1]

        self.game.board_ui.display_current_player_game_label(
            self.current_player_choice - 1
        )

        self.game.board_ui.make_move(button, symbol)
        self.game.make_move(int(move), symbol)

        if self.game.check_for_win():
            self.game.board_ui.disable_all_tiles()
            self.game.board_ui.display_winning_tiles(self.game.winning_tiles)
            self.game.board_ui.delay_action(1500, self.declare_winner)

        elif len(self.game.available_moves) == 0:
            self.declare_tie_game()

        else:
            self.swap_current_player()
            if isinstance(
                self.players[self.current_player_choice], ComputerPlayer
            ) and isinstance(
                self.players[self.current_player_choice - 1], ComputerPlayer
            ):
                self.game.board_ui.delay_action(200, self.game_logic)

            elif isinstance(self.players[self.current_player_choice], ComputerPlayer):
                self.game_logic()

    def reset_game(self):
        self.current_player_choice = self.select_first_player()
        self.set_symbols()
        self.game.remake_board()
        self.game.board_ui.finish_current_game()

    def declare_winner(self):
        results_text = f"Player {self.current_player_choice + 1} Wins!"
        self.game.board_ui.update_results_label(results_text)
        
        self.game.board_ui.update_score(self.current_player_choice)
        self.reset_game()

    def declare_tie_game(self):
        results_text = "Tie Game"
        self.game.board_ui.update_results_label(results_text)
        self.reset_game()
