from objects import Button


class Page:

    def __init__(self, buttons, deck, name):
        self.buttons = buttons
        self.name = name
        self.deck = deck
        deck.set_key_callback(self.execute_button)

    def render_buttons(self):
        self.deck.reset()
        for b in self.buttons:
            b.display_button()

    def execute_button(self, deck, key, state):
        for b in self.buttons:
            if b.location == key and state:
                b.execute()