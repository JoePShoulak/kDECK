class Page:

    def __init__(self, deck, name):
        self.buttons = []
        self.name = name
        self.deck = deck

    def add_button(self, button):
        self.buttons.append(button)

    def render_buttons(self):
        self.deck.reset()
        self.deck.set_key_callback(self.execute_button)
        for b in self.buttons:
            b.display_button()

    def execute_button(self, deck, key, state):
        for b in self.buttons:
            if b.location == key and state:
                b.execute()
