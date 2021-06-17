from Actions.MechJeb import warp

layout = [
    # HOME #
    {
        "name": "MechJeb",
        "type": "nav",
        "icon": "mechjeb\\MechJeb.png",
        "location": 0,
        "page": "Home",
        "dest": "MechJeb"
    },

    # MECHJEB #
    {
        "name": "Warp",
        "type": "nav",
        "icon": "mechjeb\\warp\\Warp.png",
        "location": 0,
        "page": "MechJeb",
        "dest": "Warp"
    },

    {
        "name": "Exit",
        "type": "nav",
        "icon": "Exit.png",
        "location": 31,
        "page": "MechJeb",
        "dest": "Home"
    },

    # WARP #
    {
        "name": "WarpPE",
        "type": "action",
        "icon": "mechjeb\\warp\\WarpPE.png",
        "location": 0,
        "page": "Warp",
        "callback": warp,
        "params": "pe"
    },
    {
        "name": "WarpAP",
        "type": "action",
        "icon": "mechjeb\\warp\\WarpAP.png",
        "location": 1,
        "page": "Warp",
        "callback": warp,
        "params": "ap"
    },
    {
        "name": "WarpSOI",
        "type": "action",
        "icon": "mechjeb\\warp\\WarpSOI.png",
        "location": 2,
        "page": "Warp",
        "callback": warp,
        "params": "soi"
    },

    {
        "name": "LeadTime",
        "type": "value",
        "icon": "bg.png",
        "location": 8,
        "page": "Warp",
        "label": "Lead time (s):",
        "value": "0"
    },

    {
        "name": "Exit",
        "type": "nav",
        "icon": "Exit.png",
        "location": 31,
        "page": "Warp",
        "dest": "MechJeb"
    },
]

'''
param_buttons = [
    {
        "name": "+1",
        "type": "param",
        "icon": "bg.png",
        "location": 9,
        "page": "Warp",
        "value_button": next(x for x in layout if x["name"] == "LeadTime"),
        "delta": 1
    },
]

layout.extend(param_buttons)
'''


