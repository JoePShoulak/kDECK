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
        # Resize the source image asset to best-fit the dimensions of a single key,
        # leaving a margin at the bottom so that we can draw the key title
        # afterwards.
        icon = Image.open(self.icon)
        image = PILHelper.create_scaled_image(self.deck, icon)
        self.deck.set_key_image(self.location, PILHelper.to_native_format(self.deck, image))

    def execute(self):
        print(f'deck: {self.deck} location: {self.location}')
        if self.page:
            print(f'Loading page {self.page.name} ')
            self.page.render_buttons()
