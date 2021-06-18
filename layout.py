from Actions.MechJeb import warp
from Actions.Utilities import science
from helper import make_params

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

    *make_params("Warp", "LeadTime"),

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
        "value_button": [],
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

