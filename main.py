#!/usr/bin/env python3

import os
import threading

from StreamDeck.DeviceManager import DeviceManager

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

        # TODO: Deck is needed here, but if these definitions were in a module, that would be ideal
        button3 = ActionButton(deck, 0, "WarpPE", os.path.join(ASSETS_PATH, "WarpPE.png"), warp_pe)
        button4 = NavButton(deck, 31, "Exit", os.path.join(ASSETS_PATH, "Exit.png"))
        page2 = Page([button3, button4], deck, "Page 2")

        button1 = NavButton(deck, 0, "MechJeb", os.path.join(ASSETS_PATH, "MechJeb.png"), page2)
        button2 = NavButton(deck, 1, "ActionGroups", os.path.join(ASSETS_PATH, "ActionGroups.png"))
        home = Page([button1, button2], deck, "Home")

        # TODO: This is janky as fuck
        home.buttons[0].page = page2
        page2.buttons[1].page = home

        home.render_buttons()

        # Wait until all application threads have terminated (for this example,
        # this is when all deck handles are closed).
        for t in threading.enumerate():
            if t is threading.currentThread():
                continue

            if t.is_alive():
                t.join()
