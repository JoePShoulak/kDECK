import krpc


def warp_pe():
    conn = krpc.connect(name="Smart Warp")

    ut = conn.add_stream(getattr, conn.space_center, 'ut')

    my_orbit = conn.space_center.active_vessel.orbit

    conn.space_center.warp_to(ut() + my_orbit.time_to_periapsis)
