
"""Warning Class that helps produce warnings for the monitor system."""

class Warning:
    """Generates warning messages based on volcano status and selected style.

    Attributes:
        style (str): The style of warning ('sassy', 'poetic', or 'scientific').
    """
    def __init__(self, style="sassy"):
        """Initializes the warning system with a chosen style."""
        self.style = style

    def generate(self, volcano_name, status):
        """Generates a warning message based on the volcano's status.

        Args:
            volcano_name (str): The name of the volcano.
            status (str): The current status of the volcano.

        Returns:
            str: A formatted warning message.
        """
        if self.style == "sassy":
            if status == "eruption imminent":
                msg = f"{volcano_name} says: "
                msg += "You thought I was dormant? Cute, I was just "
                msg += "waiting for my dramatic entrance."
                return msg
            else:
                msg = f"{volcano_name} says: "
                msg += "Just taking a spa day in the magma chamber. "
                msg += "Don't get too comfortable."
                return msg
        elif self.style == "poetic":
            if status == "eruption imminent":
                msg = f"{volcano_name} whispers: "
                msg += "My fire stirs beneath the stone, prepare to flee, "
                msg += "leave me alone."
                return msg
            else:
                return f"{volcano_name} hums: I slumber deep, my rage asleep."
        else:  # scientific
            return f"{volcano_name} report: Status = {status}"

