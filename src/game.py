import random
from src.player import HumanPlayer, ComputerPlayer


class TicTacToe:
    """
    The TicTacToe game class which is responsible for keeping track of the players moves,
    the current board state, the current remaining valid moves, remaking the board state and 
    remaining available moves after each game and checking if any player met the win condition
    after each move. 

    :param board_ui: Gives access to the Board_Ui class which is resposible for the Ui of the game
    :type board_ui: BoardUi
    """
    def __init__(self, board_ui):
        """
        Intiializes the TicTacToe game instance

        Sets up the board and the available moves, which start out as the same.
        The board gets filled with each players symbols while the moves in available_moves get
        slowly removed as the board gets filled up, and initializes the winning_tiles list which stays
        empty until the win condition is reached.

        :param board_ui: An instance of the BoardUi class so that the the ui of the game can be modified
                         based on the users actions
        :type board_ui: BoardUi
        """
        self.board = [i + 1 for i in range(9)]
        self.available_moves = [i + 1 for i in range(9)]
        self.board_ui = board_ui
        self.winning_tiles = []

    def remake_board(self):
        """
        Whenever a game is completed the board and available_moves get reset back to 
        their original states to prepare for the next game.
        """
        self.board = [i + 1 for i in range(9)]
        self.available_moves = [i + 1 for i in range(9)]

    def make_move(self, move, symbol):
        """
        In charge of recording the move thats made

        Whenever a button in the self.board_ui.window.board_tiles list is pressed it updates
        the self.board list with the symbol of the player who pressed it and removes the index of
        the button that was pressed from the self.available_moves list.

        :param move: The index of the button that was clicked
        :type move: int

        :param symbol: The symbol of the player that made the move
        :type symbol: string
        """
        self.board[move - 1] = symbol
        self.available_moves.remove(move)

    def check_for_win(self):
        """
        After each move checks the self.board list if it has met any of the win conditions
        if a win condition is met also creates a self.winning_tiles list with the tiles
        that met the win condition to be used in the board_ui class instance

        :return: If a win condition is met returns True, if its not returns False
        :rtype: bool
        """

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
    """
    Responsible for handling all of the game logic and making it a action based application
    based off of the buttons that are clicked in the BoardUi class
    """
    def __init__(self, game):
        """
        Initializes the Play object
        
        Initializes the player objects in a class so they can be indexed into easily, sets up
        a toggle list to track which players turn it is by toggling between those two options 
        and using it to index into the self.players list. Sets up the connections for the 
        game.window.board_tiles so they can listen for the signal that gets emitted when one
        of them gets clicked. 

        :param game: An object instance of the game class which gives this class access to the
                     BoardUi class and the QMainWindow class inside of that.
        :type game: Play object
        """
        self.game = game
        self.players = [HumanPlayer(), ComputerPlayer()]
        self.current_player_choice = self.select_first_player()

        self.setup_connections()
        self.game.board_ui.button_clicked.connect(self.board_button_click)

    def setup_connections(self):
        """
        Sets up a connection to the start_game_button QPushButton that starts the game and
        switches to the game tab whenever the button is clicked.
        """
        self.game.board_ui.window.start_game_button.clicked.connect(
            self.start_game_button
        )

    def start_game_button(self):
        """
        Changes the current tab index to the game tab, updates self.players with the selected
        player objects so that the user can play with another human or against the cpu,sets the 
        symbols for each player based off of whoever gets to go first,sets the game labels based 
        on the players and their symbols, highlights which player gets to go first.
        """
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
            self.game_logic()

    def board_button_click(self, button):
        """
        Whenever a QPushButton in the self.game.board_ui.window.board_tiles is pressed 
        it saves that current button to a variable and calls the game_logic function
        which takes advantage of that button. The reason its not passed into the game_logic 
        function directly is because the CPU doesn't actually press the button. It just 
        simulates a press programmatically

        :param button: The actual QPushButton object that was clicked
        :type button: QPushButton
        """
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
        """
        Sets the symbols for each player object

        As per the rules of TicTacToe the first player will always be 'X' which leaves
        the player who gets to act second with the 'O' symbol 
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
        """
        The main function in charge of the game logic.

        In charge of making the moves and making sure both the ui and the lists in
        the game object instance get updated properly, checks for a win condition after
        every move, if the win condition is not met, checks if the board has any more 
        remaining free tiles. If it does it and its a HumanPlayers turn it waits for them
        to click on a tile to repeat, if its a CPU's turn it automatically repeats the function
        """
        current_player = self.players[self.current_player_choice]
        # Gets the symbol for the current player so it can be applied to the button
        symbol = current_player.get_symbol()

        # Resets the font style of the game label so it can be set only to the current player
        self.game.board_ui.reset_game_label()

        # If the current_player is a CPU then programatically simulates a click 
        if isinstance(current_player, ComputerPlayer):
            move = current_player.make_move(self.game.available_moves)
            button = self.game.board_ui.window.board_tiles[move - 1]

        # If the current player is a human then the button is selected by whatever they click on
        elif isinstance(current_player, HumanPlayer):
            move = current_player.make_move(self.current_button)
            button = self.game.board_ui.window.board_tiles[move - 1]

        # Makes a move on both the board_ui and the game objects.
        self.game.board_ui.make_move(button, symbol)
        self.game.make_move(int(move), symbol)

        # Checks if the win condition was met afte the move
        if self.game.check_for_win():
            # If it was disable all tiles and highlight the tiles that met the win condition
            self.game.board_ui.disable_all_tiles()
            self.game.board_ui.display_winning_tiles(self.game.winning_tiles)

            # Delay reseting the board so the users can see what tiles met the win condition
            self.game.board_ui.delay_action(1500, self.declare_winner)

        # If self.game.available_moves is empty it means there are no more moves and its a tie
        elif len(self.game.available_moves) == 0:

            # Delays reseting the board for a bit less because there is nothing to see
            self.game.board_ui.delay_action(1000, self.declare_tie_game)

        # If the win condition is not met and there are more remaining moves then swap the player
        # and swap the label highlight to display the opposite player
        else:
            self.game.board_ui.display_current_player_game_label(
                self.current_player_choice - 1
            )
            self.swap_current_player()

            # If the new current player is a CPU then call game_logic again.
            if isinstance(self.players[self.current_player_choice], ComputerPlayer):
                self.game_logic()

    def reset_game(self):
        """
        Resets the game back to its original state both in the game object instance and
        in the game.board_ui object instance

        Randomly selects the first player again, sets the symbols again for the new first player
        resets new style on the winning tiles back to their original state and enables all the 
        board tiles that were disabled after they've been clicked and removes the symbols from them.
        """
        self.current_player_choice = self.select_first_player()
        self.set_symbols()
        self.game.board_ui.reset_winning_tiles(self.game.winning_tiles)
        self.game.remake_board()
        self.game.board_ui.finish_current_game()

    def declare_winner(self):
        """
        If a win condition is reached sets up th winning player string, updates the 
        results_labels on the Menu Tab and updates the winning players score by adding 1,
        and then resets the game so that it can be played again without restarting.
        """
        results_text = f"Player {self.current_player_choice + 1} Wins!"
        self.game.board_ui.update_results_label(results_text)
        self.game.board_ui.update_score(self.current_player_choice)
        self.reset_game()

    def declare_tie_game(self):
        """
        If game.availabe_moves runs out before a win condition is met then declare a tie
        The text displayed on the Menu Tab shows that it's a tie game, the player scores don't 
        get updated and the game resets to prepare for the next game.
        """
        results_text = "Tie Game"
        self.game.board_ui.update_results_label(results_text)
        self.reset_game()
