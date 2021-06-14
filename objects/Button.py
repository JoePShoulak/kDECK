import os

from PIL import Image, ImageDraw, ImageFont
from StreamDeck.ImageHelpers import PILHelper


class Button:
    def __init__(self, deck, location, name, icon):
        self.deck = deck
        self.name = name
        self.location = location
        self.icon = icon

    def display_button(self):
        # Resize the source image asset to best-fit the dimensions of a single key,
        # leaving a margin at the bottom so that we can draw the key title
        # afterwards.
        icon = Image.open(self.icon)
        image = PILHelper.create_scaled_image(self.deck, icon, margins=[0, 0, 0, 0])
        self.deck.set_key_image(self.location, PILHelper.to_native_format(self.deck, image))

    def execute(self):
        print(f'deck: {self.deck} location: {self.location} ')


class PageButton(Button):

    def __init__(self, page, deck, location, name, icon):
        super().__init__(deck, location, name, icon)
        page.render_buttons()
