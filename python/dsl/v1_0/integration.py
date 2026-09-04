class Integration:
    """
    NDH Integration semantic wrapper.
    Represents integrated values over runtime flows.
    """

    def __init__(self, integrated_value: float = 0.0):
        self.integrated_value = integrated_value

    def reversible_integrate(self, delta: float) -> None:
        self.integrated_value += delta
