from models import Unit, db


def get_all_units():
    """
    Gets and returns all available units for recipe items.
    """

    all_units = Unit.query.all()

    serialized = [
        {
            "short": unit.short,
            "singular": unit.singular,
            "plural": unit.plural
        }
        for unit in all_units
    ]

    return {"units": serialized}
