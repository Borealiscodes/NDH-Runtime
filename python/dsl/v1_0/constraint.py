class Constraint:
    """
    NDH Constraint semantic wrapper.
    Encodes altitude bounds and drift-neutrality.
    """

    def __init__(
        self,
        altitude_min: int = 4,
        altitude_max: int = 7,
        drift_neutral: bool = True,
        reversible: bool = True,
    ):
        self.altitude_min = altitude_min
        self.altitude_max = altitude_max
        self.drift_neutral = drift_neutral
        self.reversible = reversible

    def validate_altitude(self, altitude: int) -> bool:
        return self.altitude_min <= altitude <= self.altitude_max
