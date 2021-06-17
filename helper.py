def get_page_names(layout):
    page_names = []

    for button in layout:
        if button["page"] not in page_names:
            page_names.append(button["page"])

    return page_names
