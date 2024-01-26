import random


class HumanPlayer:
    """
    A Human player and the Parent Class of all player classes

    Allows a symbol to be set for the player and also allows that symbol to be
    returned for wherever its needed 
    """
    def __init__(self):
        """
        Initializes the HumanPlayer object

        At first the symbol is an empty string before the player order is known, whichever
        player gets to make a move first is the one that gets the 'X' symbol
        """
        self.symbol = ""

    def __str__(self):
        """
        Initializes a ComputerPlayer instance.
        """
        return f"Human Player: {self.symbol}"

    def set_symbol(self, symbol):
        """
        Sets the symbol into a variable that can then be retrieved by another function

        :param symbol: The first player gets to have the 'X' symbol
        :type symbol: string
        """
        self.symbol = symbol

    def get_symbol(self):
        """
        Returns whatever symbol is set for this player instance

        :return: Returns the symbol that was set
        :rtype: string
        """
        return self.symbol

    def make_move(self, button):
        return int(str(button.objectName()).split("_")[1])


class ComputerPlayer(HumanPlayer):
    """
    Represents a computer controlled player in the game

    The computer class is a subclass of the HumanPlayer class but is slightly different
    since the computer doesn't actually click on the Ui, it has to simulate that click
    
    """
    def __init__(self):
        """
        Initializes a ComputerPlayer instance.

        This constructor calls the initialization of the HumanPlayer superclass.
        """
        super().__init__()

    def __str__(self):
        """
        Returns a slightly different string representation indicating that its a CPU

        :return: A string representation of the Computer Player and whatever symbol it has
        :rtype: string
        """
        return f"CPU: {self.symbol}"

    def make_move(self, available_moves):
        """
        Picks a random move from the remaining available_moves since this CPU doesn't have
        any intelligence or strategy

        :return: a random choice selected from a list of available moves
        :rtype: int
        """
        return random.choice(available_moves)
