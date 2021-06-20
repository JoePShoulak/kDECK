import os

ASSETS_PATH = os.path.join(os.path.dirname(__file__), "Assets")


def show(conn, text):
    conn.ui.message("kDECK: " + text, 5)


def path_to(icon):
    return os.path.join(ASSETS_PATH, icon)


def find_vb(page, value_button):
    return next(b for b in page.buttons if b.name == value_button)


def get_page_names(layout):
    page_names = []

    for button in layout:
        if button["page"] not in page_names:
            page_names.append(button["page"])

    return page_names


def make_params(page, value_button, lst=None, row=3, offset=0):
    if lst is None:
        lst = [1, 10, 100]
    param_buttons = []
    options = []
    for i in lst[::-1]:
        options.append(-i)
    options.append(False)
    options.extend(lst)
    for index, delta in enumerate(options):
        if delta:
            param_buttons.append(
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

    return param_buttons


def parse(params):
    for k, v in params.items():
        if type(v) is bool:
            params[k] = v
        elif type(v.value) is bool:
            params[k] = v.value
        else:
            params[k] = int(v.value)

    return params


def set_params(obj, params, node=None):
    parse(params)
    for k, v in params.items():
        if k == "autowarp":
            node.autowarp = v
        else:
            setattr(obj, k, v)

