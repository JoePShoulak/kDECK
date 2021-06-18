import krpc

# Warp #
from helper import show

warp_destinations = {
    "pe": "periapsis",
    "ap": "apoapsis",
    "soi": "SOI change",
    "node": "maneuver node"
}


def warp(params):
    destination = params["destination"]
    lead_time = int(params["LeadTime"].value)

    conn = krpc.connect(name="Smart Warp")
    ut = conn.add_stream(getattr, conn.space_center, 'ut')
    my_vessel = conn.space_center.active_vessel
    my_orbit = my_vessel.orbit
    time = 0

    if destination == "pe":
        time = my_orbit.time_to_periapsis
    elif destination == "ap":
        time = my_orbit.time_to_apoapsis
    elif destination == "soi":
        time = my_orbit.time_to_soi_change
    elif destination == "node":
        nodes = my_vessel.control.nodes
        if nodes:
            next_node = nodes[0]
            time = next_node.time_to

    show(conn, f'Warping to {warp_destinations[destination]}...')

    conn.space_center.warp_to(ut() + time - lead_time)

# TODO: Try to implement tabbed page like in the MJ UI


def smart_ass(params):
    direction = params["direction"]
    conn = krpc.connect(name="Smart Ass")
    mj = conn.mech_jeb

    modes = mj.SmartASSAutopilotMode

    # Orbital
    if direction == "prograde":
        mode = modes.prograde
    elif direction == "retrograde":
        mode = modes.retrograde
    elif direction == "normal":
        mode = modes.normal_plus
    elif direction == "antinormal":
        mode = modes.normal_minus
    elif direction == "radialout":
        mode = modes.radial_plus
    elif direction == "radialin":
        mode = modes.radial_minus
    # Surface
    elif direction == "svel+":
        mode = modes.surface_prograde
    elif direction == "svel-":
        mode = modes.surface_retrograde
    elif direction == "hvel+":
        mode = modes.horizontal_plus
    elif direction == "hvel-":
        mode = modes.horizontal_minus
    elif direction == "surf":
        mode = modes.off  # TODO: Implement surface
    elif direction == "up":
        mode = modes.vertical_plus

    show(conn, f'Smart A.S.S. set to {direction}')

    mj.smart_ass.autopilot_mode = mode
