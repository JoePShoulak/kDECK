from abc import abstractmethod, ABC

from PIL import Image
from StreamDeck.ImageHelpers import PILHelper


class Button(ABC):
    def __init__(self, deck, location, name, icon):
        self.deck = deck
        self.name = name
        self.location = location
        self.icon = icon

    def display_button(self):
        icon = Image.open(self.icon)
        image = PILHelper.create_scaled_image(self.deck, icon)
        self.deck.set_key_image(self.location, PILHelper.to_native_format(self.deck, image))

    @abstractmethod
    def execute(self):
        pass


class NavButton(Button):
    def __init__(self, deck, location, name, icon, page):
        self.page = page
        super().__init__(deck, location, name, icon)

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
