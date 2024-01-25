from src.game import TicTacToe, Play
from ui.app_ui import init_app
from slots.game_board import BoardUi


def main():
    """
    The main entry point for the TicTacToe application.

    This function initializes the application, sets up the UI, applies stylesheets,
    and configures the game logic. It handles exceptions related to stylesheet loading,
    sets the window title, initializes the game board, and starts the event loop of the application.

    It creates instances of the BoardUi, TicTacToe, and Play classes, and shows the main window
    to start the application.
    """
    app, window = init_app()

    try:
        with open("ui/style.qss", "r", encoding="utf-8") as file:
            stylesheet = file.read()
            app.setStyleSheet(stylesheet)
    except Exception as e:
        print(f"Stylesheet error: {e}")

    window.setWindowTitle("TicTacToe")
    board_ui = BoardUi(window)
    game = TicTacToe(board_ui)
    play = Play(game)

    window.show()

    app.exec()


if __name__ == "__main__":
    main()
