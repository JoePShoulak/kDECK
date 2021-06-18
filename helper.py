def get_page_names(layout):
    page_names = []

    for button in layout:
        if button["page"] not in page_names:
            page_names.append(button["page"])

    return page_names


def make_params(page, value_button):
    params = []
    for index, delta in enumerate([-100, -10, -1, False, 1, 10, 100]):
        if delta:
            params.append(
                {
                    "name": str(delta),
                    "type": "param",
                    "icon": "bg.png",
                    "location": 24 + index,
                    "page": page,
                    "value_button": value_button,
                    "delta": delta
                },
            )

    return params
