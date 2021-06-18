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
        "name": "LeadTime",
        "type": "value",
        "icon": "bg.png",
        "location": 27,
        "page": "Warp",
        "label": "Lead time (s):",
        "value": "0"
    },

    {
        "name": "WarpPE",
        "type": "action",
        "icon": "mechjeb\\warp\\WarpPE.png",
        "location": 0,
        "page": "Warp",
        "callback": warp,
        "value_button": "LeadTime",
        "params": {
            "destination": "pe",
        }
    },
    {
        "name": "WarpAP",
        "type": "action",
        "icon": "mechjeb\\warp\\WarpAP.png",
        "location": 1,
        "page": "Warp",
        "callback": warp,
        "value_button": "LeadTime",
        "params": {
            "destination": "ap",
        }
    },
    {
        "name": "WarpSOI",
        "type": "action",
        "icon": "mechjeb\\warp\\WarpSOI.png",
        "location": 2,
        "page": "Warp",
        "callback": warp,
        "value_button": "LeadTime",
        "params": {
            "destination": "soi",
        }
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

param_buttons = [
    {
        "name": "-100",
        "type": "param",
        "icon": "bg.png",
        "location": 24,
        "page": "Warp",
        "value_button": "LeadTime",
        "delta": -100
    },
    {
        "name": "-10",
        "type": "param",
        "icon": "bg.png",
        "location": 25,
        "page": "Warp",
        "value_button": "LeadTime",
        "delta": -10
    },
    {
        "name": "-1",
        "type": "param",
        "icon": "bg.png",
        "location": 26,
        "page": "Warp",
        "value_button": "LeadTime",
        "delta": -1
    },
    {
        "name": "+1",
        "type": "param",
        "icon": "bg.png",
        "location": 28,
        "page": "Warp",
        "value_button": "LeadTime",
        "delta": 1
    },
    {
        "name": "+10",
        "type": "param",
        "icon": "bg.png",
        "location": 29,
        "page": "Warp",
        "value_button": "LeadTime",
        "delta": 10
    },
    {
        "name": "+100",
        "type": "param",
        "icon": "bg.png",
        "location": 30,
        "page": "Warp",
        "value_button": "LeadTime",
        "delta": 100
    },
]

layout.extend(param_buttons)

