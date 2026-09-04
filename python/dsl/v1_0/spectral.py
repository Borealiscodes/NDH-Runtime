class Spectral:
    """
    NDH Spectral semantic wrapper.
    Represents adjacency and resonance fields.
    """

    def __init__(self, adjacency: float = 0.0, resonance: float = 0.0):
        self.adjacency = adjacency
        self.resonance = resonance

    def reversible_update(self, adjacency: float, resonance: float) -> None:
        self.adjacency = adjacency
        self.resonance = resonance
