from .core import OperatorContext


def topology_step(ctx: OperatorContext, add_nodes: int = 0, add_edges: int = 0) -> OperatorContext:
    """
    NDH topology operator step.

    Adjusts node/edge counts in a reversible, structural manner.
    """
    new_ctx = ctx.reversible_clone()
    for _ in range(add_nodes):
        new_ctx.topology.reversible_add_node()
    for _ in range(add_edges):
        new_ctx.topology.reversible_add_edge()
    return new_ctx
