from Actions.KSP_Pe_Warp import warp_pe

layout = [
    # HOME #
    {
        "name": "MechJeb",
        "type": "nav",
        "icon": "MechJeb.png",
        "location": 0,
        "page": "Home",
        "dest": "MechJeb"
    },

    # MECHJEB #
    {
        "name": "WarpPE",
        "type": "action",
        "icon": "WarpPE.png",
        "location": 0,
        "page": "MechJeb",
        "callback": warp_pe
    },
    {
        "name": "Exit",
        "type": "nav",
        "icon": "Exit.png",
        "location": 31,
        "page": "MechJeb",
        "dest": "Home"
    },
]
