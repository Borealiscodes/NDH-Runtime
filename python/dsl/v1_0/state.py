class State:
    """
    NDH State semantic wrapper.
    Represents altitude-bounded, membrane-neutral state envelopes.
    """

    def __init__(
        self,
        altitude: int = 5,
        membrane: str = "neutral",
        adjacency_field: float = 0.0,
        resonance_field: float = 0.0,
        flow_field: float = 0.0,
        calm_load: float = 0.0,
        precl_buffer: float = 0.0,
    ):
        self.altitude = altitude
        self.membrane = membrane
        self.adjacency_field = adjacency_field
        self.resonance_field = resonance_field
        self.flow_field = flow_field
        self.calm_load = calm_load
        self.precl_buffer = precl_buffer

    def reversible_clone(self) -> "State":
        return State(
            altitude=self.altitude,
            membrane=self.membrane,
            adjacency_field=self.adjacency_field,
            resonance_field=self.resonance_field,
            flow_field=self.flow_field,
            calm_load=self.calm_load,
            precl_buffer=self.precl_buffer,
        )
