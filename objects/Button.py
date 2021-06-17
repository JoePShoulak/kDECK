from PIL import Image
from StreamDeck.ImageHelpers import PILHelper


class Button:
    def __init__(self, deck, location, name, icon, page=False):
        self.deck = deck
        self.name = name
        self.location = location
        self.icon = icon
        self.page = page

    def display_button(self):
        icon = Image.open(self.icon)
        image = PILHelper.create_scaled_image(self.deck, icon)
        self.deck.set_key_image(self.location, PILHelper.to_native_format(self.deck, image))

    def execute(self):
        self.page.render_buttons()


class ActionButton(Button):
    def __init__(self, deck, location, name, icon, callback):
        super().__init__(deck, location, name, icon)
        self.callback = callback

    def execute(self):
        self.callback()


'''
class ValueButton(Button):
    def __init__(self, deck, location, name, icon, value):
        super().__init__(deck, location, name, icon)
        self.value = value

    def execute(self):
        pass
    
    def display_button(self):
        icon = Image.open(self.icon)
        image = PILHelper.create_scaled_image(self.deck, icon)
        self.deck.set_key_image(self.location, PILHelper.to_native_format(self.deck, image))
'''
