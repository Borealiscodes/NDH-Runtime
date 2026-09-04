class Chart:
    """
    NDH Chart semantic wrapper.
    Represents flow maps over envelopes.
    """

    def __init__(self):
        self.flow_map: list[float] = []

    def reversible_push(self, value: float) -> None:
        self.flow_map.append(value)
