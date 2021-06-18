from Actions.MechJeb import warp
from Actions.Utilities import science


def null_callback(params=None):
    pass

layout = [

    # HOME #
    {
        "name": "Warp",
        "type": "nav",
        "icon": "warp\\Warp.png",
        "location": 0,
        "page": "Home",
        "dest": "Warp"
    },
    {
        "name": "Utilities",
        "type": "nav",
        "icon": "utilities\\Utilities.png",
        "location": 1,
        "page": "Home",
        "dest": "Utilities"
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
        "icon": "warp\\WarpPE.png",
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
        "icon": "warp\\WarpAP.png",
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
        "icon": "warp\\WarpSOI.png",
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
        "dest": "Home"
    },
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



    # Utilities #
    {
        "name": "NULL_VALUE",
        "type": "value",
        "icon": "bg.png",
        "location": 31,
        "page": "Utilities",
        "label": "",
        "value": "0"
    },

    {
        "name": "RunScience",
        "type": "action",
        "icon": "utilities\\RunScience.png",
        "location": 0,
        "page": "Utilities",
        "callback": science,
        "value_button": "NULL_VALUE",
        "params": {
            "event": "run"
        }
    },

    {
        "name": "Exit",
        "type": "nav",
        "icon": "Exit.png",
        "location": 31,
        "page": "Utilities",
        "dest": "Home"
    },

]

