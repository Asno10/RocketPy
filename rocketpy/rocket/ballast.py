class Ballast:
    """Represents a set of ballast weights installed on the rocket."""

    def __init__(self, mass_each: float, number: int, position: float):
        self.mass_each = float(mass_each)
        self.number = int(number)
        self.position = float(position)

    @property
    def mass(self) -> float:
        """Total mass of all ballast weights."""
        return self.mass_each * self.number
