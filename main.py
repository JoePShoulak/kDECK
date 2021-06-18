#!/usr/bin/env python3

import os
import threading

from StreamDeck.DeviceManager import DeviceManager

from helper import get_page_names
from layout import layout

from objects.Button import NavButton, ActionButton, ValueButton, ParamButton
from objects.Page import Page

ASSETS_PATH = os.path.join(os.path.dirname(__file__), "Assets")


if __name__ == "__main__":
    streamdecks = DeviceManager().enumerate()

    for index, deck in enumerate(streamdecks):
        deck.open()
        deck.reset()

        # Set initial screen brightness to 30%.
        # deck.set_brightness(30)
        deck.set_brightness(100)

        page_dict = {i: Page(deck, i) for i in get_page_names(layout)}
        for p in page_dict.values():
            for button in list(filter(lambda x: x["page"] == p.name, layout)):
                if button["type"] == "nav":
                    p.add_button(NavButton(
                        deck,
                        button["location"],
                        button["name"],
                        os.path.join(ASSETS_PATH, button["icon"]),
                        page_dict[button["dest"]])
                    )
                elif button["type"] == "action":
                    # TODO: Allow multiple value buttons, probably as a dict
                    value_button = None
                    try:
                        value_button = next(b for b in p.buttons if b.name == button["value_button"])
                    except StopIteration:
                        pass
                    p.add_button(ActionButton(
                        deck,
                        button["location"],
                        button["name"],
                        os.path.join(ASSETS_PATH, button["icon"]),
                        button["callback"],
                        value_button,
                        button["params"])
                    )
                elif button["type"] == "value":
                    p.add_button(ValueButton(
                        deck,
                        button["location"],
                        button["name"],
                        os.path.join(ASSETS_PATH, button["icon"]),
                        button["value"],
                        button["label"])
                    )
                elif button["type"] == "param":
                    p.add_button(ParamButton(
                        deck,
                        button["location"],
                        button["name"],
                        os.path.join(ASSETS_PATH, button["icon"]),
                        next(b for b in p.buttons if b.name == button["value_button"]),
                        button["delta"])
                    )

        home = page_dict["Home"]
        home.render_buttons()
        # Wait until all application threads have terminated (for this example,
        # this is when all deck handles are closed).
        for t in threading.enumerate():
            if t is threading.currentThread():
                continue

            if t.is_alive():
                t.join()
