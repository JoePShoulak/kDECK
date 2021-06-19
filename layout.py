from Actions.MechJeb import warp, smart_ass, launch, rendezvous, dock, land, aircraft
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
    {
        "name": "Rendezvous",
        "type": "nav",
        "icon": "Rendezvous.png",
        "location": 9,
        "page": "Home",
        "dest": "Rendezvous"
    },
    {
        "name": "Dock",
        "type": "nav",
        "icon": "Dock.png",
        "location": 10,
        "page": "Home",
        "dest": "Dock"
    },
    {
        "name": "Land",
        "type": "nav",
        "icon": "Land.png",
        "location": 11,
        "page": "Home",
        "dest": "Land"
    },
    {
        "name": "Aircraft",
        "type": "nav",
        "icon": "Aircraft.png",
        "location": 12,
        "page": "Home",
        "dest": "Aircraft"
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
        "value": "10"
    },
    {
        "name": "TurnVel",
        "type": "value",
        "icon": "bg.png",
        "location": 10,
        "page": "Launch",
        "label": "Turn Vel. (m/s):",
        "value": "500"
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
        "name": "RollToggle",
        "type": "value",
        "icon": "bg.png",
        "location": 6,
        "page": "Launch",
        "label": "Force Roll:",
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
            "RollToggle",
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

    # Rendezvous #

    {
        "name": "MaxOrbits",
        "type": "value",
        "icon": "bg.png",
        "location": 2,
        "page": "Rendezvous",
        "label": "Max Orbits:",
        "value": "5"
    },
    {
        "name": "Distance",
        "type": "value",
        "icon": "bg.png",
        "location": 10,
        "page": "Rendezvous",
        "label": "Distance (m):",
        "value": "200"
    },
    {
        "name": "AutoWarpToggle",
        "type": "value",
        "icon": "bg.png",
        "location": 4,
        "page": "Rendezvous",
        "label": "AutoWarp:",
        "value": True,
        "toggle": True
    },

    {
        "name": "RendezvousExecute",
        "type": "action",
        "icon": "Rendezvous.png",
        "location": 0,
        "page": "Rendezvous",
        "callback": rendezvous,
        "value_buttons": [
            "MaxOrbits",
            "Distance",
            "AutoWarpToggle"
        ],
        "params": {
        }
    },

    *make_params("Rendezvous", "MaxOrbits", [1], 0, 1),
    *make_params("Rendezvous", "Distance", [10, 100], 1),

    {
        "name": "Exit",
        "type": "nav",
        "icon": "Exit.png",
        "location": 31,
        "page": "Rendezvous",
        "dest": "Home"
    },

    # Dock #

    {
        "name": "SpeedLimit",
        "type": "value",
        "icon": "bg.png",
        "location": 2,
        "page": "Dock",
        "label": "Vel. Limit (m/s):",
        "value": "1"
    },
    {
        "name": "DockRoll",
        "type": "value",
        "icon": "bg.png",
        "location": 10,
        "page": "Dock",
        "label": "Roll (°)",
        "value": "0"
    },
    {
        "name": "ForceRoll",
        "type": "value",
        "icon": "bg.png",
        "location": 8,
        "page": "Dock",
        "label": "Force Roll:",
        "value": False,
        "toggle": True
    },
    {
        "name": "SafeDistanceOverride",
        "type": "value",
        "icon": "bg.png",
        "location": 4,
        "page": "Dock",
        "label": "Start Override:",
        "value": False,
        "toggle": True
    },
    {
        "name": "StartDistanceOverride",
        "type": "value",
        "icon": "bg.png",
        "location": 12,
        "page": "Dock",
        "label": "Safe Override:",
        "value": False,
        "toggle": True
    },
    {
        "name": "DockExecute",
        "type": "action",
        "icon": "Dock.png",
        "location": 0,
        "page": "Dock",
        "callback": dock,
        "value_buttons": [
            "SpeedLimit",
            "DockRoll",
            "ForceRoll",
            "SafeDistanceOverride",
            "StartDistanceOverride"
        ],
        "params": {
        }
    },

    *make_params("Dock", "SpeedLimit", [0.1], 0, 1),
    *make_params("Dock", "DockRoll", [5], 1, 1),

    {
        "name": "Exit",
        "type": "nav",
        "icon": "Exit.png",
        "location": 31,
        "page": "Dock",
        "dest": "Home"
    },

    # Land #

    {
        "name": "LandingVel",
        "type": "value",
        "icon": "bg.png",
        "location": 10,
        "page": "Land",
        "label": "Land Vel (m/s):",
        "value": 0.5
    },

    {
        "name": "AutoWarpLand",
        "type": "value",
        "icon": "bg.png",
        "location": 1,
        "page": "Land",
        "label": "AutoWarp:",
        "value": True,
        "toggle": True,
    },
    {
        "name": "DeployGear",
        "type": "value",
        "icon": "bg.png",
        "location": 2,
        "page": "Land",
        "label": "Deploy Gear:",
        "value": True,
        "toggle": True,
    },
    {
        "name": "DeployChutes",
        "type": "value",
        "icon": "bg.png",
        "location": 3,
        "page": "Land",
        "label": "Deploy Chutes:",
        "value": True,
        "toggle": True,
    },
    {
        "name": "UseRCS",
        "type": "value",
        "icon": "bg.png",
        "location": 4,
        "page": "Land",
        "label": "Use RCS:",
        "value": True,
        "toggle": True,
    },

    *make_params("Land", "LandingVel", [0.1, 1], 1, 0),

    {
        "name": "LandExecute",
        "type": "action",
        "icon": "Land.png",
        "location": 0,
        "page": "Land",
        "callback": land,
        "value_buttons": [
            "LandingVel",
            "AutoWarpLand",
            "DeployGear",
            "DeployChutes",
            "UseRCS"
        ],
        "params": {
        }
    },

    {
        "name": "Exit",
        "type": "nav",
        "icon": "Exit.png",
        "location": 31,
        "page": "Land",
        "dest": "Home"
    },

    # Aircraft #

    {
        "name": "AltitudeHold",
        "type": "value",
        "icon": "bg.png",
        "location": 2,
        "page": "Aircraft",
        "label": "Alt. Hold:",
        "value": False,
        "toggle": True,
    },
    {
        "name": "VertSpeedHold",
        "type": "value",
        "icon": "bg.png",
        "location": 10,
        "page": "Aircraft",
        "label": "V. Speed Hold:",
        "value": False,
        "toggle": True,
    },
    {
        "name": "SpeedHold",
        "type": "value",
        "icon": "bg.png",
        "location": 18,
        "page": "Aircraft",
        "label": "Speed Hold:",
        "value": False,
        "toggle": True,
    },
    {
        "name": "AircraftRollHold",
        "type": "value",
        "icon": "bg.png",
        "location": 16,
        "page": "Aircraft",
        "label": "Roll Hold:",
        "value": False,
        "toggle": True,
    },
    {
        "name": "HeadingHold",
        "type": "value",
        "icon": "bg.png",
        "location": 27,
        "page": "Aircraft",
        "label": "Heading Hold:",
        "value": False,
        "toggle": True,
    },
    {
        "name": "AircraftAltitude",
        "type": "value",
        "icon": "bg.png",
        "location": 5,
        "page": "Aircraft",
        "label": "Altitude (m):",
        "value": 1000,
    },
    {
        "name": "AircraftVertSpeed",
        "type": "value",
        "icon": "bg.png",
        "location": 13,
        "page": "Aircraft",
        "label": "V. Speed (m/s):",
        "value": 100,
    },
    {
        "name": "AircraftSpeed",
        "type": "value",
        "icon": "bg.png",
        "location": 21,
        "page": "Aircraft",
        "label": "Speed (m/s):",
        "value": 300,
    },
    {
        "name": "AircraftHeading",
        "type": "value",
        "icon": "bg.png",
        "location": 29,
        "page": "Aircraft",
        "label": "Heading (°):",
        "value": 90,
    },
    {
        "name": "AircraftRoll",
        "type": "value",
        "icon": "bg.png",
        "location": 25,
        "page": "Aircraft",
        "label": "Roll (+180°):",
        "value": 180,
    },

    *make_params("Aircraft", "AircraftAltitude", [100, 1000], 0, 3),
    *make_params("Aircraft", "AircraftVertSpeed", [10, 100], 1, 3),
    *make_params("Aircraft", "AircraftSpeed", [10, 100], 2, 3),
    *make_params("Aircraft", "AircraftHeading", [10], 3, 4),
    *make_params("Aircraft", "AircraftRoll", [5], 3, 0),

    {
        "name": "AircraftUpdate",
        "type": "action",
        "icon": "AircraftUpdate.png",
        "location": 0,
        "page": "Aircraft",
        "callback": aircraft,
        "value_buttons": [
            "AltitudeHold",
            "VertSpeedHold",
            "SpeedHold",
            "AircraftRollHold",
            "HeadingHold",

            "AircraftAltitude",
            "AircraftVertSpeed",
            "AircraftSpeed",
            "AircraftRoll",
            "AircraftHeading"
        ],
        "params": {
            "enabled": True
        }
    },
    {
        "name": "AircraftOff",
        "type": "action",
        "icon": "AircraftOff.png",
        "location": 1,
        "page": "Aircraft",
        "callback": aircraft,
        "value_buttons": [],
        "params": {
            "enabled": False
        }
    },

    {
        "name": "Exit",
        "type": "nav",
        "icon": "Exit.png",
        "location": 31,
        "page": "Aircraft",
        "dest": "Home"
    },
]

