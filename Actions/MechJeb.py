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
    my_body = my_orbit.body
    my_ref = my_vessel.reference_frame
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
    elif destination == "atmos":
        if my_body.has_atmosphere and my_orbit.periapsis < my_body.atmosphere_depth:
            pe_time = my_orbit.time_to_periapsis
            bin_delta = pe_time / 4
            guess_time = pe_time / 2
            guess_altitude = my_body.altitude_at(my_orbit.position_at(ut() + guess_time, my_ref))
            atmos = my_body.atmosphere_depth

    show(conn, f'Warping to {warp_destinations[destination]}...')

    conn.space_center.warp_to(ut() + time - lead_time)
    conn.close()

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
    conn.close()


def launch(params):
    for k, v in params.items():
        print(f'{k}: {v.value}')
