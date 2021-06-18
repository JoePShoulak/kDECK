import krpc

# Warp #

# TODO: Add message handling


def warp(params):
    destination = params["destination"]
    lead_time = int(params["value"])

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

    conn.space_center.warp_to(ut() + time - lead_time)

