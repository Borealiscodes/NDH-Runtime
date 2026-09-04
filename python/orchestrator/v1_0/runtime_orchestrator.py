from ndh_runtime.pipeline.v1_0 import OperatorContext
from ndh_runtime.composite.v1_0 import (
    spectral_topology_step,
    spectral_integration_step,
)


class RuntimeOrchestrator:
    """
    NDH Runtime Orchestrator v1.0

    Sequences composite operators into named flows.
    Non-activating, reversible, membrane-neutral.
    """

    def __init__(self):
        self.ctx = OperatorContext()

    def reversible_clone(self) -> "RuntimeOrchestrator":
        o = RuntimeOrchestrator()
        o.ctx = self.ctx.reversible_clone()
        return o

    def run_spectral_topology_flow(
        self,
        adjacency: float,
        resonance: float,
        add_nodes: int = 0,
        add_edges: int = 0,
    ) -> "RuntimeOrchestrator":
        new = self.reversible_clone()
        new.ctx = spectral_topology_step(
            new.ctx,
            adjacency=adjacency,
            resonance=resonance,
            add_nodes=add_nodes,
            add_edges=add_edges,
        )
        return new

    def run_spectral_integration_flow(
        self,
        adjacency: float,
        resonance: float,
        delta: float,
    ) -> "RuntimeOrchestrator":
        new = self.reversible_clone()
        new.ctx = spectral_integration_step(
            new.ctx,
            adjacency=adjacency,
            resonance=resonance,
            delta=delta,
        )
        return new
