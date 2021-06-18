#!/usr/bin/env python3

import threading

from StreamDeck.DeviceManager import DeviceManager

from helper import get_page_names, path_to
from layout import layout

from objects.Button import NavButton, ActionButton, ValueButton, ParamButton
from objects.Page import Page


if __name__ == "__main__":
    streamdecks = DeviceManager().enumerate()

    for index, deck in enumerate(streamdecks):
        deck.open()
        deck.reset()

        # Set initial screen brightness to 30%.
        deck.set_brightness(100)

        page_dict = {i: Page(deck, i) for i in get_page_names(layout)}
        for p in page_dict.values():
            for button in list(filter(lambda b: b["page"] == p.name, layout)):
                if button["type"] == "nav":
                    p.add_button(NavButton(
                        deck,
                        button["location"],
                        button["name"],
                        path_to(button["icon"]),
                        page_dict[button["dest"]])
                    )
                elif button["type"] == "action":
                    value_buttons = []
                    for vb in button["value_buttons"]:
                        try:
                            value_buttons.append(next(b for b in p.buttons if b.name == vb))
                        except StopIteration:
                            pass
                    p.add_button(ActionButton(
                        deck,
                        button["location"],
                        button["name"],
                        path_to(button["icon"]),
                        button["callback"],
                        value_buttons,
                        button["params"])
                    )
                elif button["type"] == "value":
                    toggle = False
                    if "toggle" in button.keys():
                        toggle = True
                    p.add_button(ValueButton(
                        deck,
                        button["location"],
                        button["name"],
                        path_to(button["icon"]),
                        button["value"],
                        button["label"],
                        toggle)
                    )
                elif button["type"] == "param":
                    value_button = next(b for b in p.buttons if b.name == button["value_button"])
                    p.add_button(ParamButton(
                        deck,
                        button["location"],
                        button["name"],
                        path_to(button["icon"]),
                        value_button,
                        button["delta"])
                    )

        page_dict["Home"].render_buttons()
        # Wait until all application threads have terminated (for this example,
        # this is when all deck handles are closed).
        for t in threading.enumerate():
            if t is threading.currentThread():
                continue

            if t.is_alive():
                t.join()
