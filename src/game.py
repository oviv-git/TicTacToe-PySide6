import random
from src.player import HumanPlayer, ComputerPlayer


class TicTacToe:
    # find out what type board_ui is for the annotation
    def __init__(self, board_ui):
        self.board = [i + 1 for i in range(9)]
        self.available_moves = [i + 1 for i in range(9)]
        self.board_ui = board_ui

    def remake_board(self):
        self.board = [i + 1 for i in range(9)]
        self.available_moves = [i + 1 for i in range(9)]

    def make_move(self, move, symbol):
        self.board[move - 1] = symbol
        print(move, symbol)
        print(self.available_moves)
        self.available_moves.remove(move)

    def check_for_win(self):
        print("moves", self.available_moves)
        for i in range(0, 9, 3):
            print(self.board[i : i + 3])
        print("")

        # Horizontal Win Condition
        for i in range(0, 9, 3):
            row = set(self.board[i : i + 3])
            if len(row) == 1:
                print(i)
                return True

        # Vertical Win Condition
        for i in range(0, 3):
            column = set([self.board[i], self.board[i + 3], self.board[i + 6]])
            if len(column) == 1:
                print(i)
                return True

        # Left Diagonal Win
        l_diagonal = set([self.board[0], self.board[4], self.board[8]])
        if len(l_diagonal) == 1:
            return True

        # Right Diagonal Win
        r_diagonal = set([self.board[2], self.board[4], self.board[6]])
        if len(r_diagonal) == 1:
            return True
        return False


class Play:
    def __init__(self, game, player_1, player_2):
        self.game = game
        self.players = [player_1, player_2]
        self.players_index = [0, 1]
        self.current_player_choice = self.select_first_player()
        self.set_symbols()
        self.cpu = player_2

        self.setup_connections()
        self.game.board_ui.button_clicked.connect(self.board_button_click)

    def setup_connections(self):
        self.game.board_ui.window.start_game_button.clicked.connect(
            self.start_game_button
        )

    def start_game_button(self):
        self.game.board_ui.window.tab_menu.setCurrentIndex(1)
        current_player = self.players[self.current_player_choice]
        print(current_player)
        if isinstance(current_player, ComputerPlayer):
            self.game_logic()

    def board_button_click(self, button):
        self.current_button = button
        self.game_logic()
        # player_symbol = self.players[self.current_player_choice]
        # print(str(button.objectName()).split('_')[1])
        # button.setText('X')

    def select_first_player(self):
        return random.choice(self.players_index)

    def set_symbols(self):
        self.players[self.current_player_choice].set_symbol("X")
        self.players[self.current_player_choice - 1].set_symbol("O")

    def swap_current_player(self):
        if self.current_player_choice == 0:
            self.current_player_choice = 1
        else:
            self.current_player_choice = 0

    def game_logic(self):
        current_player = self.players[self.current_player_choice]
        symbol = current_player.get_symbol()

        if isinstance(current_player, ComputerPlayer):
            move = current_player.make_move(self.game.available_moves)
            button = self.game.board_ui.window.board_tiles[move - 1]

        elif isinstance(current_player, HumanPlayer):
            move = current_player.make_move(self.current_button)
            button = self.game.board_ui.window.board_tiles[move - 1]

        self.game.make_move(int(move), symbol)
        self.game.board_ui.make_move(button, symbol)

        if self.game.check_for_win():
            self.declare_winner()

        elif len(self.game.available_moves) == 0:
            self.declare_tie_game()

        else:
            self.swap_current_player()
            if isinstance(self.players[self.current_player_choice], ComputerPlayer):
                self.game_logic()

    def reset_game(self):
        self.current_player_choice = self.select_first_player()
        self.set_symbols()
        self.game.remake_board()
        self.game.board_ui.finish_current_game()

    def declare_winner(self):
        self.game.board_ui.disable_all_tiles()
        # self.game.board_ui.delay_action(1000, self.reset_game)
        self.reset_game()

    def declare_tie_game(self):
        self.reset_game()
