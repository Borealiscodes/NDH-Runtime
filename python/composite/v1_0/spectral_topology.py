from ndh_runtime.pipeline.v1_0 import (
    OperatorContext,
    spectral_step,
    topology_step,
)


def spectral_topology_step(
    ctx: OperatorContext,
    adjacency: float,
    resonance: float,
    add_nodes: int = 0,
    add_edges: int = 0,
) -> OperatorContext:
    """
    Composite operator:
    1. Apply spectral_step.
    2. Apply topology_step.
    All operations are reversible and non-activating.
    """
    ctx1 = spectral_step(ctx, adjacency=adjacency, resonance=resonance)
    ctx2 = topology_step(ctx1, add_nodes=add_nodes, add_edges=add_edges)
    return ctx2
