import krpc

# Maneuvers #

# Warp #


def warp(params):
    destination = params["destination"]
    lead_time = int(params["value"])

    print("got_here")
    print(f'Dest: {destination} Lead: {lead_time}')

    conn = krpc.connect(name="Smart Warp")
    ut = conn.add_stream(getattr, conn.space_center, 'ut')
    my_orbit = conn.space_center.active_vessel.orbit
    time = 0

    if destination == "pe":
        time = my_orbit.time_to_periapsis
    elif destination == "ap":
        time = my_orbit.time_to_apoapsis
    elif destination == "soi":
        time = my_orbit.time_to_soi_change

    conn.space_center.warp_to(ut() + time - lead_time)

