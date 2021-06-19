import krpc

# TODO: Refactor param names as attribute names
# https://stackoverflow.com/questions/2612610/how-to-access-object-attribute-given-string-corresponding-to-name-of-that-attrib

# Warp #
from helper import show

# TODO: Factor this out
warp_destinations = {
    "pe": "periapsis",
    "ap": "apoapsis",
    "soi": "SOI change",
    "node": "maneuver node"
}


# TODO: Finish cases
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
    conn.close()


# TODO: Try to implement tabbed page like in the MJ UI
# TODO: Using above layout, add all params
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
        if type(v.value) == bool:
            params[k] = v.value
        else:
            params[k] = int(v.value)

    conn = krpc.connect(name="Ascent Autopilot")
    ascent = conn.mech_jeb.ascent_autopilot
    ship = conn.space_center.active_vessel

    ascent.desired_orbit_altitude = params["OrbitAlt"]*1000
    ascent.ascent_path_classic.auto_path = True
    ascent.ascent_path_classic.turn_start_altitude = params["TurnAlt"]*1000
    ascent.ascent_path_classic.turn_start_velocity = params["TurnVel"]
    ascent.force_roll = params["RollToggle"]
    ascent.vertical_roll = params["ClimbRoll"]
    ascent.turn_roll = params["TurnRoll"]
    ascent.autodeploy_solar_panels = params["DeploySolar"]
    ascent.auto_deploy_antennas = params["DeployComms"]
    ascent.autostage = params["AutostageToggle"]
    ascent.staging_controller.autostage_limit = params["AutostageLimit"]
    ascent.skip_circularization = not params["CircularizeToggle"]
    ascent.corrective_steering = params["CorrectiveSteeringToggle"]

    ascent.enabled = True
    show(conn, "Launching...")
    ship.control.activate_next_stage()

    with conn.stream(getattr, ascent, "enabled") as enabled:
        enabled.rate = 1  # we don't need a high throughput rate, 1 second is more than enough
        with enabled.condition:
            while enabled():
                enabled.wait()

    conn.close()


def rendezvous(params):
    conn = krpc.connect(name="Rendezvous orbit")
    ren = conn.mech_jeb.rendezvous_autopilot
    node = conn.mech_jeb.node_executor

    # TODO: Factor out redundant code
    for k, v in params.items():
        if type(v.value) == bool:
            params[k] = v.value
        else:
            params[k] = int(v.value)

    ren.max_phasing_orbits = params["MaxOrbits"]
    ren.desired_distance = params["Distance"]
    node.autowarp = params["AutoWarpToggle"]

    ren.enabled = True
    show(conn, "Initiating rendezvous...")
    with conn.stream(getattr, ren, "enabled") as enabled:
        enabled.rate = 1  # we don't need a high throughput rate, 1 second is more than enough
        with enabled.condition:
            while enabled():
                enabled.wait()

    conn.close()


def dock(params):
    # TODO: Check all these naming conventions being used
    conn = krpc.connect(name="Rendezvous orbit")
    dock_a = conn.mech_jeb.docking_autopilot

    for k, v in params.items():
        if type(v.value) == bool:
            params[k] = v.value
        else:
            params[k] = int(v.value)

    dock_a.speed_limit = params["SpeedLimit"]
    dock_a.override_safe_distance = params["SafeDistanceOverride"]
    dock_a.override_start_distance = params["StartDistanceOverride"]
    dock_a.force_roll = params["ForceRoll"]
    dock_a.roll = params["DockRoll"]

    dock_a.enabled = True

    show(conn, "Docking with target...")
    with conn.stream(getattr, dock_a, "enabled") as enabled:
        enabled.rate = 1  # we don't need a high throughput rate, 1 second is more than enough
        with enabled.condition:
            while enabled():
                enabled.wait()

    conn.close()


def land(params):
    conn = krpc.connect(name="Landing")
    landing = conn.mech_jeb.landing_autopilot
    node = conn.mech_jeb.node_executor

    # TODO: Factor out redundant code
    for k, v in params.items():
        if type(v.value) == bool:
            params[k] = v.value
        else:
            params[k] = int(v.value)

    landing.touchdown_speed = params["LandingVel"]
    landing.deploy_gears = params["DeployGear"]
    landing.deploy_chutes = params["DeployChutes"]
    landing.rcs_adjustment = params["UseRCS"]
    node.autowarp = params["AutoWarpLand"]

    landing.land_untargeted()
    landing.enabled = True

    show(conn, "Landing...")
    with conn.stream(getattr, landing, "enabled") as enabled:
        enabled.rate = 1  # we don't need a high throughput rate, 1 second is more than enough
        with enabled.condition:
            while enabled():
                enabled.wait()

    conn.close()
