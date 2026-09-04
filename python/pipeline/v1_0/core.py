from ndh_runtime.dsl.v1_0 import (
    State,
    Constraint,
    Spectral,
    Chart,
    Topology,
    Integration,
    Hook,
)


class OperatorContext:
    """
    NDH OperatorContext v1.0

    Holds the core runtime envelopes used by operator pipelines.
    Non-activating, reversible, membrane-neutral.
    """

    def __init__(self):
        self.state = State()
        self.constraint = Constraint()
        self.spectral = Spectral()
        self.chart = Chart()
        self.topology = Topology()
        self.integration = Integration()
        self.hook = Hook()

    def reversible_clone(self) -> "OperatorContext":
        ctx = OperatorContext()
        ctx.state = self.state.reversible_clone()
        ctx.constraint = Constraint(
            altitude_min=self.constraint.altitude_min,
            altitude_max=self.constraint.altitude_max,
            drift_neutral=self.constraint.drift_neutral,
            reversible=self.constraint.reversible,
        )
        ctx.spectral = Spectral(
            adjacency=self.spectral.adjacency,
            resonance=self.spectral.resonance,
        )
        ctx.chart.flow_map = list(self.chart.flow_map)
        ctx.topology.nodes = self.topology.nodes
        ctx.topology.edges = self.topology.edges
        ctx.integration.integrated_value = self.integration.integrated_value
        ctx.hook.registered = self.hook.registered
        return ctx
