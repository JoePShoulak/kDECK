from Actions.MechJeb import warp, smart_ass, launch
from helper import make_params


def empty():
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
        "name": "SmartAss",
        "type": "nav",
        "icon": "smartass\\SmartAss.png",
        "location": 1,
        "page": "Home",
        "dest": "SmartAss"
    },
    {
        "name": "Launch",
        "type": "nav",
        "icon": "Launch.png",
        "location": 8,
        "page": "Home",
        "dest": "Launch"
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
        "value_buttons": ["LeadTime"],
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
        "value_buttons": ["LeadTime"],
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
        "value_buttons": ["LeadTime"],
        "params": {
            "destination": "soi",
        }
    },
    {
        "name": "WarpNode",
        "type": "action",
        "icon": "warp\\WarpNode.png",
        "location": 3,
        "page": "Warp",
        "callback": warp,
        "value_buttons": ["LeadTime"],
        "params": {
            "destination": "node",
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

    # Smart A.S.S #
    # Orbital
    {
        "name": "Prograde",
        "type": "action",
        "icon": "smartass\\Prograde.png",
        "location": 0,
        "page": "SmartAss",
        "callback": smart_ass,
        "value_buttons": [],
        "params": {
            "direction": "prograde",
        }
    },
    {
        "name": "Retrograde",
        "type": "action",
        "icon": "smartass\\Retrograde.png",
        "location": 1,
        "page": "SmartAss",
        "callback": smart_ass,
        "value_buttons": [],
        "params": {
            "direction": "retrograde",
        }
    },
    {
        "name": "Normal",
        "type": "action",
        "icon": "smartass\\Normal.png",
        "location": 8,
        "page": "SmartAss",
        "callback": smart_ass,
        "value_buttons": [],
        "params": {
            "direction": "normal",
        }
    },
    {
        "name": "AntiNormal",
        "type": "action",
        "icon": "smartass\\AntiNormal.png",
        "location": 9,
        "page": "SmartAss",
        "callback": smart_ass,
        "value_buttons": [],
        "params": {
            "direction": "antinormal",
        }
    },
    {
        "name": "RadialOut",
        "type": "action",
        "icon": "smartass\\RadialOut.png",
        "location": 16,
        "page": "SmartAss",
        "callback": smart_ass,
        "value_buttons": [],
        "params": {
            "direction": "radialout",
        }
    },
    {
        "name": "RadialIn",
        "type": "action",
        "icon": "smartass\\RadialIn.png",
        "location": 17,
        "page": "SmartAss",
        "callback": smart_ass,
        "value_buttons": [],
        "params": {
            "direction": "radialin",
        }
    },
    # Surface
    {
        "name": "SVEL+",
        "type": "action",
        "icon": "smartass\\SVEL_P.png",
        "location": 2,
        "page": "SmartAss",
        "callback": smart_ass,
        "value_buttons": [],
        "params": {
            "direction": "svel+",
        }
    },
    {
        "name": "SVEL-",
        "type": "action",
        "icon": "smartass\\SVEL_M.png",
        "location": 3,
        "page": "SmartAss",
        "callback": smart_ass,
        "value_buttons": [],
        "params": {
            "direction": "svel-",
        }
    },
    {
        "name": "HVEL+",
        "type": "action",
        "icon": "smartass\\HVEL_P.png",
        "location": 10,
        "page": "SmartAss",
        "callback": smart_ass,
        "value_buttons": [],
        "params": {
            "direction": "hvel+",
        }
    },
    {
        "name": "HVEL-",
        "type": "action",
        "icon": "smartass\\HVEL_M.png",
        "location": 11,
        "page": "SmartAss",
        "callback": smart_ass,
        "value_buttons": [],
        "params": {
            "direction": "hvel-",
        }
    },
    {
        "name": "Surf",
        "type": "action",
        "icon": "smartass\\Surf.png",
        "location": 18,
        "page": "SmartAss",
        "callback": smart_ass,
        "value_buttons": [],
        "params": {
            "direction": "surf",
        }
    },
    {
        "name": "Up",
        "type": "action",
        "icon": "smartass\\Up.png",
        "location": 19,
        "page": "SmartAss",
        "callback": smart_ass,
        "value_buttons": [],
        "params": {
            "direction": "up",
        }
    },
    {
        "name": "Exit",
        "type": "nav",
        "icon": "Exit.png",
        "location": 31,
        "page": "SmartAss",
        "dest": "Home"
    },

    # Launch #
    {
        "name": "OrbitAlt",
        "type": "value",
        "icon": "bg.png",
        "location": 26,
        "page": "Launch",
        "label": "Orbit Alt. (km):",
        "value": "100"
    },
    {
        "name": "TurnAlt",
        "type": "value",
        "icon": "bg.png",
        "location": 18,
        "page": "Launch",
        "label": "Turn Alt. (km):",
        "value": "100"
    },
    {
        "name": "TurnVel",
        "type": "value",
        "icon": "bg.png",
        "location": 10,
        "page": "Launch",
        "label": "Turn Vel. (m/s):",
        "value": "100"
    },
    {
        "name": "ClimbRoll",
        "type": "value",
        "icon": "bg.png",
        "location": 14,
        "page": "Launch",
        "label": "Climb Roll (°):",
        "value": "90"
    },
    {
        "name": "TurnRoll",
        "type": "value",
        "icon": "bg.png",
        "location": 22,
        "page": "Launch",
        "label": "Turn Roll (°):",
        "value": "90"
    },
    {
        "name": "DeploySolar",
        "type": "value",
        "icon": "bg.png",
        "location": 29,
        "page": "Launch",
        "label": "Deploy Solar:",
        "value": False,
        "toggle": True
    },
    {
        "name": "DeployComms",
        "type": "value",
        "icon": "bg.png",
        "location": 30,
        "page": "Launch",
        "label": "Deploy Comms:",
        "value": False,
        "toggle": True
    },
    {
        "name": "AutostageLimit",
        "type": "value",
        "icon": "bg.png",
        "location": 2,
        "page": "Launch",
        "label": "Autostage to:",
        "value": 1,
    },
    {
        "name": "AutostageToggle",
        "type": "value",
        "icon": "bg.png",
        "location": 4,
        "page": "Launch",
        "label": "Autostage:",
        "value": True,
        "toggle": True
    },
    {
        "name": "CircularizeToggle",
        "type": "value",
        "icon": "bg.png",
        "location": 5,
        "page": "Launch",
        "label": "Circularize:",
        "value": True,
        "toggle": True
    },
    {
        "name": "WarpToggle",
        "type": "value",
        "icon": "bg.png",
        "location": 6,
        "page": "Launch",
        "label": "AutoWarp:",
        "value": True,
        "toggle": True
    },
    {
        "name": "CorrectiveSteeringToggle",
        "type": "value",
        "icon": "bg.png",
        "location": 7,
        "page": "Launch",
        "label": "Autocorrect:",
        "value": True,
        "toggle": True
    },

    {
        "name": "LaunchExecute",
        "type": "action",
        "icon": "Launch.png",
        "location": 0,
        "page": "Launch",
        "callback": launch,
        "value_buttons": [
            "OrbitAlt",
            "TurnAlt",
            "TurnVel",
            "ClimbRoll",
            "TurnRoll",
            "DeploySolar",
            "DeployComms",
            "AutostageLimit",
            "AutostageToggle",
            "CircularizeToggle",
            "WarpToggle",
            "CorrectiveSteeringToggle"
        ],
        "params": {
        }
    },

    *make_params("Launch", "OrbitAlt", [10, 100]),
    *make_params("Launch", "TurnAlt", [10, 100], 2),
    *make_params("Launch", "TurnVel", [10, 100], 1),
    *make_params("Launch", "ClimbRoll", [5], 1, 5),
    *make_params("Launch", "TurnRoll", [5], 2, 5),
    *make_params("Launch", "AutostageLimit", [1], 0, 1),

    {
        "name": "Exit",
        "type": "nav",
        "icon": "Exit.png",
        "location": 31,
        "page": "Launch",
        "dest": "Home"
    },
]

