import krpc


# TODO: Add message handling

# Science #


def science(params=None):
    event = params["event"]

    conn = krpc.connect(name="science")
    parts = conn.space_center.active_vessel.parts
    experiments = parts.experiments
    science_lab = parts.modules_with_name("ModuleScienceLab")[0]
    science_container = next(x for x in science_lab.part.modules if x.name == "ModuleScienceContainer")

    if event == "run":
        for ex in experiments:
            if not ex.inoperable and ex.available and not ex.has_data:
                ex.run()
