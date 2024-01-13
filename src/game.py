import random


class TicTacToe:
    # find out what type board_ui is for the annotation
    def __init__(self, board_ui):
        self.board = [i + 1 for i in range(9)]
        self.available_moves = [i + 1 for i in range(9)]
        self.board_ui = board_ui

    def make_move(self, move, symbol):
        self.board[move - 1] = symbol
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
                return True

        # Vertical Win Condition
        for i in range(0, 3):
            h_row = set([self.board[i], self.board[i + 3], self.board[i + 6]])
            if len(h_row) == 1:
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
        self.init_symbols()

        self.setup_connections()
        self.game.board_ui.button_clicked.connect(self.board_button_click)

    def setup_connections(self):
        self.game.board_ui.window.start_game_button.clicked.connect(
            self.start_game_button
        )

    def start_game_button(self):
        self.game.board_ui.window.tab_menu.setCurrentIndex(1)

    def board_button_click(self, button):
        move = str(button.objectName()).split("_")[1]
        self.game_logic(button, move)
        # player_symbol = self.players[self.current_player_choice]
        # print(str(button.objectName()).split('_')[1])
        # button.setText('X')

    def select_first_player(self):
        return random.choice(self.players_index)

    def init_symbols(self):
        self.players[self.current_player_choice].set_symbol("X")
        self.players[self.current_player_choice - 1].set_symbol("O")

    def swap_current_player(self):
        if self.current_player_choice == 0:
            self.current_player_choice = 1
        else:
            self.current_player_choice = 0

    def game_logic(self, button, move):
        current_player = self.players[self.current_player_choice]
        symbol = current_player.get_symbol()
        button.setText(symbol)
        self.game.make_move(int(move), symbol)

        if self.game.check_for_win():
            self.declare_winner()

        elif len(self.game.available_moves) == 0:
            self.declare_tie_game()

        else:
            self.swap_current_player()

    def declare_winner(self):
        print(f"winner = {self.players[self.current_player_choice]}")
        self.game.board_ui.finish_current_game()

    def declare_tie_game(self):
        pass

    def reset_board_state(self):
        pass
        # resets board, tiles and available moves back to base
