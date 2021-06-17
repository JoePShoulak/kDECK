#!/usr/bin/env python3

import os
import threading

from StreamDeck.DeviceManager import DeviceManager
from layout import layout

# Folder location of image assets used by this example.
from objects.Button import Button
from objects.Page import Page

ASSETS_PATH = os.path.join(os.path.dirname(__file__), "Assets")


if __name__ == "__main__":
    streamdecks = DeviceManager().enumerate()

    print("Found {} Stream Deck(s).\n".format(len(streamdecks)))

    for index, deck in enumerate(streamdecks):
        deck.open()
        deck.reset()

        # Set initial screen brightness to 30%.
        deck.set_brightness(30)

        pages = [Page(deck, "Home"), Page(deck, "MechJeb")]
        page_dict = {"Home": pages[0], "MechJeb": pages[1]}
        for p in pages:
            for button in list(filter(lambda x: x["page"] == p.name, layout)):
                if button["type"] == "nav":
                    p.add_button(NavButton(
                        deck,
                        button["location"],
                        button["name"],
                        os.path.join(ASSETS_PATH, button["icon"]),
                        page_dict[button["dest"]]))
                elif button["type"] == "action":
                    p.add_button(ActionButton(
                        deck,
                        button["location"],
                        button["name"],
                        os.path.join(ASSETS_PATH, button["icon"]),
                        button["callback"]))

        home = pages[0]
        home.render_buttons()
        # Wait until all application threads have terminated (for this example,
        # this is when all deck handles are closed).
        for t in threading.enumerate():
            if t is threading.currentThread():
                continue

            if t.is_alive():
                t.join()
