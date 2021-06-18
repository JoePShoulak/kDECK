import os

ASSETS_PATH = os.path.join(os.path.dirname(__file__), "Assets")


def show(conn, text):
    conn.ui.message("kDECK: " + text, 5)


def path_to(icon):
    return os.path.join(ASSETS_PATH, icon)


def get_page_names(layout):
    page_names = []

    for button in layout:
        if button["page"] not in page_names:
            page_names.append(button["page"])

    return page_names


def make_params(page, value_button, lst=None, row=3, offset=0):
    if lst is None:
        lst = [1, 10, 100]
    params = []
    options = []
    for i in lst[::-1]:
        options.append(-i)
    options.append(False)
    options.extend(lst)
    for index, delta in enumerate(options):
        if delta:
            params.append(
                {
                    "name": str(delta),
                    "type": "param",
                    "icon": "bg.png",
                    "location": (8*row) + index + offset,
                    "page": page,
                    "value_button": value_button,
                    "delta": delta
                },
            )

    return params
