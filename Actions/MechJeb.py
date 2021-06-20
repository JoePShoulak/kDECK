import krpc
from helper import show, parse, set_params

# TODO: Refactor param names as attribute names
# https://stackoverflow.com/questions/2612610/how-to-access-object-attribute-given-string-corresponding-to-name-of-that-attrib

# Warp #

# TODO: Factor this out

warp_destinations = {
    "time_to_periapsis": "periapsis",
    "time_to_apoapsis": "apoapsis",
    "time_to_soi_change": "SOI change",
    "node": "maneuver node"
}


# TODO: Finish cases
def warp(params):
    conn = krpc.connect(name="Warp")
    ut = conn.add_stream(getattr, conn.space_center, 'ut')
    my_vessel = conn.space_center.active_vessel
    nodes = my_vessel.control.nodes

    destination = params["destination"]
    lead_time = int(params["LeadTime"].value)

    if destination == "node" and nodes:
        time = nodes[0].time_to
    else:
        time = getattr(my_vessel.orbit, destination)

    show(conn, f'Warping to {warp_destinations[destination]}...')

    conn.space_center.warp_to(ut() + time - lead_time)
    conn.close()


# TODO: Try to implement tabbed page like in the MJ UI
# TODO: Using above layout, add all params
def smart_ass(params):
    conn = krpc.connect(name="Smart A.S.S.")
    smartass = conn.mech_jeb.smart_ass

    direction = params["direction"]

    smartass.autopilot_mode = getattr(conn.mech_jeb.SmartASSAutopilotMode, direction)
    show(conn, f'Smart A.S.S. set to {direction}')
    smartass.update(False)

    conn.close()


def launch(params):
    parse(params)

    conn = krpc.connect(name="Ascent Autopilot")
    ascent = conn.mech_jeb.ascent_autopilot
    ship = conn.space_center.active_vessel

    ascent.desired_orbit_altitude = params["OrbitAlt"]*1000
    ascent.ascent_path_classic.auto_path = True
    ascent.ascent_path_classic.turn_start_altitude = params["TurnAlt"]*1000
    ascent.ascent_path_classic.turn_start_velocity = params["TurnVel"]
    ascent.force_roll = params["ForceRoll"]
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
    conn = krpc.connect(name="Rendezvous Autopilot")
    ren = conn.mech_jeb.rendezvous_autopilot
    node = conn.mech_jeb.node_executor

    set_params(ren, params, node)

    ren.enabled = True
    show(conn, "Initiating rendezvous...")
    with conn.stream(getattr, ren, "enabled") as enabled:
        enabled.rate = 1  # we don't need a high throughput rate, 1 second is more than enough
        with enabled.condition:
            while enabled():
                enabled.wait()

    conn.close()


def dock(params):
    conn = krpc.connect(name="Docking Autopilot")
    dock_a = conn.mech_jeb.docking_autopilot

    set_params(dock, params)

    dock_a.enabled = True

    show(conn, "Docking with target...")
    with conn.stream(getattr, dock_a, "enabled") as enabled:
        enabled.rate = 1  # we don't need a high throughput rate, 1 second is more than enough
        with enabled.condition:
            while enabled():
                enabled.wait()

    conn.close()


def land(params):
    conn = krpc.connect(name="Landing Guidance")
    landing = conn.mech_jeb.landing_autopilot
    node = conn.mech_jeb.node_executor

    set_params(landing, params, node)

    landing.land_untargeted()
    landing.enabled = True

    show(conn, "Landing...")
    with conn.stream(getattr, landing, "enabled") as enabled:
        enabled.rate = 1  # we don't need a high throughput rate, 1 second is more than enough
        with enabled.condition:
            while enabled():
                enabled.wait()

    conn.close()


def aircraft(params):

    # TODO: Figure out v/s+-, roll_max

    conn = krpc.connect(name="Aircraft Autopilot")
    airplane = conn.mech_jeb.airplane_autopilot

    airplane.enabled = False  # Not sure why this has to be here, but apparently it does

    parse(params)

    if params["enabled"]:
        airplane.altitude_hold_enabled = params["AltitudeHold"]
        airplane.heading_hold_enabled = params["HeadingHold"]
        airplane.roll_hold_enabled = params["AircraftRollHold"]
        airplane.speed_hold_enabled = params["SpeedHold"]
        airplane.vert_speed_hold_enabled = params["VertSpeedHold"]

        airplane.altitude_target = params["AircraftAltitude"]
        airplane.heading_target = params["AircraftHeading"]
        airplane.roll_target = params["AircraftRoll"] - 180
        airplane.speed_target = params["AircraftSpeed"]
        airplane.vert_speed_target = params["AircraftVertSpeed"]

    airplane.enabled = params["enabled"]

    conn.close()
