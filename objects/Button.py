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
    def __init__(self, deck, location, name, icon, callback, value_button, params):
        super().__init__(deck, location, name, icon)
        self.callback = callback
        self.value_button = value_button
        self.params = params

    def execute(self):
        # TODO: Part of the other TODO on accepting multiple value buttons
        if self.value_button:
            self.params["value"] = self.value_button.value

        self.callback(self.params)


class ValueButton(Button):
    def __init__(self, deck, location, name, icon, value, label):
        super().__init__(deck, location, name, icon)
        self.value = value
        self.label = label

    def execute(self):
        pass
    
    def display_button(self):
        icon = Image.open(self.icon)
        image = PILHelper.create_scaled_image(self.deck, icon)

        draw = ImageDraw.Draw(image)
        value_font = ImageFont.truetype(os.path.join(ASSETS_PATH, "Roboto-Regular.ttf"), 28)
        label_font = ImageFont.truetype(os.path.join(ASSETS_PATH, "Roboto-Regular.ttf"), 14)
        draw.text((image.width / 2, image.height / 2 + 20), text=self.value, font=value_font, anchor="ms", fill="white")
        draw.text((image.width / 2, 20), text=self.label, font=label_font, anchor="ms", fill="white")
        self.deck.set_key_image(self.location, PILHelper.to_native_format(self.deck, image))


class ParamButton(Button):
    def __init__(self, deck, location, name, icon, value_button, delta):
        super().__init__(deck, location, name, icon)
        self.value_button = value_button
        self.delta = delta

    def execute(self):
        value = int(self.value_button.value)
        value += self.delta
        self.value_button.value = str(max(value, 0))

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

