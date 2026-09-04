class Topology:
    """
    NDH Topology semantic wrapper.
    Represents node/edge counts in runtime graphs.
    """

    def __init__(self, nodes: int = 0, edges: int = 0):
        self.nodes = nodes
        self.edges = edges

    def reversible_add_node(self) -> None:
        self.nodes += 1

    def reversible_add_edge(self) -> None:
        self.edges += 1
