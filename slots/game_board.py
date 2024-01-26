from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtWidgets import QPushButton


class BoardUi(QObject):
    """
    Responsible for managing the Ui elements of the game. Connects the slots of the
    board tiles, all the labels that display information about the current players
    and the results of the games.

    :ivar button_clicked: button_clicked (Signal): Signal emitted when a signal (QPushButton)
    is clicked so it can be utilized in the Play class in src/game.py
    """

    button_clicked = Signal(QPushButton)

    def __init__(self, window) -> None:
        """
        Initializies the BoardUi object

        This constructor sets up internal reference to the app window, sets up the board_tile
        connections, and saves the base label font so it can be changed and reapplied

        :param window: The main window of the application containing all the Ui elements
        :type window: QMainWindow
        """
        super().__init__()
        self.window = window
        self.setup_board_connections()
        self.label_font = self.window.game_labels[0].font()

    def setup_board_connections(self):
        """
        Loops through the list of board tiles and connects each of them to a slot
        """
        for button in self.window.board_tiles:
            button.clicked.connect(lambda _=False, b=button: self.click_button(b))

    def disable_all_tiles(self):
        """
        Disables all tiles when a player wins so the other player can't keep clicking
        the tiles during the small self.delay_action that happens while displaying the
        winning tiles
        """
        for button in self.window.board_tiles:
            button.setEnabled(False)

    def click_button(self, button):
        """
        When a button in window.board_tiles is clicked it emits a signal containing that
        button to src/game.py which in turn returns that same button object and the current
        players symbol back to self.make_move() so the symbol can be displayed on the button

        :param button: Whenever a QPushButton is clicked that button instance emits a signal with 
                       itself as an argument so that it can be used in other parts of the code
        :type button: QPushButton
        """
        button.setEnabled(False)
        self.button_clicked.emit(button)

    def make_move(self, button, symbol):
        """
        Places the symbol on the button whenever a button on the board is clicked, the functions
        happen in this order: self.click_button > src/game.make_move > self.make_move

        :param button: The QPushButton in the window.board_tiles that was pressed
        :type QPushButton:

        :param symbol: The string representation of the current player objects symbol
        :type string:
        """
        button.setEnabled(False)
        button.setText(symbol)

    def set_game_labels(self, players):
        """
        Enumrates through the players list and populates the labels above the game board
        with relevant player info, like the player type and the symbol of the player

        :param players: A List containing the two player objects
        :type players: list
        """
        for i, player in enumerate(players):
            self.window.game_labels[i].setText(f"{str(player)}")

    def finish_current_game(self):
        """
        When the game finishes goes back to the starting tab and resets every tile on
        the board to be enabled again and clears the text to prepare for the next game
        """
        self.window.tab_menu.setCurrentIndex(0)
        for button in self.window.board_tiles:
            button.setEnabled(True)
            button.setText("")

    def reset_game_label(self):
        """
        Resets the font of the both of the window.game_labels back to their original form
        happens after each turn and after the game is completed
        """
        font = self.label_font
        font.setBold(False)

        for label in self.window.game_labels:
            label.setFont(font)

    def display_current_player_game_label(self, current_player):
        """
        Sets the current player label above the game board to be bold so the user can
        know whose turn it currently is. When the player is against a CPU, the label
        appears as if it's not changing because the CPU acts instantly, but it's mostly
        to be used when two human players are playing.

        :param current_player: An integer that can be used to index into window.game_labels
        :type players: int
        """
        font = self.label_font
        font.setBold(True)

        current_label = self.window.game_labels[current_player]
        current_label.setFont(font)

    def update_score(self, winning_player):
        """
        When a game is completed the score for the player that won is updated by adding
        1 to whatever the current score is for that player, the correct label is found by
        indexing into self.window.player_score_labels with the winning player parameter

        :param winning_player: the index of the winning player
        :type winning_player: int
        """
        new_score = 1 + int(self.window.player_score_labels[winning_player].text())
        self.window.player_score_labels[winning_player].setText(str(new_score))

    def update_results_label(self, game_results):
        """
        Sets the text of window.game_results_label to describe which player won or
        or if it was a tie game.

        :param game_results: A string that gets applied onto the label to describe the winner
        :type game_results: string
        """
        self.window.game_results_label.setText(game_results)

    def display_winning_tiles(self, winning_tiles):
        """
        Whenever a win condition is met in the TicTacToe game the tiles that met
        that win condition will become visually distinct by having their colors changed

        Iterates through the winning_tiles list and applies a property to each of them
        unpolish clears the old style. Polish is used to apply the new style from the new
        property, and update ensures that the new style is redrawn on the screen

        :param winning_tiles: A list containing the 3 board tile indicies that met
                              any of the win conditions
        :type winning_tiles: list of ints
        """
        for tile in winning_tiles:
            tile_widget = self.window.board_tiles[tile - 1]
            tile_widget.setProperty("type", "winningTile")
            tile_widget.style().unpolish(tile_widget)
            tile_widget.style().polish(tile_widget)
            tile_widget.update()

    def reset_winning_tiles(self, winning_tiles):
        """
        Resets the tiles with the new winningTile property back to their default style

        While the board is getting reset, uses the same winning tiles that just had
        the winningTile property to them and applies None to the same property removing
        the new style that was just set. Polish is used to apply the new style from the new
        property, and update ensures that the new style is redrawn on the screen

        :param winning_tiles: A list containing the 3 board tile indicies that met
                              any of the win conditions
        :type winning_tiles: list of ints
        """
        for tile in winning_tiles:
            tile_widget = self.window.board_tiles[tile - 1]
            tile_widget.setProperty("type", None)
            tile_widget.style().unpolish(tile_widget)
            tile_widget.style().polish(tile_widget)
            tile_widget.update()

    def delay_action(self, delay, function, *args, **kwargs):
        """
        Executes a given function after a specified delay.

        This method uses a QTimer to delay the execution of the specified function. It can
        pass arbitrary positional and keyword arguments to the function when it is called.

        :param delay: The delay time in milliseconds after which the function should be executed.
        :type delay: int
        :param function: The function to be executed after the delay.
        :type function: callable
        :param args: Variable length argument list passed to the function.
        :type args: tuple
        :param kwargs: Arbitrary keyword arguments passed to the function.
        :type kwargs: dict
        """
        QTimer.singleShot(delay, lambda: function(*args, **kwargs))
