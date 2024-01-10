import random

class TicTacToe:
    # find out what type board_ui is for the annotation
    def __init__(self, board_ui):
        self.board = [i + 1 for i in range(9)]
        self.available_moves = [i + 1 for i in range(9)]
        self.board_ui = board_ui
        print(board_ui)

    def make_move(self, move, symbol):
        self.board[move - 1] = symbol
        self.available_moves.remove(move)

    def check_for_win(self):
        print('moves', self.available_moves)
        for i in range(0,9,3):
            print(self.board[i: i+3])
        print('')

        # Horizontal Win Condition
        for i in range(0,9,3):
            row = set(self.board[i: i+3])
            if len(row) == 1:
                return True

        # Vertical Win Condition
        for i in range(0,3):
            h_row = set([self.board[i], self.board[i+3], self.board[i+6]])
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

        self.set_players = [player_1, player_2]
        self.current_player_list = [0, 1]
        self.current_player_choice = self.select_first_player()
        self.game_logic()

    @property
    def set_players(self):
        return self._players

    @set_players.setter
    def set_players(self, players_list):
        self.player_1 = players_list[0]
        self.player_1.set_symbol("X")

        self.player_2 = players_list[1]
        self.player_2.set_symbol("O")

        self._players = [self.player_1, self.player_2]

    def select_first_player(self):
        current_player_choice = random.choice(self.current_player_list)
        return current_player_choice


    def swap_current_player(self):
        print(self.current_player_choice)
        if self.current_player_choice == 0:
            self.current_player_choice = 1
        else:
            self.current_player_choice = 0
        

    def game_logic(self):
        while True:
            player_move = self.set_players[self.current_player_choice].make_move()
            player_symbol = self.set_players[self.current_player_choice].get_symbol()
            self.game.make_move(player_move, player_symbol)
            
            if self.game.check_for_win():
                break
            
            if len(self.game.available_moves) == 0:
                print('Tie Game')
                break
            
            self.swap_current_player()
            continue
        self.declare_winner()

    def declare_winner(self):
        print(f"winner = {self.set_players[self.current_player_choice]}")

