import os
from abc import abstractmethod, ABC

from PIL import Image, ImageDraw, ImageFont
from StreamDeck.ImageHelpers import PILHelper

dirname = os.path.dirname
ASSETS_PATH = os.path.join(dirname(dirname(__file__)), "Assets")


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
    def __init__(self, deck, location, name, icon, callback, value_buttons, params):
        super().__init__(deck, location, name, icon)
        self.callback = callback
        self.value_buttons = value_buttons
        self.params = params

    def execute(self):
        for vb in self.value_buttons:
            self.params[vb.name] = vb

        self.callback(self.params)


class ValueButton(Button):
    def __init__(self, deck, location, name, icon, value, label, toggle=False):
        super().__init__(deck, location, name, icon)
        self.value = value
        self.label = label
        self.toggle = toggle

    def execute(self):
        if self.toggle:
            self.value = not self.value
            self.display_button()

    def display_button(self):
        icon = Image.open(self.icon)
        image = PILHelper.create_scaled_image(self.deck, icon)

        # TODO: Move units to bottom row, align all values and params to center
        # TODO: Add min/max options
        draw = ImageDraw.Draw(image)
        label_font = ImageFont.truetype(os.path.join(ASSETS_PATH, "Roboto-Regular.ttf"), 14)
        value_font = ImageFont.truetype(os.path.join(ASSETS_PATH, "Roboto-Regular.ttf"), 28)
        draw.text((image.width / 2, 20), text=self.label, font=label_font, anchor="ms", fill="white")
        draw.text((image.width / 2, image.height / 2 + 20), text=str(self.value), font=value_font, anchor="ms", fill="white")
        self.deck.set_key_image(self.location, PILHelper.to_native_format(self.deck, image))


class ParamButton(Button):
    def __init__(self, deck, location, name, icon, value_button, delta):
        super().__init__(deck, location, name, icon)
        self.value_button = value_button
        self.delta = delta

    def execute(self):
        value = float(self.value_button.value) + self.delta
        value = max(round(value, 1), 0)
        if value == round(value):
            value = int(value)
        self.value_button.value = str(value)

        self.value_button.display_button()

    def display_button(self):
        icon = Image.open(self.icon)
        image = PILHelper.create_scaled_image(self.deck, icon)

        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(os.path.join(ASSETS_PATH, "Roboto-Regular.ttf"), 28)
        if self.delta > 0:
            label = "+" + str(self.delta)
        else:
            label = str(self.delta)
        draw.text((image.width / 2, image.height / 2 + 20), text=label, font=font, anchor="ms", fill="white")

        self.deck.set_key_image(self.location, PILHelper.to_native_format(self.deck, image))

