<<<<<<< HEAD
import sys
import random
from player import HumanPlayer
from itertools import cycle


class TicTacToe:
    def __init__(self):
        self.board = [i + 1 for i in range(9)]
        self.available_moves = [i + 1 for i in range(9)]

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

        


def main():
    game = TicTacToe()
    player_1 = HumanPlayer()
    player_2 = HumanPlayer()
    play = Play(game, player_1, player_2)


if __name__ == "__main__":
    main()
=======
import random
from player import RandomComputerPlayer, HumanPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('[' + ']['. join(row) + ']')
        

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3+1, (j+1)*3+1)] for j in range(3)]
        for row in number_board:
            print('[' + ']['.join(row) + ']')
            
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')
        
    def first_player(self):
        return self.first_move == random.choice(['X', 'O'])

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):

def play(game, first_player, second_player, print_game=True):
    user_letter = None
    x_player = None
    o_player = None
    if print_game:
        game.print_board_nums()
    while user_letter not in ['X', 'O']:
        user_letter = str(input("Would you like to be X's or O's: ")).upper()
        if user_letter == 'X':
            x_player = HumanPlayer
            o_player = RandomComputerPlayer
            break
        else:
            x_player = RandomComputerPlayer
            o_player = HumanPlayer
            break
    
    if game.make_move(square, letter):
        if print_game:
            print({letter} + f' makes a move to square {square}')
            game.print_board()
            print("") # Just empty line

            letter = 'O' if game.first_move == 'O' else "X"
            
    if game.current_winner:
        if print_game:
            print(letter + ' wins!')
        return letter

    if print_game:
        print('It\'s a tie!')

t = TicTacToe()

# t.print_board_nums()
# t.print_board()
# t.available_moves()

play(TicTacToe, HumanPlayer, RandomComputerPlayer, print_game = True)
input("Press Enter to Exit")
>>>>>>> 4797b605031721fbed7998963c66265766f484a2
