#!/usr/bin/env python3

import threading

from StreamDeck.DeviceManager import DeviceManager

from helper import get_page_names, path_to, find_vb
from layout import layout

from objects.Button import NavButton, ActionButton, ValueButton, ParamButton
from objects.Page import Page

if __name__ == "__main__":
    streamdecks = DeviceManager().enumerate()

    for index, deck in enumerate(streamdecks):
        deck.open()
        deck.reset()

        deck.set_brightness(100)

        page_dict = {i: Page(deck, i) for i in get_page_names(layout)}
        for p in page_dict.values():
            for button in list(filter(lambda b: b["page"] == p.name, layout)):
                defaults = [deck,
                            button["location"],
                            button["name"],
                            path_to(button["icon"])
                            ]
                if button["type"] == "nav":
                    p.add_button(NavButton(
                        *defaults,
                        page_dict[button["dest"]])
                    )
                elif button["type"] == "action":
                    value_buttons = []
                    for vb in button["value_buttons"]:
                        value_buttons.append(find_vb(p, vb))
                    p.add_button(ActionButton(
                        *defaults,
                        button["callback"],
                        value_buttons,
                        button["params"])
                    )
                elif button["type"] == "value":
                    # TODO: Factor this out
                    toggle = False
                    units = ""
                    if "toggle" in button.keys():
                        toggle = True
                    if "units" in button.keys():
                        units = button["units"]

                    p.add_button(ValueButton(
                        *defaults,
                        button["value"],
                        button["label"],
                        toggle,
                        units)
                    )
                elif button["type"] == "param":
                    value_button = find_vb(p, button["value_button"])
                    p.add_button(ParamButton(
                        *defaults,
                        value_button,
                        button["delta"])
                    )

        page_dict["Home"].render_buttons()

        for t in threading.enumerate():
            if t is threading.currentThread():
                continue

            if t.is_alive():
                t.join()
