class BoardUi():
    def __init__(self, buttons) -> None:
        self.buttons = buttons
        self.setup_connections()

    def setup_connections(self):
        for button in self.buttons:
            button.clicked.connect(lambda _=False, b=button: self.place_tile(b))

    def place_tile(self, button):
        # print(f"Button {button.objectName()} clicked")
        button.setText(button.objectName())
        button.setText('X')
        button.setEnabled(False)
        return button.objectName()
    
    def update_score(label, score):
        pass
        





    