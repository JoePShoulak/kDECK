from PIL import Image
from StreamDeck.ImageHelpers import PILHelper

import os

ASSETS_PATH = os.path.join(os.path.dirname(__file__), "Assets")


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
        if self.page:
            self.page.render_buttons()
